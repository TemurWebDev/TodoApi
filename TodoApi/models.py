from django.db import models

class Task(models.Model):
    STATUS_CHOICES = [
        ('todo', 'Todo'),
        ('in_progress', 'In progress'),
        ('done', 'Done'),
        ('expired', 'Expired'),
    ]
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(choices=STATUS_CHOICES, default='todo', max_length=20)

    def __str__(self):
        return self.title
