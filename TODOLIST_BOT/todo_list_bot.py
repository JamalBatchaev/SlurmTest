from aiogram import Bot, Dispatcher, types
from aiogram.utils.callback_data import CallbackData

from settings import settings
from task import Task
from task_repository import TaskRepository

import typing

bot = Bot(token=settings["TELEGRAM_TOKEN"])
dispatcher = Dispatcher(bot)
clear_cb = CallbackData("clear", "action")

tasks = []

_repository = TaskRepository()


def _task_dto_to_string(task: Task) -> str:
    status_char = "\u2705" if task.is_done else "\u274c"
    return f"{task.id}: {task.text} | {status_char}"


def _get_keyboard():
    return types.InlineKeyboardMarkup().row(
        types.InlineKeyboardButton(
            "Удалить все!", callback_data=clear_cb.new(action="all")
        ),
        types.InlineKeyboardButton(
            "Только завершенные", callback_data=clear_cb.new(action="completed")
        ),
    )


@dispatcher.message_handler(commands=["todo"])
async def create_task(message: types.Message):
    _repository.add_task(message.get_args())
    await message.reply(f"Задача добавлена: {''.join(filter(str.isdigit, map(str, _repository.added_id)))}")

@dispatcher.message_handler(commands=["add_subtask"])
async def create_subtask(message: types.Message):
    try:
        args = message.get_args().strip().split(maxsplit=1)
        parent_id = int(args[0]) 
        text = args[1]
        _repository.add_subtask(parent_id, text)
        text = f"Задача добавлена: {''.join(filter(str.isdigit, map(str, _repository.added_id)))}"
    except ValueError as e:
        text = "Неправильный номер задачи"

    await message.reply(text)


@dispatcher.message_handler(commands=["list"])
async def get_list(message: types.Message):
    tasks = _repository.get_list()
    if tasks:
        task_dict = {}  
        for task in tasks:
            task_dict[task.id] = task

        text = ""
        for task in tasks:
            if task.parent_id is None:  
                text += f"{_task_dto_to_string(task)}\n"  
                for subtask in tasks:
                    if subtask.parent_id == task.id:  
                        text += f"    {_task_dto_to_string(subtask)}\n" 
    else:
        text = "У вас нет задач!"
    await bot.send_message(message.chat.id, text)

@dispatcher.message_handler(commands=["find"])
async def get_tasks(message: types.Message):
    tasks = _repository.find_task(message.get_args())
    if tasks:
        text = "\n".join([_task_dto_to_string(res) for res in tasks])
    else:
        text = "Задач по запросу не найдено"
    await bot.send_message(message.chat.id, text)


@dispatcher.message_handler(commands=["done"])
async def finish_task(message: types.Message):
    try:
        task_ids = [int(id_) for id_ in message.get_args().split(" ")]
        _repository.finish_tasks(task_ids)
        text = f"Завершенные задачи: {task_ids}"
    except ValueError as e:
        text = "Неправильный номер задачи"

    await message.reply(text)

@dispatcher.message_handler(commands=["reopen"])
async def reopen_task(message: types.Message):
    try:
        task_ids = [int(id_) for id_ in message.get_args().split(" ")]
        _repository.reopen_task(task_ids)
        text = f"Переоткрытые задачи: {task_ids}"
    except ValueError as e:
        text = "Неправильный номер задачи"

    await message.reply(text)

@dispatcher.message_handler(commands=["clear"])
async def clear(message: types.Message):
    await message.reply("Вы хотите удалить ваши задачи?", reply_markup=_get_keyboard())


@dispatcher.callback_query_handler(clear_cb.filter(action=["all", "completed"]))
async def callback_clear_action(
    query: types.CallbackQuery, callback_data: typing.Dict[str, str]
):
    await query.answer()
    callback_data_action = callback_data["action"]

    if callback_data_action == "all":
        _repository.clear()
    else:
        _repository.clear(is_done=True)

    await bot.edit_message_text(
        f"Задачи удалены! ",
        query.from_user.id,
        query.message.message_id,
    )

@dispatcher.message_handler(commands=["help"])
async def clear(message: types.Message):
    with open('help.txt', 'r', encoding='utf-8') as file:
        help_text = file.read()
    await message.reply(help_text)