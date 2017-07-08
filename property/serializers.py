from rest_framework import serializers

from .models import Property


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ('title', 'name', 'city', 'state', 'id_json', 'purpose', 'listing_type', 'published_on')
