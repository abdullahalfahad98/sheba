# from django.urls import path

# from . import views

# urlpatterns = [
#     path("", views.index, name="index"),
# ]


from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from event import views

urlpatterns = [
    path('', views.EventList.as_view()),
    # path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)