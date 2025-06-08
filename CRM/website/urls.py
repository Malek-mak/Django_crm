from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
    path('record/<int:pk>', views.customer_record, name='record'),
    path('delete/<int:pk>', views.delete_record, name='delete'),
    path('add_record/', views.add_record, name='add'),
    path('update/<int:pk>', views.update_record, name='update'),
]
