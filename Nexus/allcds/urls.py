from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('logout/',views.logout_user,name='logout'),
    path('records/',views.records,name='records'),
    path('register/',views.register_user,name='register'),
    path('record/<int:pk>',views.precord,name='record'),
    path('delete_record/<int:pk>',views.del_precord,name='delete_record'),
    path('add_record/',views.add_precord,name='add_record'),
]
