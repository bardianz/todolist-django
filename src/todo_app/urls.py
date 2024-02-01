from django.urls import path
from .views import *

app_name = "todo_app"

urlpatterns = [
    path("", home_view, name="home"),
    # path("dashboard/", dashboard_view, name="dashboard"),
    path("aboutus/", about_us_view, name="about_us"),
    path('tasks/', items_list_view, name='tasks_list'),
    path('new_task', create_new_task, name='new_task'),
    path('<id>/delete', delete_task, name='delete_task'),
    path('tasks/<id>/edit', edit_task_view, name='edit_task'),
    path('tasks/<id>', task_detail_view, name='task_detail'),
]