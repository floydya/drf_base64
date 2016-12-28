from django.db import models

from rest_framework.serializers import (ModelSerializer as DRFModelSerializer,
                                        HyperlinkedModelSerializer as DRFHyperlinkedModelSerializer)

from .fields import Base64FileField, Base64ImageField


ms_field_mapping = DRFModelSerializer.serializer_field_mapping
ms_field_mapping.update({
    models.FileField: Base64FileField,
    models.ImageField: Base64ImageField,
})


# class Base64ModelSerializerMixin(object):


class ModelSerializer(DRFModelSerializer):
    field_mapping = ms_field_mapping


# class HyperlinkedModelSerializer(Base64ModelSerializerMixin, DRFHyperlinkedModelSerializer):
#     pass
