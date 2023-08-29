from django.urls import path
from . import views
from .views import HomeView
urlpatterns = [
    path("", views.form, name='form'),
    path("predict", HomeView.as_view(), name='predict'),
]
