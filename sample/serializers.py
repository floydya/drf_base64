from drf_base64.serializers import ModelSerializer

from .models import FileModel


class FileModelSerializer(ModelSerializer):

    class Meta:
        model = FileModel
        fields = (
            'id',
            'file',
            'image',
        )
