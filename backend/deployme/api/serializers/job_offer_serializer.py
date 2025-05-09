from rest_framework import serializers
from jobs.models import JobOffer

class JobOfferSerializer(serializers.ModelSerializers):
    class Meta:
        job_offer = JobOffer
        fields = "__all__"