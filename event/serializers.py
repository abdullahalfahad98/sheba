# from rest_framework import serializers
# from event.models import Event
# from django.utils import timezone

# class EventSerializers(serializers.Serializer):
    
#     title = serializers.CharField(max_length=255)
#     image = serializers.ImageField(required=False)  
#     description = serializers.CharField() 
#     created_date = serializers.DateField(read_only=True)
#     event_date = serializers.DateField()


#     def create(self, validated_data):
#         # Set the created_date when creating a new instance
#         validated_data['created_date'] = timezone.now().date()
        
#         # Custom handling of file upload path
#         image = validated_data.pop('image')
#         event = Event.objects.create(image=image, **validated_data)
#         return event



from rest_framework import serializers
from event.models import Event
from django.utils import timezone

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
