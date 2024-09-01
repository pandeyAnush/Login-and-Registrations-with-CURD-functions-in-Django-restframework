from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authentication import TokenAuthentication

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cars
from .serializers import CarSerializer, CarListSerializer

class CarViewSet(APIView):
    def get(self, request):
        cars = Cars.objects.all()
        serializer = CarListSerializer(cars, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, car_id):
        try:
            car = Cars.objects.get(pk=car_id)
        except Cars.DoesNotExist:
            return Response({'error': 'Car not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, car_id):
        try:
            car = Cars.objects.get(pk=car_id)
        except Cars.DoesNotExist:
            return Response({'error': 'Car not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CarSerializer(car, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, car_id):
        try:
            car = Cars.objects.get(pk=car_id)
            car.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Cars.DoesNotExist:
            return Response({'error': 'Car not found'}, status=status.HTTP_404_NOT_FOUND)
























# class CarList(APIView):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]
#     permission_classes = [IsAuthenticated | IsAdminUser]
#     def get(self,request):

#         objs = Cars.objects.all()
#         if objs:
#             return Response({
#                 "error": False,
#                 "data": CarListSerializer(objs, many=True, context={'request': request}).data,
#                 "status": status.HTTP_200_OK
#             }, status=status.HTTP_200_OK)
#         else:
#             return Response({
#                 "error": False,
#                 "data": "Car list not found.",
#                 "status": status.HTTP_204_NO_CONTENT
#             }, status=status.HTTP_204_NO_CONTENT)

    
#     def get(self, request):
#         obje = Cars.objects.all()
#         serializer = CarListSerializer(obje, many = True).data
#         return Response({'status': 200, 'payload': serializer})
            
#     def post(self, request):
#         serializer = CarSerializer(data = request.data)
#         if not serializer.is_valid():
#             print(serializer.errors)
#             return Response({'status': 403, 'errors': serializer.errors, 'message': 'Wrong data!'})
#         serializer.save()
#         return Response({'status': 200, 'payload': serializer.data, 'message': 'your data is saved!'})

#     def put(self, request):
#         try:
#             car_obj = Cars.objects.get(id = request.data['id'])
#             serializer = CarSerializer(car_obj, data = request.data, partial = False)
#             if not serializer.is_valid():
#                 print(serializer.errors)
#                 return Response({'status': 403, 'errors': serializer.errors, 'message': 'Something is Wrong in your data!'})
#             serializer.save()
#             return Response({'status': 403, 'message': 'Your data is Updated!!'})
#         except Exception as e:
#             print(e)
#             return Response({'status': 403, 'message': 'Invalid data'})

#     def patch(self, request):
#         try:
#             car_obj = Cars.objects.get(id = request.data['id'])
#             serializer = CarSerializer(car_obj, data = request.data, partial = True)
#             if not serializer.is_valid():
#                 print(serializer.errors)
#                 return Response({'status': 403, 'errors': serializer.errors, 'message': 'Something is Wrong in your data!'})
#             serializer.save()
#             return Response({'status': 403, 'message': 'Your data is Updated!!'})
#         except Exception as e:
#             print(e)
#             return Response({'status': 403, 'message': 'Invalid data'})

#     def delete(self, request):
#         try:
#             id = request.GET.get('id')
#             car_obj = Cars.objects.get(id = id)
#             car_obj.delete()
#             return Response({'status':403, 'message': 'Data Has Been Deleted Sucessfully'})
#         except Exception as e:
#             return Response({'status':403, 'message': 'Invalid data'})
