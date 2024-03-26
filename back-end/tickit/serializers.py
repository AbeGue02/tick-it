from rest_framework import serializers
from .models import Location, Venue, Event

class EventSerializer(serializers.HyperlinkedModelSerializer):
    venue = serializers.HyperlinkedRelatedField(
        view_name='venue_detail',
        many=False,
        read_only=True
    )

    class Meta:
        model = Event
        fields = ('venue', 'name', 'event_type', 'date', 'seating_type', 'cost', 'event_img')

class VenueSerializer(serializers.HyperlinkedModelSerializer):
    events = serializers.HyperlinkedRelatedField(
        view_name='event-detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Venue
        fields = ('location', 'name', 'venue_img', 'events')

class LocationSerializer(serializers.ModelSerializer):
  venues = VenueSerializer(
    many=True,
    read_only=True
  )
  
  class Meta:
    model = Location
    fields = ('state', 'city', 'city_img', 'venues')


