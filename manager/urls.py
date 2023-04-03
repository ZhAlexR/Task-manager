from django.urls import path

from manager.views import index_view, TaskCreateView

app_name = "manager"

urlpatterns = [
    path("", index_view, name="index"),
    path("task/crate", TaskCreateView.as_view(), name="task")
]
