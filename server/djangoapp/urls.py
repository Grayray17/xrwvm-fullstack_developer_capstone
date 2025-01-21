from django.views.generic import TemplateView
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'

urlpatterns = [
    # Path for registration view (to be implemented later)
    # path('register/', views.registration, name='register'),

    # Path for login view
    path('login/', views.login_user, name='login'),
    path('login/', TemplateView.as_view(template_name="index.html")),

    #path for logout view
    path('logout/', views.logout_user, name='logout'),  # Add this line
    path('logout/', TemplateView.as_view(template_name="index.html")),

    #Path for registration
      path('registration/', views.registration, name='registration'),
      #path('register_user/', registration, name='register_user'),

    # Path for dealer reviews view (to be implemented later)
    # path('reviews/<int:dealer_id>/', views.get_dealer_reviews, name='dealer_reviews'),

    # Path for adding a review view (to be implemented later)
    # path('add_review/', views.add_review, name='add_review'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
