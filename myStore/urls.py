from django.contrib import admin
from django.urls import path, include
from course.views import custom_404_view  # Import the custom 404 view
handler404 = custom_404_view  # Set the custom 404 handler

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('course.urls'))
]
