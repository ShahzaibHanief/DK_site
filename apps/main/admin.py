
from django.contrib import admin
from .models import (
    WorkHour, About, Achievement, TeamMember, 
    Service, Course, ContactInfo, SocialLink,
    ProjectCategory, Project, SiteStat,BlogPost
)
# Register your models here.
@admin.register(WorkHour)
class WorkHourAdmin(admin.ModelAdmin):
    list_display = ['day', 'start_time', 'end_time', 'is_closed']
    list_editable = ['start_time', 'end_time', 'is_closed']
    list_filter = ['is_closed']

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']
    list_editable = ['is_active']


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ['text', 'icon', 'order']
    list_editable = ['icon', 'order']


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'order', 'is_active']
    list_editable = ['order', 'is_active']




@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon', 'order', 'is_active', 'show_on_home']
    list_editable = ['icon', 'order', 'is_active', 'show_on_home']
    list_filter = ['is_active', 'show_on_home', 'icon']
    search_fields = ['title', 'description']



@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'duration', 'level', 'schedule', 'status', 'fee', 'order', 'is_active', 'show_on_home']
    list_editable = ['order', 'is_active', 'show_on_home', 'status']
    list_filter = ['level', 'status', 'is_active', 'show_on_home']
    search_fields = ['title', 'short_description']
    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'icon', 'duration', 'level', 'schedule', 'status', 'fee')
        }),
        ('Descriptions', {
            'fields': ('short_description', 'full_description')
        }),
        ('Details', {
            'fields': ('syllabus', 'projects', 'tools', 'instructor', 'start_date', 'certificate')
        }),
        ('Settings', {
            'fields': ('order', 'is_active', 'show_on_home')
        }),
    )




@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ['email', 'phone', 'is_active']
    list_editable = ['is_active']


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ['platform', 'url', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    list_filter = ['platform', 'is_active']




@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'order']
    list_editable = ['order']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'year', 'is_featured', 'is_active', 'order']
    list_editable = ['year', 'is_featured', 'is_active', 'order']
    list_filter = ['category', 'year', 'is_featured', 'is_active']
    search_fields = ['title', 'description']


@admin.register(SiteStat)
class SiteStatAdmin(admin.ModelAdmin):
    list_display = ['value', 'label', 'suffix', 'order', 'is_active']
    list_editable = ['order', 'is_active']



@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author', 'published_date', 'is_featured', 'is_active']
    list_editable = ['category', 'is_featured', 'is_active']  # ← Category editable
    list_filter = ['published_date', 'is_featured', 'is_active']  # ← Category filter hata diya
    search_fields = ['title', 'excerpt', 'content', 'category']  # ← Category search mein
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'slug', 'category', 'author', 'published_date', 'read_time')  # ← Category free text
        }),
        ('Content', {
            'fields': ('excerpt', 'content', 'image')
        }),
        ('Settings', {
            'fields': ('is_featured', 'is_active')
        }),
    )