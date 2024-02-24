from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path("envelopes/", views.EnvelopeList.as_view()),
    path("envelopes/<int:pk>/", views.EnvelopeDetail.as_view()),
    path("transactions/", views.TransactionList.as_view()),
    path("transactions/<int:pk>/", views.TransactionDetail.as_view()),
    path("fills/", views.FillList.as_view()),
    path("fills/<int:pk>/", views.FillDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
