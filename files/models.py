import os
from django.conf import settings 
from django.db import models  

from django.contrib.auth import get_user_model
User = get_user_model()

def get_file_path(instance, filename):
    return os.path.join('file', str(instance.user), filename)

class Invoice(models.Model):     
    user = models.ForeignKey(User, on_delete=models.CASCADE)     
    file = models.FileField(upload_to=get_file_path)
