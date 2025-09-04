from django.contrib import admin
from django.urls import path
from design import views   

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("signup/", views.signup_view, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("profile/", views.profile_view, name="profile"),
    path("candidates/", views.candidate_list, name="candidate_list"),   
    path("vote/<int:candidate_id>/", views.cast_vote, name="cast_vote"),
    path("results/", views.result_page, name="results"),
]
