from django.db import models
from django.contrib.auth.models import User
# from account_app.models import CustomUser


# Create your models here.

class ToDoItem(models.Model):
    title = models.CharField(max_length=110, unique=True)
    description = models.TextField(max_length=400, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    checked = models.BooleanField(default=False, null=False)
    owner = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    # owner = models.ForeignKey(User,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
