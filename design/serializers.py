from rest_framework import serializers
from .models import Candidate, Vote

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ["id", "name", "party"]

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ["id", "candidate", "voter"]
