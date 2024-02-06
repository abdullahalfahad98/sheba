# from django.shortcuts import render

# # Create your views here.
# from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")


from event.models import Event
from event.serializers import EventSerializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly


class EventList(APIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]  # Add this line

    def get_queryset(self):
        return Event.objects.all()
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        event = Event.objects.all()
        serializer = EventSerializers(event, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EventSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)