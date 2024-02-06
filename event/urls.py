from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from event import views

urlpatterns = [
    path('v1/event/', views.EventList.as_view()),
    path('v1/event/<int:pk>/', views.EventDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)