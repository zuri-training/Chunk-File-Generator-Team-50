from time import timezone
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class ChunkCsv(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
