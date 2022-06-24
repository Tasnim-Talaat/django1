from django.db.models import fields
from rest_framework import serializers
from .models import *


class Traineeserilizer(serializers.ModelSerializer):
    class Mete:
        model=Trainee
        fields='__all__'