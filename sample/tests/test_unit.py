import base64

from unittest import TestCase

from django.core.files.base import ContentFile
from django.db import models
from rest_framework.fields import SkipField

from drf_base64.fields import Base64FieldMixin, Base64FileField, Base64ImageField


from ..serializers import FileModelSerializer


class FieldTestCase(TestCase):

    def setUp(self):
        self.field_serializer = Base64FieldMixin()

    def test_decode(self):
        orig = 'brol'
        extension = 'txt'
        py2 = True
        try:
            test_str = 'data:text/{};base64,{}'.format(extension, base64.b64encode(orig))
        except TypeError:
            py2 = False
            orig = b'brol'
            test_str = 'data:text/{};base64,{}'.format(extension, base64.b64encode(orig))

        output = self.field_serializer._decode(test_str)
        self.assertTrue(isinstance(output, ContentFile))
        if py2:
            self.assertEqual(output.read(), orig)
        self.assertEqual(output.name.split('.')[-1], extension)

    def test_skip_url(self):
        test_str = 'http://levit.be'

        with self.assertRaises(SkipField):
            self.field_serializer._decode(test_str)


class SerializerTestCase(TestCase):

    def setUp(self):
        self.serializer = FileModelSerializer()

    def test_fields(self):
        self.assertTrue(isinstance(self.serializer.fields['file'], Base64FileField))
        self.assertTrue(isinstance(self.serializer.fields['image'], Base64ImageField))
