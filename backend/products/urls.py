from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('<int:pk>/', views.ProductDetailAPIView.as_view(), name='detail-view'),
    path('', views.ProductListCreateAPIView.as_view()),
    path('<int:pk>/update', views.ProductUpdateAPIView.as_view()),
    path('<int:pk>/delete', views.ProductDeleteAPIView.as_view())
]