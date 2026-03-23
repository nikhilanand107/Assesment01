from django.urls import path

from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("add/", views.add_task, name="add_task"),
    path("categories/", views.categories, name="categories"),
    path("task/<int:task_id>/", views.task_detail, name="task_detail"),
    path("edit/<int:task_id>/", views.edit_task, name="edit_task"),
    path("delete/<int:task_id>/", views.delete_task, name="delete_task"),
    path("register/", views.register, name="register"),
]
