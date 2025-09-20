from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework import status
from django.conf import settings
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView, TokenVerifyView
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import FilesSerializer
import json
from rest_framework import generics
from rest_framework import status, permissions
from django.db.models import Q
from .models import Files


@api_view(['GET'])
def display(request):

    routes = [
        'MY FIRST REST RESPONSE ON DJANGO'
    ]

    return Response(routes)

##Can add the JWT authenticaton views from bryan kirch auth video if needed.


class FileUploadView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        print("Recieved_data:", request.data)
        file_serializer = FilesSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save(user=request.user)
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)

        return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
