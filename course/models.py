from django.db import models

class Courses(models.Model):
    courseName = models.CharField(max_length=50, unique=True)
    courseFee  = models.IntegerField()
    courseDuration = models.CharField(max_length=50)

class Signup(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    last_login = models.DateTimeField(null=True, blank=True)  # Added last_login field
    is_superuser = models.BooleanField(default=False)  # Added is_superuser field

class Admin_Signup(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    last_login = models.DateTimeField(null=True, blank=True)  # Added last_login field
    is_superuser = models.BooleanField(default=False)  # Added is_superuser field

    def get_superuser_details(self):
        if self.is_superuser:
            return {
                'firstName': self.firstName,
                'lastName': self.lastName,
                'email': self.email,
                'last_login': self.last_login
            }
        return None
