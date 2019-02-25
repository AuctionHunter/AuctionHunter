from rest_framework import routers, serializers, viewsets
from pymongo.collection import ObjectId

from .models import Vehicles


class ObjectIdField(serializers.Field):
    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return ObjectId(data)


class VehicleSerializer(serializers.ModelSerializer):
    _id = ObjectIdField()

    class Meta:
        model = Vehicles
        fields = '__all__'


class VehicleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Vehicles.objects.all()
    serializer_class = VehicleSerializer


router = routers.DefaultRouter()
router.register(r'vehicles', VehicleViewSet)
