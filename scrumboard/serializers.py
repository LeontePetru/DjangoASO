from rest_framwork import serializers
from scrumboard.model import List,Card

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model= Card
        fields = '__all__'

class ListSerializer(serializers.modelSerializer):
    cards=CardSerializer(read_only=True, many=True)

    class Meta:
        model =List
        fields = '__all__'