from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.db.models import Count
from .models import Voter, Candidate, Vote

# --- Signup ---
def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Voter.objects.create(user=user)  # create voter profile
            login(request, user)
            return redirect("profile")
    else:
        form = UserCreationForm()
    return render(request, "design/signup.html", {"form": form})

# --- Login ---
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("profile")
    else:
        form = AuthenticationForm()
    return render(request, "design/login.html", {"form": form})

# --- Logout ---
def logout_view(request):
    logout(request)
    return redirect("login")

# --- Profile ---
@login_required
def profile_view(request):
    voter = get_object_or_404(Voter, user=request.user)
    return render(request, "design/profile.html", {"voter": voter})

# --- Candidate List ---
@login_required
def candidate_list(request):
    candidates = Candidate.objects.all()
    return render(request, "design/candidate_list.html", {"candidates": candidates})

# --- Cast Vote ---
@login_required
def cast_vote(request, candidate_id):
    candidate = get_object_or_404(Candidate, id=candidate_id)
    voter = get_object_or_404(Voter, user=request.user)

    if voter.has_voted or Vote.objects.filter(voter=voter).exists():
        messages.error(request, "❌ You have already voted!")
        return redirect("candidate_list")

    if request.method == "POST":
        Vote.objects.create(voter=voter, candidate=candidate)
        voter.has_voted = True
        voter.save()
        messages.success(request, f"✅ You voted for {candidate.name}!")
        return redirect("result_page")   # ✅ fixed name

    return render(request, "design/vote_confirm.html", {"candidate": candidate})

# --- Results ---
@login_required
def result_page(request):
    candidates = Candidate.objects.annotate(vote_count=Count("votes"))
    return render(request, "design/results.html", {"candidates": candidates})

# --- Homepage ---
def homepage(request):
    return render(request, "design/homepage.html")
