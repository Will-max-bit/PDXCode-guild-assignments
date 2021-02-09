from django.db import models

# Create your models here.
class Priority(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    


class ToDoItem(models.Model):
    text = models.CharField(max_length=200)
    priority = models.ForeignKey(Priority, on_delete=models.PROTECT, related_name='Priority')
    created_date = models.DateTimeField()
    completed_date = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.text
    
