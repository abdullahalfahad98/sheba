
from rest_framework import serializers
from event.models import Event
from django.utils import timezone
from .models import Donation

class EventSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Event
        fields = ['id', 'title', 'image', 'description', 'created_date', 'event_date']
        read_only_fields = ['created_date']

    def validate_event_date(self, value):
        if value < timezone.now().date():
            raise serializers.ValidationError("Event date cannot be in the past.")
        return value

    def create(self, validated_data):
        return Event.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.image = validated_data.get('image', instance.image)
        instance.description = validated_data.get('description', instance.description)
        instance.event_date = validated_data.get('event_date', instance.event_date)
        instance.save()
        return instance
    

  
class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = '__all__'

        def update(self, instance, validated_data):
            instance.full_name = validated_data.get('full_name', instance.full_name)
            instance.amount = validated_data.get('amount', instance.amount)
            instance.purpose = validated_data.get('purpose', instance.purpose)
            instance.note = validated_data.get('note', instance.note)
            instance.save()
            return instance
