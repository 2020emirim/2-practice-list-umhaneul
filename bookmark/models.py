from django.db import models

class Bookmark(models.Mode):
    site_name = models.CharField(max_length=20)
    url = models.URLField('Site URL')