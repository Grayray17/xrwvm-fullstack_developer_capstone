from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import json
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

@csrf_exempt
def login_user(request):
    """
    Handles user login requests. Accepts a JSON payload with 'userName' and 'password'.
    """
    if request.method == 'POST':
        try:
            # Parse JSON data from the request body
            data = json.loads(request.body)
            username = data.get('userName')
            password = data.get('password')

            # Validate input
            if not username or not password:
                return JsonResponse({"error": "Missing username or password"}, status=400)

            # Authenticate user
            user = authenticate(username=username, password=password)
            if user is not None:
                # Log in the user
                login(request, user)
                response_data = {"userName": username, "status": "Authenticated"}
                return JsonResponse(response_data, status=200)
            else:
                return JsonResponse({"error": "Invalid credentials"}, status=401)
        except json.JSONDecodeError:
            logger.error("Invalid JSON received in login request")
            return JsonResponse({"error": "Invalid JSON format"}, status=400)
        except Exception as e:
            logger.error(f"An error occurred: {str(e)}")
            return JsonResponse({"error": "An unexpected error occurred"}, status=500)
    else:
        return JsonResponse({"error": "Only POST method is allowed"}, status=405)

@csrf_exempt
def logout_user(request):
    """
    Handles user logout requests. Logs out the user and returns a JSON response.
    """
    if request.method == 'POST':
        try:
            # Log out the user
            logout(request)
            response_data = {"userName": ""}
            return JsonResponse(response_data, status=200)
        except Exception as e:
            logger.error(f"An error occurred during logout: {str(e)}")
            return JsonResponse({"error": "An unexpected error occurred during logout"}, status=500)
    else:
        return JsonResponse({"error": "Only POST method is allowed"}, status=405)

@csrf_exempt
def registration(request):
    """
    Handles user registration requests. Accepts a JSON payload with user details.
    """
    if request.method == 'POST':
        try:
            # Parse JSON data from the request body
            data = json.loads(request.body)
            username = data.get('userName')
            password = data.get('password')
            first_name = data.get('firstName')
            last_name = data.get('lastName')
            email = data.get('email')

            # Validate the input
            if not username or not password or not email:
                return JsonResponse({"error": "Missing required fields"}, status=400)

            # Check if username or email already exists
            if User.objects.filter(username=username).exists():
                return JsonResponse({"error": "Username already exists"}, status=400)
            if User.objects.filter(email=email).exists():
                return JsonResponse({"error": "Email already exists"}, status=400)

            # Create a new user
            user = User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                password=password,
                email=email,
            )

            # Authenticate and log in the newly registered user
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({"userName": username, "status": "Registered and Logged In"}, status=201)
            else:
                return JsonResponse({"error": "Authentication failed after registration"}, status=500)
        except json.JSONDecodeError:
            logger.error("Invalid JSON received in registration request")
            return JsonResponse({"error": "Invalid JSON format"}, status=400)
        except Exception as e:
            logger.error(f"An error occurred during registration: {str(e)}")
            return JsonResponse({"error": "An unexpected error occurred"}, status=500)
    else:
        return JsonResponse({"error": "Only POST method is allowed"}, status=405)
