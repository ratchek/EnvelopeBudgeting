from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

urlpatterns = [
    path("envelopes/", views.EnvelopeList.as_view(), name="envelope-list"),
    path("envelopes/<int:pk>/", views.EnvelopeDetail.as_view(), name="envelope-detail"),
    path("transactions/", views.TransactionList.as_view(), name="transaction-list"),
    path(
        "transactions/<int:pk>/",
        views.TransactionDetail.as_view(),
        name="transaction-detail",
    ),
    path("fills/", views.FillList.as_view(), name="fill-list"),
    path("fills/<int:pk>/", views.FillDetail.as_view(), name="fill-detail"),
    path("", views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)

# JWT token authentication
urlpatterns += [
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
