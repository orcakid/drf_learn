from django.urls import path
from .views import PersApiViews

urlpatterns = [
    path('champs/', PersApiViews.as_view()), 
    path('champs/<int:pk>/',PersApiViews.as_view()),
    path('champs_del/<int:pk>/',PersApiViews.as_view()),
]
