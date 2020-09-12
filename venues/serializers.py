from rest_framework import serializers
from .models import Venue


class VenueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Venue
        fields = [
            "name",
            "slug",
            "date_modified",
            "website",
            "calendar_url",
            "facebook",
            "twitter",
            "instagram",
            "phone",
            "email",
            "description",
            "address_street",
            "address_city",
            "address_full",
        ]
