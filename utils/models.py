from django.db import models

class WikiModel(models.Model):
    created_at = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on wich the object was created.'
    )
    modified_at = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Date time on wich the object was last modified.'
    )

    class Meta:
        abstract = True
        get_latest_by = 'created_at'
        ordering = ['-created_at', '-modified_at']

