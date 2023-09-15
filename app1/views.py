from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Userdata
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from django.http import JsonResponse

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        # pdb.set_trace()
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    def post(self, request):
        serializers = UserLoginSerializer(data=request.data)
        if serializers.is_valid():
            try:
                user = Userdata.objects.get(email=serializers.validated_data["email"],password=serializers.validated_data['password'])
                if user: 
                    return Response({"msg":"Login Successfull"},status=status.HTTP_200_OK)
                
            except :
                return Response({"msg":"Enter Email & Password Invalid","->":serializers.errors},status=status.HTTP_401_UNAUTHORIZED)

        return Response({"msg":serializers.errors}, status=status.HTTP_400_BAD_REQUEST)


class AllUserDetailsView(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user=Userdata.objects.all()
        userdisp=UserProfileSerializer(user,many=True)
        return JsonResponse(userdisp.data,safe=False)


class UserlistDetailsView(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request,format=None):
            serializers = UserfilterSerializer(data=request.data)
            try:
                user = Userdata.objects.filter(user=serializers.validated_data["full_name"])
                print(user)
                serializers = UserRegistrationSerializer(user,many=True)
                return Response({"success": True,"posts of":serializers.data })
            except :
                return Response({'Message':"not found"},status=status.HTTP_400_BAD_REQUEST)
            
from rest_framework import generics
from rest_framework import permissions

class UserListView(generics.ListAPIView):
    authentication_classes=[JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Userdata.objects.all()
    serializer_class = UserRegistrationSerializer

    def get_queryset(self):
        queryset = Userdata.objects.all()
        name = self.request.query_params.get('full_name', None)
        if name is not None:
            queryset = queryset.filter(full_name__icontains=name)
            return JsonResponse(queryset.data,safe=False)
        return queryset