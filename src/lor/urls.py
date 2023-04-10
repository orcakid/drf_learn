from django.urls import path
from .views import PersUpdateAPI, PersListCreateAPI, PersCRUDapi, PersViewSet



urlpatterns = [
    # path('champs/', PersListCreateAPI.as_view()), 
    # path('champs/<int:pk>/',PersUpdateAPI.as_view()),
    # path('champs_detail/<int:pk>/',PersCRUDapi.as_view()),
]
