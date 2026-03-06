from django.contrib import admin
from .models import (
    Profile, Education, Experience, Skill, Interest,
    Project, Fact, ContactMessage
)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'is_active')
    list_filter = ('is_active',)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('title', 'period', 'place', 'order')


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')


@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'order')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'project_type', 'tech', 'order')
    list_filter = ('project_type',)


@admin.register(Fact)
class FactAdmin(admin.ModelAdmin):
    list_display = ('number', 'suffix', 'label', 'order')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    list_display_links = ('subject',)
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')
