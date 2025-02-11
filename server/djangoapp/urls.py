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

    # Path for retrieving dealers (Corrected)
    path("get_dealers/", views.get_dealerships, name="get_dealers"),

    # Path for retrieving dealers by state (Optional: dynamic state filter)
    path("get_dealers/<str:state>/", views.get_dealerships_by_state, name="get_dealers_by_state"),

    # Path for retrieving dealer reviews
    path("get_dealers_reviews/", views.get_dealer_reviews, name="get_dealers_reviews"),

    # Path for adding a review (Uncomment when implemented)
    # path("add_review/", views.add_review, name="add_review"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
