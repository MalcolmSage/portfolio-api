from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):
    options = (
        ('wip', 'WIP'),
        ('mvp', 'MVP'),
        ('prp', 'PRP'),
    )

    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, default=1
    )
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='documented')
    documented = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=10, choices=options, default='WIP'
    )
    objects = models.Manager()
    tags = ArrayField(models.CharField(max_length=200), blank=True)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ('-documented',)

    def __str__(self):
        return self.title