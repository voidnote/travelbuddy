from django.shortcuts import render, redirect
from .. first_app.models import User
from .models import Trip
from django.core.urlresolvers import reverse
from django.contrib import messages


def travels(request, userid, route): 
	context = {
	"user" : User.object.get(id=userid),
	"route" : route,
	"itinerary" : Trip.objects.filter(created_by=userid)|Trip.objects.filter( attendees=userid),
	"otherplans" : Trip.objects.exclude(created_by=userid)|Trip.objects.exclude(attendees=userid)
	}
	return render(request, "travel_app/travels.html", context)

def addplan(request, id): 
	context = {
	"user" : User.object.get(id=id),
	}
	return render(request, "travel_app/add.html", context)

def createPlan(request, id): 
	if request.method == "POST":
		response_from_models = Trip.objects.createTrip(request.POST)
		if not response_from_models["status"]:
			for error in response_from_models["errorStr"]:
				messages.error(request, error)
			return redirect("/travel/addplan/"+str(id))
	newtrip = response_from_models["tripobj"]
	this_user =  User.object.get(id=id)
	newtrip.attendees.add(this_user)
	route = "post"
	return redirect("/travel/"+str(id)+"/"+route)

def joinTrip(request, userid, tripid): 
	this_trip = Trip.objects.get(id=tripid)
	this_user =  User.object.get(id=userid)
	this_trip.attendees.add(this_user)
	route = "join"
	return redirect("/travel/"+str(userid)+"/"+route)

def destination(request, tripid): 
	this_trip = Trip.objects.get(id=tripid)
	context = {
	"trip" : this_trip,
	"attendees" : this_trip.attendees.all()
	}
	return render(request, "travel_app/trip.html", context)