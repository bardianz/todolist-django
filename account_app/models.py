from django.db import models
from django.contrib.auth.models import AbstractUser,User
from PIL import Image


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    avatar = models.ImageField(default='media/images/default-avatar.png' , upload_to='media/images/avatars',blank=True,null=True)

    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (300, 300)
            img.thumbnail(new_img)
            img.save(self.avatar.path)

# class CustomUser(AbstractUser):
#     firstname = models.CharField(max_length=70, blank=True,null=True )
#     lastname = models.CharField(max_length=70,blank = True,null=True )
#     email = models.EmailField(max_length=110,blank = True,null=True,unique=True )