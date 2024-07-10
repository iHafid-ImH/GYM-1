from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Trainer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    specialty = models.CharField(max_length=100)
    date_joined = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField()
    date_joined = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Subscription(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    membership_type = models.CharField(max_length=50, choices=[('monthly', 'Monthly'), ('annual', 'Annual')])

    def __str__(self):
        return f'Subscription of {self.member} with {self.trainer}'
    
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    image = models.ImageField(upload_to='blog_images/',blank=True,null=True)
    
    def __str__(self):
        return f"{self.name} - {self.subject}"

