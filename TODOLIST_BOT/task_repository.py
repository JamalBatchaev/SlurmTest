from db import tasks, engine
from task import Task

from typing import List


class TaskRepository:
    def __init__(self) -> None:
        self.added_id = None
    
    def add_task(self, text: str):
        query = tasks.insert().values(text=text)
        with engine.connect() as conn:
            self.added_id=conn.execute(query).inserted_primary_key
            conn.commit()
    
    def reopen_task(self, ids: List[int]):
        query = tasks.update().where(tasks.c.id.in_(ids)).values(is_done=False)
        with engine.connect() as conn:
            conn.execute(query)
            conn.commit()
    
            

    def get_list(self, is_done=None) -> List[Task]:
        query = tasks.select()

        if is_done != None:
            query = query.where(is_done=is_done)

        result = []
        with engine.connect() as conn:
            result = [
                Task(id=id, text=text, is_done=is_done)
                for id, text, is_done in conn.execute(query.order_by(tasks.c.id))
            ]

        return result
    

    def find_task(self, textlike: str) -> List[Task]:
        query = tasks.select()
        query = query.where(tasks.c.text.ilike(f'%{textlike}%'))

        result = []
        with engine.connect() as conn:
            result = [
                Task(id=id, text=text, is_done=is_done)
                for id, text, is_done in conn.execute(query.order_by(tasks.c.id))
            ]

        return result
    


    def finish_tasks(self, ids: List[int]):
        query = tasks.update().where(tasks.c.id.in_(ids)).values(is_done=True)
        with engine.connect() as conn:
            conn.execute(query)
            conn.commit()

    def clear(self, is_done=None):
        query = tasks.delete()

        if is_done is not None:
            query = query.where(tasks.c.is_done == is_done)

        with engine.connect() as conn:
            conn.execute(query)
            conn.commit()
