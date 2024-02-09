from django.urls import path,include
# from rest_framework.urlpatterns import format_suffix_patterns
from event.views import EventList, EventDetail, EventDonation,DonationDetail,GetRoutes
from rest_framework.authtoken import views

urlpatterns = [
    path('', GetRoutes.as_view()),
    path('v1/event/', EventList.as_view(),name="user-list"),
    path('v1/event/<int:pk>/', EventDetail.as_view()),
    path('v1/donate/', EventDonation.as_view()),
    path('v1/donate/<int:pk>/', DonationDetail.as_view()),
    path('api-token-auth/', views.obtain_auth_token),
    
]

# urlpatterns = format_suffix_patterns(urlpatterns)