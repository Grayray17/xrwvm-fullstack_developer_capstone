"""
djangoapp URL Configuration

Defines URL patterns for the djangoapp application.
"""

from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from djangoapp import views

app_name = "djangoapp"

urlpatterns = [
    # Path for registration view
    path("register/", views.registration, name="register"),

    # Path for login view
    path("login/", views.login_user, name="login"),

    # Path for logout view
    path("logout/", views.logout_user, name="logout"),

    # Path for dealer reviews view
    path("get_dealers_reviews/", views.get_dealer_reviews, name="get_dealers_reviews"),

    # Path for adding a review view (to be implemented later)
    # path("add_review/", views.add_review, name="add_review"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
