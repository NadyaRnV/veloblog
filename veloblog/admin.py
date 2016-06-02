from django.contrib import admin

from veloblog.models import Post # наша модель из blog/models.py

admin.site.register(Post)
