from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ImageApiView , WeatherApiView

app_name = "main"

router = DefaultRouter()
router.register(r'image', ImageApiView, basename='image')

urlpatterns = [
    path("weather", WeatherApiView.as_view({'get': 'list'}) , name="test")
]
