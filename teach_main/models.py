from django.db import models
import datetime

# Create your models here.
class Request(models.Model):
    course_name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    masters = models.BooleanField()
    bachelor = models.BooleanField()
    prof_fname = models.CharField(max_length=30)
    prof_lname = models.CharField(max_length=30)
    prof_id = models.CharField(max_length=6)
    date = models.DateField(auto_now_add=True, blank=True)
    #datetime = models.DateTimeField(auto_now_add=True, blank=True)
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
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    reply_text = models.CharField(max_length=500)
    replier_fname = models.CharField(max_length=30)
    replier_lname = models.CharField(max_length=30)
    replier_id = models.CharField(max_length=7)
    def __str__(self):
        return self.reply_text
