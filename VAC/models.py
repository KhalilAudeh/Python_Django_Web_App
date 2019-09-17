from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    description = models.TextField()
    date_from = models.DateField(blank=False,)
    date_to = models.TextField()                                
    time_from = models.TextField()
    time_to = models.TextField()
    duration_of_the_whole_trip = models.TextField()
    # for the duration, subtract the date_to from date_from
    who_posted = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.description

    # for PostCreateView
    #def get_absolute_url(self):
     #  return reverse('VAC-home', kwargs={'pk': self.pk})