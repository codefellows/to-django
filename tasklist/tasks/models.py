from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

class TaskManager(models.Manager):
    """a docstring"""

    def get_queryset(self):
        return super(TaskManager, self).get_queryset().filter(complete=False)

CATEGORY_CHOICES = [
    ('W', 'work'), ('S', 'school'), ('H', 'home')
]

@python_2_unicode_compatible
class Task(models.Model):
    """docstring for Task."""

    title = models.CharField(max_length=255)
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES, default='W')
    due_date = models.DateTimeField(null=True, blank=True)
    complete = models.BooleanField(default=False)

    objects = models.Manager()
    incomplete_tasks = TaskManager()

    def __repr__(self):
        return "<Task: {} category: {} complete: {}>".format(self.title, self.category, self.complete)

    def __str__(self):
        self.__repr__()
