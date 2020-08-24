from rest_framework import viewsets, status
from .serializers import ChannelSerializer
from rest_framework.response import Response


class ChannelView(viewsets.ViewSet):
    """
    Create the view for each of the components of the Channel model
    """

    def put(self, request, pk):
        channel = self.get_object(pk)
        if channel == 'phone_number':  # What exactly does this line do?
            serializer = ChannelSerializer(channel, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
