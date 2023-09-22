from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, RegisterPage
from .views import update_order
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', TaskList.as_view(), name='task'),
    path('task-create/', CustomLoginView.as_view(), name='login'),
    path('login/', TaskCreate.as_view(), name='tasks-create'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='tasks-detail'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
    
    # path('update_order/', update_order, name='update_order'),
   
]
