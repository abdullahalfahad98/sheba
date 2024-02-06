from rest_framework import serializers
from event.models import Event
from django.utils import timezone

class EventSerializers(serializers.Serializer):
    
    title = serializers.CharField(max_length=255)
    image = serializers.ImageField(required=False)  
    description = serializers.CharField() 
    created_date = serializers.DateField(read_only=True)
    event_date = serializers.DateField()


    def create(self, validated_data):
        # Set the created_date when creating a new instance
        validated_data['created_date'] = timezone.now().date()
        
        # Custom handling of file upload path
        image = validated_data.pop('image')
        event = Event.objects.create(image=image, **validated_data)
        return event