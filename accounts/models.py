from django.contrib.auth.models import AbstractUser # abstractuser allows us to extend django's inbuilt authentication functionality
from django.db import models

# Create your models here. email, password fields will come from our abstract  user
class User(AbstractUser):
    # define our roles
    USER_TYPE_CHOICE = (
        ('student', 'Student')
        ('teacher', 'Teacher')
        # these are roles that i want extended to my AbstractUser which is the model existing from django
    )

    # table columns
    user_type = models.CharField(max_length=50, choices=USER_TYPE_CHOICE)
    # Choices is a new constraint
    profile_image = models.ImageField(upload_to='profiles/', null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True, null=True)

    # methods that any of the objects can access within my app
    def __str__(self):
        return f"{self.username} - {self.email}"
    
    def is_teacher(self):
        return self.user_type == 'teacher'
    
    def is_student(self):
        return self.user_type == 'student'
    
    # the above is an example of a custom user model which extends the django native user model
