from rest_framework import serializers

from models import Team, People


class TeamSerializer(serializers.ModelSerializer):
    peoples = serializers.SerializerMethodField(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ("id", "name", "peoples")


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ("id", "first_name", "last name", "email", "team")
