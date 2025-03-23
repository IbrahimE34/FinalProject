from rest_framework import serializers

from app.models import Category, Car


class CategorySerializers(serializers. ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'full_name']

class CarSerializers(serializers.ModelSerializer):
    discount_price = serializers.IntegerField(read_only= True)

    class Meta:
        model = Car
        fields = "__all__"

