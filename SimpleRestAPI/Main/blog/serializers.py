from rest_framework import serializers
from .models import DataModel

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataModel
        fields = [
            "id",
            "name",
            "age",
            "gender",
            "id_card_number",
            "address",
            "is_married",
            "created",
            "updated"
        ]