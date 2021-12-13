from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns=[
    path('list/',views.taskList,name="task_list"),
    path('detail/<int:id>/',views.taskDetail,name="task_detail"),
    path('create/',views.taskCreate,name="task_create"),
    path('update/<int:id>/',views.taskUpdate,name="task_update"),
    path('delete/<int:pk>/',views.taskDelete,name="task_delete"),

]