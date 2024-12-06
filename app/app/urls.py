from django.urls import path, include
from rest_framework import routers
from forms import views


router = routers.SimpleRouter()
router.register('forms', views.FormsAPIView)

urlpatterns = [
    path('', include(router.urls)),
]
