from rest_framework import serializers
from .models import Location, Venue, Event

class EventSerializer(serializers.HyperlinkedModelSerializer):
    venue = serializers.PrimaryKeyRelatedField(
        queryset = Venue.objects.all(),
        source = 'venue_id'
    )
    venue_name = serializers.ReadOnlyField(source='venue.name')
    event_city = serializers.ReadOnlyField(source='venue.location.city')
    event_state = serializers.ReadOnlyField(source='venue.location.state')

    event_url = serializers.ModelSerializer.serializer_url_field(
      view_name = 'event_detail',
    )

    class Meta:
        model = Event
        fields = ('id', 'venue', 'venue_name', 'event_city', 'event_state', 'name', 'event_type', 'date', 'seating_type', 'cost', 'event_img', 'event_url')

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


