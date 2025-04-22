from django.urls import path
from . import views
from django.urls import path
from . import views

# handler404 = views.custom_404_view  # Set the custom 404 view

urlpatterns = [
    path('', views.home, name='home'),
    path('add_image/', views.add_image, name='add_img'),
    path('signup/', views.create, name='signup'),
    path('login/', views.login, name='login'),
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
    path('forgot_password/', views.forgot_password, name="forgot_password"),
    
    # read page urls + delete
    path('delete/<int:id>/', views.delete, name="delete"),
    path('delete_post/<int:id>/', views.deletePost, name="dlt_post"),
    
    # Admin data URL
    path('admin_data/', views.admin_data, name='admin_data'),
]
