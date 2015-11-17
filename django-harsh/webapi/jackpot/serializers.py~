from rest_framework import serializers
from jackpot.models import Bowler


class BowlerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=False, allow_blank=True, max_length=200)
    #email = serializers.EmailField(max_length=200)
    created = serializers.DateTimeField()
    #password = serializers.CharField(max_length=6)
    amount = serializers.IntegerField(default=1000)

    

    def create(self, validated_data):
        """
        Create and return a new `Bowler` instance, given the validated data.
        """
        return Bowler.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Bowler` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        #instance.email = validated_data.get('email', instance.email)
        #instance.password = validated_data.get('password', instance.password)
        instance.amount = validated_data.get('amount', instance.amount)
        
        instance.save()
        return instance
