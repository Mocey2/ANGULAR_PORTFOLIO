from rest_framework import serializers
from .models import Profile, Education, Experience, Skill, Interest, Project, Fact, ContactMessage


class ProfileSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()
    cv_url = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = [
            'id', 'full_name', 'first_name', 'last_name', 'headline', 'bio_lead', 'bio_paragraph', 'personality',
            'email', 'phone', 'photo', 'photo_url', 'cv_url',
            'linkedin_url', 'github_url'
        ]

    def get_photo_url(self, obj):
        if obj.photo:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.photo.url)
            return obj.photo.url
        return None

    def get_cv_url(self, obj):
        if obj.cv_file:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.cv_file.url)
            return obj.cv_file.url
        return None


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['id', 'period', 'title', 'place']


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ['id', 'title', 'description']


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name']


class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = ['id', 'title', 'subtitle', 'icon']


class ProjectSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    type = serializers.CharField(source='project_type', read_only=True)

    class Meta:
        model = Project
        fields = [
            'id', 'title', 'short_desc', 'full_desc',
            'tech', 'image', 'image_url', 'type'
        ]

    def get_image_url(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None


class FactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fact
        fields = ['id', 'number', 'suffix', 'label', 'icon']


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']

    def create(self, validated_data):
        return ContactMessage.objects.create(**validated_data)
