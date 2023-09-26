from django.urls import path
from .views import CategoryListCreateView, LocationListView, LocationDetailView, PersonListView, PersonDetailView

urlpatterns = [
    path('api/categorys/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('api/locations/', LocationListView.as_view({'get': 'list', 'post': 'create'}), name='location-list-create'),
    path('api/locations/<int:pk>/', LocationDetailView.as_view(), name='location-detail'),
    path('api/persons/', PersonListView.as_view({'get': 'list'}), name='person-list-create'),
    path('api/persons/<int:pk>/', PersonDetailView.as_view(), name='person-detail')
    
        
]


    
