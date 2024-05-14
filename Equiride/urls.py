from django.urls import path
from .views import Index


urlpatterns = [
    path('', Index.as_views(), name='Equiride')
]