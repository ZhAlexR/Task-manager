from django.urls import path

from manager.views import (
    index_view,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView, TagListView, TagCreateView
)

app_name = "manager"

urlpatterns = [
    path("", index_view, name="index"),
    path("tasks/crate/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete", TaskDeleteView.as_view(), name="task-delete"),
    path("tags/list/", TagListView.as_view(), name="tag-list"),
    path("tags/crate/", TagCreateView.as_view(), name="tag-create"),
]
