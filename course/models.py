from django.db import models

class Courses(models.Model):  # Adding the Courses model
    courseName = models.CharField(max_length=100)
    courseFee = models.DecimalField(max_digits=10, decimal_places=2)
    courseDuration = models.CharField(max_length=100)

class Signup(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    username = models.CharField(max_length=100, default='zoro', db_collation='utf8_bin')
    email = models.EmailField(unique=True,db_collation='utf8_bin')  # Ensure email is case-sensitive
    password = models.CharField(max_length=100)
    last_login = models.DateTimeField(null=True, blank=True) 
    is_superuser = models.BooleanField(default=False)  

class Admin_Signup(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True, default='zoro', db_collation='utf8_bin')  # Added username field
    email = models.EmailField(unique=True,db_collation='utf8_bin')  # Updated to ensure email is unique
    password = models.CharField(max_length=100)
    last_login = models.DateTimeField(null=True, blank=True)  # Added last_login field
    is_superuser = models.BooleanField(default=False)  # Added is_superuser field

    def get_superuser_details(self):
        if self.is_superuser:
            return {
                'username': self.username,
                'firstName': self.firstName,
                'lastName': self.lastName,
                'email': self.email,
                'last_login': self.last_login
            }
        return None

class Notification(models.Model):
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.message
