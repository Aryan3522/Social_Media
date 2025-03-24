from django.urls import path


from django.views.generic.base import TemplateView
from . import views

urlpatterns = [ 

    # home url
    path('', TemplateView.as_view(template_name="index.html"), name="home"),
    
    # signin and login urls
    path('signin/', views.create, name="create"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    
    # profile urls
    path('profile/', views.profile, name="profile"),
    
    # update
    path('edit/<int:id>/', views.edit, name="edit"),
    path('update/<int:id>/', views.update, name="update"),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('admin_edit/', views.admin_edit, name='admin_edit'),
    
    # read page urls + delete
    path('read/', views.read, name='read'),
    path('delete/<int:id>/', views.delete, name="delete"),
    
    # Admin data URL
    path('admin_data/', views.admin_data, name='admin_data'),  # Add this line for admin data view
]
