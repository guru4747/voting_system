from django.db import models
from django.contrib.auth.models import User

class Voter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    has_voted = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Candidate(models.Model):
    name = models.CharField(max_length=100)
    party = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.party})"


class Election(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return self.name


class Vote(models.Model):
    voter = models.ForeignKey(Voter, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.voter.user.username} → {self.candidate.name}"
