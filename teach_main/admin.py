from django.contrib import admin

from .models import Timing
from .models import Request
from .models import Reply

admin.site.register(Timing)
admin.site.register(Request)
admin.site.register(Reply)


# Register your models here.
