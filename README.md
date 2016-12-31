# DRF-Base64

**DRF-Base64** provides a set of serializers to handle Bas64-encoded files.

## Installation

**DRF-Base64** is compatible with python 2.7 and 3.4+ as well as Django 1.8+ and DRF 3.3+

### With pip

`pip install drf-base64`

### From source

Within the source directory:

`python setup.py install`

## Field Serializers

**DRF-Base64** provides a `Base64FileField` and a `Base64ImageField` very similar
to DRF's `FileField` and `ImageField` with the added functionality of accepting
base64-encoded file strings as input.
If those serialiers receive an url (ie: when updating a record containing a file without
modifying that said file), it will leave the existing value untouched.

Example usage:

```
from rest_framework import serializers
from base64.fields import Base64ImageField

from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    picture = Base64ImageField(required=False)

    class Meta:
        model = Product
...

```

## Model Serializers

**DRF-Base64** also provides a `ModelSerializer` and an `HyperlinkedModelSerializer`
also similar to DRF's own `ModelSerializer` and `HyperlinkedModelSerializer` with the
added functionality of mapping `django.db.models.FileField`'s to `Bas64FileField`'s and
`django.db.models.ImageField`'s to `Base64ImageField`'s.

Example usage:

```
from drf_base64.serializers import ModelSerializer

from .models import Product


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
...

```

## Mixins

### `drf_base64.fields.Base64FieldMixin`

If you'd like to enable base64 uploading of file for other field types than `FileField` or
`ImageField`, **DRF-Base64** provides `Base64FieldMixin` to let you do just that.

### `drf_base64.serializers.Base64ModelSerializerMixin`

If you wish to use `Base64FileField` and `Base64ImageField` as default for model serializers
other than the ones provided, **DRF-Base64** also provides `Base64ModelSerializerMixin`
that you can apply on any other model serializer as long as they use
[`serializer_field_mapping`](http://www.django-rest-framework.org/api-guide/serializers/#serializer_field_mapping).

---

License information available [here](LICENSE.md).

Contributors code of conduct is available [here](COC.md). Note that this COC **will** be enforced.
