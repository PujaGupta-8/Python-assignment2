from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    TODO = 'To Do'
    IN_PROGRESS = 'In Progress'
    COMPLETED = 'Completed'

    STATUS_CHOICES = [
        (TODO, 'To Do'),
        (IN_PROGRESS, 'In Progress'),
        (COMPLETED, 'Completed'),
    ]

    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'

    PRIORITY_CHOICES = [
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=TODO)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default=MEDIUM)
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)

    def _str_(self):
        return self.title
        
class TaskAssignment(models.Model):
    task = models.ForeignKey(Task, related_name='assignments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='assignments', on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.user.username} assigned to {self.task.title}"

class Comment(models.Model):
    task = models.ForeignKey(Task, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"Comment by {self.user.username} on {self.task.title}"
