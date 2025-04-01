from django.urls import path
from .views import CategoryViewSets, ProductViewSets


urlpatterns = [
    path('', ProductViewSets.as_view({'get': 'list', 'post': 'create'})),
    path('<int:pk>/', ProductViewSets.as_view({'get': 'retrieve', 'put': 'update','delete':'destroy'})),

    path('category/', CategoryViewSets.as_view({'get': 'list'}))

]