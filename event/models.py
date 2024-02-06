from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='event/images/')  # You may specify the upload_to path as per your requirement
    description = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    event_date = models.DateField()

    class Meta:
        ordering = ['created_date']
        

    def __str__(self):
        return self.title