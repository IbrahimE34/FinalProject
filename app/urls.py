from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app import views

# router = DefaultRouter()
#
#
# router.register(r'cars', views.CarViewSet, basename='cars')

urlpatterns = [
    path("car/create/", views.CarCreateApi.as_view()),
    path("car/create/list/", views.CarlistApi.as_view()),
    path("car/update/<pk>", views.CarUpdateApiView.as_view()),
    path("car/destroy/<pk>", views.CarDestroyApi.as_view()),
    path("car/list/", views.CarListView.as_view()),
    # path("cars/", include(router.urls))


]