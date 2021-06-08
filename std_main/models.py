from teach_main.models import Request
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class StoredRequests(models.Model):
    owner = models.ForeignKey(User, on_delete=CASCADE)
    request = models.ForeignKey(Request, on_delete=CASCADE)