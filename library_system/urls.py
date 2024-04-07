# We import the necessary libraries
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from library_system import views

# We create an instance of the default Django REST Framework router.
router = routers.DefaultRouter()

# We register our views with the router.
# Each view is associated with a specific endpoint
router.register(r'books', views.BookViewSet, basename='book')  # Endpoint for books
router.register(r'users', views.UserViewSet, basename='user')  # Endpoint for users
router.register(r'loans', views.LoanViewSet, basename='loan')  # Endpoint for loans

# Define our URL routes
# We include the router's routes in our list of routes
urlpatterns = [
    path('api/v1/', include(router.urls)),  # All endpoints will be under 'api/v1/'.
    path("docs/", include_docs_urls(title="Library API")), # Include the coreapi urls for documentation
]
