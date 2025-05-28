from rest_framework import serializers
from ..models import JobOffer, Technology


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ['name']

class JobOfferSerializer(serializers.ModelSerializer):
    technologies = TechnologySerializer(many=True)
    created_at = serializers.DateTimeField(format="%d-%m-%Y")
    class Meta:
        model = JobOffer
        fields = "__all__"