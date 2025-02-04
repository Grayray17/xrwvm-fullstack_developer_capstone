"""
Views for djangoapp.

This module contains user authentication and dealer review handling functions.
"""

import json
import logging
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

# Get an instance of a logger
logger = logging.getLogger(__name__)


@csrf_exempt
def login_user(request):
    """
    Handles user login requests.
    Accepts a JSON payload with 'userName' and 'password'.
    """
    if request.method != "POST":
        return JsonResponse({"error": "Only POST method is allowed"}, status=405)

    try:
        # Parse JSON data from request
        data = json.loads(request.body)
        username = data.get("userName", "").strip()
        password = data.get("password", "").strip()

        if not username or not password:
            return JsonResponse({"error": "Missing username or password"}, status=400)

        # Authenticate user
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return JsonResponse({"userName": username, "status": "Authenticated"}, status=200)

        return JsonResponse({"error": "Invalid username or password"}, status=401)

    except json.JSONDecodeError:
        logger.error("Invalid JSON received in login request")
        return JsonResponse({"error": "Invalid JSON format"}, status=400)

    except Exception as e:
        logger.error(f"Unexpected error during login: {str(e)}")
        return JsonResponse({"error": "An unexpected error occurred"}, status=500)


@csrf_exempt
def logout_user(request):
    """
    Handles user logout requests.
    Logs out the user and returns a JSON response.
    """
    if request.method != "POST":
        return JsonResponse({"error": "Only POST method is allowed"}, status=405)

    try:
        logout(request)
        return JsonResponse({"message": "Successfully logged out"}, status=200)

    except Exception as e:
        logger.error(f"Unexpected error during logout: {str(e)}")
        return JsonResponse({"error": "An unexpected error occurred during logout"}, status=500)


@csrf_exempt
def registration(request):
    """
    Handles user registration requests.
    Accepts a JSON payload with user details.
    """
    if request.method != "POST":
        return JsonResponse({"error": "Only POST method is allowed"}, status=405)

    try:
        # Parse JSON data from request
        data = json.loads(request.body)
        username = data.get("userName", "").strip()
        password = data.get("password", "").strip()
        first_name = data.get("firstName", "").strip()
        last_name = data.get("lastName", "").strip()
        email = data.get("email", "").strip()

        # Validate required fields
        if not username or not password or not email:
            return JsonResponse(
                {"error": "Missing required fields: username, password, and email are required"},
                status=400,
            )

        # Check if username or email already exists
        if User.objects.filter(username=username).exists():
            return JsonResponse({"error": "Username already taken"}, status=400)

        if User.objects.filter(email=email).exists():
            return JsonResponse({"error": "Email already registered"}, status=400)

        # Create a new user
        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
            email=email,
        )

        # Authenticate and log in the newly registered user
        login(request, user)
        return JsonResponse(
            {"userName": username, "status": "Registered and Logged In"},
            status=201,
        )

    except json.JSONDecodeError:
        logger.error("Invalid JSON received in registration request")
        return JsonResponse({"error": "Invalid JSON format"}, status=400)

    except Exception as e:
        logger.error(f"Unexpected error during registration: {str(e)}")
        return JsonResponse({"error": "An unexpected error occurred"}, status=500)


@csrf_exempt
def get_dealer_reviews(request, dealer_id):
    """
    Retrieves reviews for a specific dealer.
    """
    try:
        logger.info(f"Fetching reviews for dealer_id: {dealer_id}")

        # TODO: Replace with actual database query or API call
        reviews = [
            {"dealer_id": dealer_id, "review": "Great service!", "rating": 5, "customer": "John Doe"},
            {"dealer_id": dealer_id, "review": "Good prices!", "rating": 4, "customer": "Jane Smith"},
        ]

        if not reviews:
            logger.warning(f"No reviews found for dealer_id: {dealer_id}")
            return JsonResponse(
                {"dealer_id": dealer_id, "reviews": [], "message": "No reviews found"},
                status=404,
            )

        return JsonResponse({"dealer_id": dealer_id, "reviews": reviews}, status=200)

    except Exception as e:
        logger.error(f"Error retrieving reviews for dealer_id {dealer_id}: {str(e)}")
        return JsonResponse({"error": "An unexpected error occurred"}, status=500)


def dealer_list(request):
    """
    Retrieves and displays the list of dealers.
    """
    response = get_dealerships(request)
    data = json.loads(response.content)
    return render(request, "dealers.html", {"dealers": data["dealerships"]})
