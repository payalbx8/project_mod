from django.db import models

class contact(models.Model):
    name = models.CharField(max_length=122)
    email =  models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name