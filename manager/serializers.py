from rest_framework import serializers

from manager.models import Team, Person


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ("id", "name")


class TeamListSerializer(TeamSerializer):
    persons = serializers.SlugRelatedField(
        many=True, slug_field="full_name", read_only=True
    )

    class Meta:
        model = Team
        fields = ("id", "name", "persons")


class PersonSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True)
    class Meta:
        model = Person
        fields = ("id", "first_name", "last_name", "email", "team")
