from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class People(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="peoples", null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
