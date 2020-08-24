from django.urls import path
from .views import ChannelView


urlpatterns = [
    path('setupchannel/', ChannelView.as_view({'put':'update'})),
]