from tastypie.resources import ModelResource
from .models import Operations


class OperationsResource(ModelResource):
    class Meta:
        queryset = Operations.objects.all()
        resource_name = 'operations'