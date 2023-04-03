from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic

from manager.forms import TaskForm
from manager.models import Task, Tag


def index_view(request):
    tasks = Task.objects.all()
    context = {
        "tasks": tasks
    }

    return render(request, "manager/index.html", context=context)


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("manager:index")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("manager:index")


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("manager:index")


class TagListView(LoginRequiredMixin, generic.ListView):
    model = Tag
    template_name = "manager/tags.html"
