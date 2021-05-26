from django.db import models
from django.db.models import fields
from rest_framework import serializers

from todos.models import Todo

class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'