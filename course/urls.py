from django.urls import path
from . import views
from django.urls import path
from . import views

handler404 = views.custom_404_view  # Set the custom 404 view

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.create, name='signup'),
    path('login/', views.login, name='login'),
    # path('admin_data/', views.admin_data, name='admin_data'),
    path('approve_superuser/', views.approve_superuser, name='approve_superuser'),
    path('handle_approval/<int:user_id>/<str:approve>/', views.handle_approval , name='handle_approval'),
    
    # signin and login urls
    path('signin/', views.create, name="create"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    
    # profile urls
    path('profile/', views.profile, name="profile"),
    
    # update
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    
    # read page urls + delete
    # path('read/', views.read, name='read'),
    path('delete/<int:id>/', views.delete, name="delete"),
    
    # Admin data URL
    path('admin_data/', views.admin_data, name='admin_data'), 
]
