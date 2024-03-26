from rest_framework import serializers
from .models import Location, Venue, Event

class EventSerializer(serializers.HyperlinkedModelSerializer):
    venue = serializers.PrimaryKeyRelatedField(
        queryset = Venue.objects.all(),
        source = 'venue_id'
    )

    event_url = serializers.ModelSerializer.serializer_url_field(
      view_name = 'event_detail',
    )

    class Meta:
        model = Event
        fields = ('id', 'venue', 'name', 'event_type', 'date', 'seating_type', 'cost', 'event_img', 'event_url')

class VenueSerializer(serializers.HyperlinkedModelSerializer):
    event = EventSerializer(
        many = True,
        read_only = True
    )

    city = serializers.ReadOnlyField(source='location.city')
    state = serializers.ReadOnlyField(source='location.state')

    location_url = serializers.HyperlinkedRelatedField(
       view_name = 'location_detail',
       source = 'locations',
       read_only = True
    )

    class Meta:
        model = Venue
        fields = ('id', 'city', 'state', 'location_url', 'name', 'venue_img', 'event')

class LocationSerializer(serializers.ModelSerializer):
  venues = VenueSerializer(
    many = True,
    read_only = True
  )
  
  class Meta:
    model = Location
    fields = ('id', 'state', 'city', 'city_img', 'venues')


