from django.contrib import admin
from .models import Courses,Signup
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'courseName', 'courseFee','courseDuration')


class SignupAdmin(admin.ModelAdmin):
    list_display = ('id','firstName','lastName','email', 'is_superuser')  # Added is_superuser field to display


admin.site.register(Courses,CourseAdmin)
admin.site.register(Signup,SignupAdmin)
