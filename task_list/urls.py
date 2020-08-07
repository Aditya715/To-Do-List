from django.urls import path
from .views import (
    dashboard, 
    add_new,
    mark_me_complete
)  

app_name = 'task_list'

urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('add/', add_new, name="add_new"),
    path('markComplted/', mark_me_complete, name="mark_me_complete")
]