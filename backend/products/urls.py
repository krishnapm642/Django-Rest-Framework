from django.urls import path
from . import views


urlpatterns = [
    path('<int:pk>/', views.product_mixin_view),
    path('', views.product_mixin_view),
    path('<int:pk>/update', views.ProductUpdateAPIView.as_view()),
    path('<int:pk>/delete', views.ProductDeleteAPIView.as_view())
]