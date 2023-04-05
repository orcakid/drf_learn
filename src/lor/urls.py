from django.urls import path
from .views import PersApiViews

urlpatterns = [
    path('mf/', PersApiViews.as_view())
]
