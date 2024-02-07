from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
from event.views import EventList, EventDetail
from rest_framework.authtoken import views

urlpatterns = [
    path('v1/event/', EventList.as_view(),name="user-list"),
    path('v1/event/<int:pk>/', EventDetail.as_view()),
    path('api-token-auth/', views.obtain_auth_token),
]

# urlpatterns = format_suffix_patterns(urlpatterns)