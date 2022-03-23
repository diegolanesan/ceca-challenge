from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Car
from .serializers import CarSerializer


class CarViewSet(viewsets.ViewSet):
    def list(self, request):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        pass

    def retrieve(self, request, pk=None):
        car = Car.objects.get(id=pk)
        serializer = CarSerializer(car)
        return Response(serializer.data)

    def get_cars_by_plate(self, request, plate=None):
        cars = Car.objects.filter(plate=plate)
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)

    def update(self, request, pk=None):
        car = Car.objects.get(id=pk)
        serializer = CarSerializer(instance=car, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        car = Car.objects.get(id=pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
