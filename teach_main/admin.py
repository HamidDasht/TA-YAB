from django.contrib import admin

from .models import Timing, Request, Reply, StoredReplies

admin.site.register(Timing)
admin.site.register(Request)
admin.site.register(Reply)
admin.site.register(StoredReplies)


# Register your models here.
