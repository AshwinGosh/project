from django.db import models

class feedback(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=50)
    phone = models.IntegerField(max_length=15 ,null=True,blank=True)
    password = models.CharField(max_length=100)
class Announcement(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title