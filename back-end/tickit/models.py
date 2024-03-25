from django.db import models

# Create your models here.

class State(models.Model):
  state = models.CharField(max_length=100, default='no state name')
  city = models.CharField(max_length=100, default='no city name')
  city_img = models.TextField(max_length=300, default='')

  def __str__(self):
    return self.state
  
class Venue(models.Model):
  state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='venue')
  name = models.CharField(max_length=100, default='no venue name')
  state = models.CharField(max_length=100, default='no state name')
  city = models.CharField(max_length=100, default='no city name')
  venue_img = models.TextField(max_length=300, default='')

  def __str__(self):
    return self.name
  
class Event(models.Model):
  venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='event')
  name = models.CharField(max_length=100, default='no event name')
  event_type = models.CharField(max_length=100, default='no event type')
  date = models.DateTimeField()
  seating_type = models.CharField(max_length=100, default='no seating type')
  cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
  event_img = models.TextField(max_length=300, default='')

  def __str__(self):
    return self.name