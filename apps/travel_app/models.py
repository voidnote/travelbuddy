from __future__ import unicode_literals
from django.db import models
from .. first_app.models import User


class TripManager(models.Manager):
    def createTrip(self, postData):
        errorStr = []
        if len(postData['destination']) < 1:
            errorStr.append("Destination name can't be empty")
        if len(postData['description']) < 3:
            errorStr.append("Description can't be empty")

        response_to_views = {}
        if errorStr:
            response_to_views['status'] = False
            response_to_views['errorStr'] = errorStr
        else:
            trip = self.create(created_by = User.object.get(id=postData["id"]), destination = postData["destination"], description = postData["description"], date_from = postData["date_from"], date_to = postData["date_to"])
            response_to_views['status'] = True
            response_to_views['tripobj'] = trip
        return response_to_views

class Trip(models.Model):
  created_by = models.ForeignKey(User, related_name="my_trips")
  destination = models.TextField(max_length=100)
  description = models.TextField(max_length=100)
  date_from = models.DateField()
  date_to = models.DateField()
  attendees = models.ManyToManyField(User, related_name = "trips_attending")
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  objects = TripManager()
