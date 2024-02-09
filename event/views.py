from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from event.models import Event
from .serializers import EventSerializer
from django.http import Http404
# from rest_framework.authtoken.models import Token
from .models import Donation
from .serializers import DonationSerializer

# for token authentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication



class GetRoutes(APIView):
    def get(self, request, format=None):
        routes = [
            'GET /api/v1/event/',
            'GET /api/v1/event/:id/',
            'GET /api/v1/donate/',
            'GET /api/v1/donate/:id/',
            'GET /api-token-auth/',
        ]
        context = {
            'routes': routes
        }
        return Response(context)

class EventList(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    """
    List all events or create a new event.
    """
    def get(self, request, format=None):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token_obj, created = Token.objects.get_or_create(user=user)
            if created:
                return Response({'user':serializer.data, 'token': token_obj.key}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventDetail(APIView):
    """
    Retrieve, update or delete an event instance.
    """
    def get_object(self, pk):
        try:
            return Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        event = self.get_object(pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        event = self.get_object(pk)
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        event = self.get_object(pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class EventDonation(APIView):
    def get(self, request):
        donations = Donation.objects.all()
        serializer = DonationSerializer(donations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DonationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DonationDetail(APIView):
    def get_object(self, pk):
        try:
            return Donation.objects.get(pk=pk)
        except Donation.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        donation = self.get_object(pk)
        serializer = DonationSerializer(donation)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        donation = self.get_object(pk)
        serializer = DonationSerializer(donation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        donation = self.get_object(pk)
        donation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)