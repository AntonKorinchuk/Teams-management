from rest_framework import viewsets

from manager.models import Team, People
from manager.serializers import TeamSerializer, PeopleSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.prefetch_related("peoples")
    serializer_class = TeamSerializer


class PeopleViewSet(viewsets.ModelViewSet):
    queryset = People.objects.select_related("team")
    serializer_class = PeopleSerializer
