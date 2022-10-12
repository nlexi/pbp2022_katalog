from django.urls import path
from todolist.views import show_todolist
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import add_task
from todolist.views import finish_task
from todolist.views import delete_task
from todolist.views import show_json
from todolist.views import add


app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', add_task, name='addtask'),
    path('delete_task/<int:id>', delete_task, name='delete_task_id'),
    path('finish_task/<int:id>', finish_task, name='finish_task_id'),
    path('json/', show_json, name="show_json"),
    path('add/', add, name='add'),
]