from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from . import views

router = DefaultRouter()
router.register(r'profile', views.ProfileViewSet, basename='profile')
router.register(r'education', views.EducationViewSet, basename='education')
router.register(r'experience', views.ExperienceViewSet, basename='experience')
router.register(r'skills', views.SkillViewSet, basename='skill')
router.register(r'interests', views.InterestViewSet, basename='interest')
router.register(r'projects', views.ProjectViewSet, basename='project')
router.register(r'facts', views.FactViewSet, basename='fact')
router.register(r'contact', views.ContactViewSet, basename='contact')

urlpatterns = [
    path('', views.api_root),
    path('', include(router.urls)),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
