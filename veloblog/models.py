# -*- coding: utf-8 -*-
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255) # header
    datetime = models.DateTimeField(u'Дата публикации') # дата публикации
    content = models.TextField(max_length=10000) # текст поста

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/veloblog/%i/" % self.id