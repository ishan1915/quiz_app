from django.db import models

class Quiz(models.Model):
    title = models.CharField(max_length=255)
    question = models.CharField(max_length=255)
    option1 = models.CharField(max_length=50)
    option2 = models.CharField(max_length=50)
    option3 = models.CharField(max_length=50)
    option4 = models.CharField(max_length=50)
    correct_option = models.CharField(max_length=50, choices=[
        ('option1', 'Option 1'),
        ('option2', 'Option 2'),
        ('option3', 'Option 3'),
        ('option4', 'Option 4'),
    ])




    def __str__(self):
        return self.title

 