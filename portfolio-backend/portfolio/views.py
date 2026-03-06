from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.http import JsonResponse

from .models import Profile, Education, Experience, Skill, Interest, Project, Fact, ContactMessage
from .serializers import (
    ProfileSerializer, EducationSerializer, ExperienceSerializer,
    SkillSerializer, InterestSerializer, ProjectSerializer,
    FactSerializer, ContactMessageSerializer
)


class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Profile.objects.filter(is_active=True)
    serializer_class = ProfileSerializer

    def list(self, request, *args, **kwargs):
        profile = self.get_queryset().first()
        if not profile:
            return Response({})
        serializer = self.get_serializer(profile)
        return Response(serializer.data)


class EducationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class ExperienceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class InterestViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        project_type = self.request.query_params.get('type')
        if project_type:
            qs = qs.filter(project_type=project_type)
        return qs


class FactViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Fact.objects.all()
    serializer_class = FactSerializer


class ContactViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def create(self, request):
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            msg = serializer.save()
            from .services import send_contact_notification
            send_contact_notification(msg)
            return Response(
                {'message': 'Message envoyé avec succès'},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def api_root(request):
    """Point d'entrée de l'API avec liens vers la documentation."""
    return JsonResponse({
        'message': 'Portfolio API - Océane Konan',
        'documentation': '/api/schema/swagger-ui/',
        'endpoints': {
            'profile': '/api/profile/',
            'education': '/api/education/',
            'experience': '/api/experience/',
            'skills': '/api/skills/',
            'interests': '/api/interests/',
            'projects': '/api/projects/',
            'facts': '/api/facts/',
            'contact': '/api/contact/ (POST)',
        }
    })
