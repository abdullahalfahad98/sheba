from event.models import Event
from event.serializers import EventSerializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly


class EventList(APIView):
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]  # Add this line

    def get_queryset(self):
        return Event.objects.all()
    """
    List all events, or create a new event.
    """
    def get(self, request, format=None):
        event = Event.objects.all()
        serializer = EventSerializers(event, many=True)
        return Response(serializer.data)

    # def post(self, request, format=None):
    #     serializer = EventSerializers(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class EventDetail(APIView):

    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]  # Add this line
    def get_queryset(self):
        return Event.objects.all()
    """
    Retrieve, update  a event instance.
    """
    def get_object(self, pk):
        try:
            return Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        event = self.get_object(pk)
        serializer = EventSerializers(event)
        return Response(serializer.data)

  

    # def put(self, request, pk, format=None):
    #     event = self.get_object(pk)
    #     serializer = EventSerializers(event, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    
