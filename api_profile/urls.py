from django.contrib import admin
from django.urls import path
from user_profile.views import User, UserViewSet
from rest_framework import routers
from django.conf.urls import include

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('register/', User.as_view()),
]
