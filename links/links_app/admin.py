from django.contrib import admin
from .models import Bookmark, Collections

# Register your models here.
admin.site.register(Bookmark)
admin.site.register(Collections)