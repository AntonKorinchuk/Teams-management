from rest_framework import serializers

from manager.models import Team, People


class TeamSerializer(serializers.ModelSerializer):
    peoples = serializers.SlugRelatedField(many=True, read_only=True, slug_field="full_name")

    class Meta:
        model = Team
        fields = ("id", "name", "peoples")


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ("id", "first_name", "last name", "email", "team")
