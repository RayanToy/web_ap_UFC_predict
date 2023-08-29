from django.urls import path
from . import views
from .views import HomeView
from .views import TreeView
from .views import ForestView
from .views import knieghView
from .views import LDAView
urlpatterns = [
    path("", TreeView.as_view(), name='home'),
    path("about", HomeView.as_view(), name='about'),
    path("forest", ForestView.as_view(), name='forest'),
    path("kneigh", knieghView.as_view(), name='kneigh'),
    path("LDA", knieghView.as_view(), name='LDA'),
]
