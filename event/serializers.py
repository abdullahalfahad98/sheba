from rest_framework import serializers
from event.models import Event


class EventSerializers(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    image = serializers.ImageField(upload_to='event/images/')  # You may specify the upload_to path as per your requirement
    description = serializers.TextField()
    created_date = serializers.DateField(auto_now_add=True)
    event_date = serializers.DateField()

