from rest_framework import viewsets

from manager.models import Team, Person
from manager.serializers import TeamListSerializer, PersonSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.prefetch_related("persons")
    serializer_class = TeamListSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.select_related("team")
    serializer_class = PersonSerializer
