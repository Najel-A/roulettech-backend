from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet
from .views import about
from .views import generateFunFact

router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('about', about, name='about'),
    path('generateFunFact', generateFunFact, name="generateFunFact")
]
