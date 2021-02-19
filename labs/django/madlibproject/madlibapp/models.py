from django.db import models

# Create your models here.
class MadLib(models.Model):
    title = models.CharField(max_length=200)
    template = models.TextField()

    def __str__(self):
        return self.title
    

class MadLibWord(models.Model):
    madlib = models.ForeignKey(MadLib, on_delete=models.PROTECT, related_name='words')
    variable_name = models.CharField(max_length=200)
    part_of_speech = models.CharField(max_length=200)


    def __str__(self):
        return self.variable_name
    