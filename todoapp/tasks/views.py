from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Task
from .forms import TaskCreateForm, TaskUpdateForm

# Create your views here.
class TaskListView(ListView):
    model = Task
    template_name = "tasks_list.html"


class TaskCreateView(CreateView):
    model = Task
    template_name = "task_create.html"
    form_class = TaskCreateForm
    success_url = "/todo/list"


class TaskUpdateView(UpdateView):
    model = Task
    template_name = "task_update.html"
    form_class = TaskUpdateForm
    success_url = "/todo/list"


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_delete.html'
    success_url = "/todo/list"