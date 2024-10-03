from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from manager.models import Team, Person


class TeamAPITestCase(APITestCase):

    def setUp(self):
        self.team = Team.objects.create(name="Test Team")
        self.person = Person.objects.create(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            team=self.team,
        )

    def test_create_team(self):
        url = reverse("manager:team-list")
        data = {"name": "New Team"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Team.objects.count(), 2)
        self.assertEqual(Team.objects.get(id=2).name, "New Team")

    def test_get_team_list(self):
        url = reverse("manager:team-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_team_detail(self):
        url = reverse("manager:team-detail", kwargs={"pk": self.team.id})
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Test Team")

    def test_update_team(self):
        url = reverse("manager:team-detail", kwargs={"pk": self.team.id})
        data = {"name": "Updated Team"}
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.team.refresh_from_db()
        self.assertEqual(self.team.name, "Updated Team")

    def test_delete_team(self):
        url = reverse("manager:team-detail", kwargs={"pk": self.team.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Team.objects.count(), 0)


class PersonAPITestCase(APITestCase):

    def setUp(self):
        self.team = Team.objects.create(name="Test Team")
        self.person = Person.objects.create(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            team=self.team,
        )

    def test_create_person(self):
        url = reverse("manager:person-list")
        data = {
            "first_name": "Jane",
            "last_name": "Smith",
            "email": "jane.smith@example.com",
            "team": self.team.id,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Person.objects.count(), 2)
        self.assertEqual(Person.objects.get(id=2).first_name, "Jane")

    def test_get_person_list(self):
        url = reverse("manager:person-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_person_detail(self):
        url = reverse("manager:person-detail", kwargs={"pk": self.person.id})
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["first_name"], "John")

    def test_update_person(self):
        url = reverse("manager:person-detail", kwargs={"pk": self.person.id})
        data = {
            "first_name": "Updated",
            "last_name": "Name",
            "email": "john.doe@example.com",
            "team": self.team.id,
        }
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.person.refresh_from_db()
        self.assertEqual(self.person.first_name, "Updated")
        self.assertEqual(self.person.last_name, "Name")

    def test_delete_person(self):
        url = reverse("manager:person-detail", kwargs={"pk": self.person.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Person.objects.count(), 0)
