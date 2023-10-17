from django.urls import path
from enroll import views

urlpatterns = [
    path('',views.add_show,name='homepage'),
    path('delete/<int:id>/',views.delete_data,name="delete_data"),
    path("<int:id>/",views.update_data,name='updatedata')
]