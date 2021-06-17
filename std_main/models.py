from teach_main.models import Request
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class StoredRequests(models.Model):
    owner = models.ForeignKey(User, on_delete=CASCADE)
    request = models.ForeignKey(Request, on_delete=CASCADE)
    datetime_of_bookmark = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.owner.first_name + " " + self.owner.last_name + " " + self.request.course_name 