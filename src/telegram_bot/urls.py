from django.urls import path

from .views import UpdateHandler


urlpatterns = [
    path('', UpdateHandler.as_view(), name='update_handler_url')
]
