from django.db import models
from django.contrib.auth.models import User
import datetime

from django.db.models.deletion import CASCADE

# Create your models here.
class Request(models.Model):
    owner = models.ForeignKey(User, on_delete=CASCADE)
    course_name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    masters = models.BooleanField()
    bachelor = models.BooleanField()
    prof_fname = models.CharField(max_length=30)
    prof_lname = models.CharField(max_length=30)
    date = models.DateField(auto_now_add=True, blank=True)
    datetime = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.course_name + '(' + str(self.id) + ')'

class Timing(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    day = models.CharField(max_length=15)
    start = models.TimeField()
    end = models.TimeField()
    def __str__(self):
        return str(self.request)

class Reply(models.Model):
    owner = models.ForeignKey(User, on_delete=CASCADE)
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    reply_text = models.CharField(max_length=500)
    replier_fname = models.CharField(max_length=30)
    replier_lname = models.CharField(max_length=30)
    is_accepted = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.reply_text

class StoredReplies(models.Model):
    owner = models.ForeignKey(User, on_delete=CASCADE)
    reply = models.ForeignKey(Reply, on_delete=CASCADE)
    datetime_of_bookmark = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.owner.first_name + " " + self.owner.last_name + " " + self.reply.reply_text 