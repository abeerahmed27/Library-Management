from django.contrib import admin

from lib.views import showbooks
from .models import AddBook
from .models import RBook
# Register your models here.
admin.site.register(AddBook)
admin.site.register(RBook)