from django.urls import path

from manager.views import (
    index_view,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView, TagListView
)

app_name = "manager"

urlpatterns = [
    path("", index_view, name="index"),
    path("task/crate/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete", TaskDeleteView.as_view(), name="task-delete"),
    path("tags/list/", TagListView.as_view(), name="tag-list"),
]
