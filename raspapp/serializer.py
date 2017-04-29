from rest_framework import serializers


class StatusSerializer(serializers.Serializer):

    type = serializers.CharField(max_length=10)
    amount = serializers.IntegerField()
