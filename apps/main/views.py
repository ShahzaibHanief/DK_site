from django.shortcuts import render, get_object_or_404,redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import (
    WorkHour, About, Achievement, TeamMember, 
    Service, Course, ContactInfo, SocialLink,
    ProjectCategory, Project, SiteStat,BlogPost
)




def home(request):
    all_services = Service.objects.filter(is_active=True)
    home_services = Service.objects.filter(is_active=True, show_on_home=True)[:3]
    home_courses = Course.objects.filter(is_active=True, show_on_home=True)[:4]
    featured_projects = Project.objects.filter(is_active=True, is_featured=True)[:3]
    featured_posts = BlogPost.objects.filter(is_active=True, is_featured=True)[:3]
    
    return render(request, 'index.html', {
        'all_services': all_services,
        'home_services': home_services,
        'home_courses': home_courses,
        'featured_projects': featured_projects,
        'featured_posts': featured_posts,
    })

def about(request):
    about_data = About.objects.filter(is_active=True).first()
    achievements = Achievement.objects.all()
    team_members = TeamMember.objects.filter(is_active=True)
    context = {
        'about': about_data,
        'achievements': achievements,
        'team_members': team_members,
    }
    return render(request, 'about.html', context)

def services(request):
    all_services = Service.objects.filter(is_active=True)
    return render(request, 'services.html', {'services': all_services})

def training(request):
    all_courses = Course.objects.filter(is_active=True)
    return render(request, 'trainings.html', {'courses': all_courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk, is_active=True)
    return render(request, 'course_detail.html', {'course': course})

def projects(request):
    categories = ProjectCategory.objects.all()
    all_projects = Project.objects.filter(is_active=True)
    site_stats = SiteStat.objects.filter(is_active=True)
    
    return render(request, 'projects.html', {
        'categories': categories,
        'projects': all_projects,
        'site_stats': site_stats,
    })


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk, is_active=True)
    related_projects = Project.objects.filter(
        category=project.category, 
        is_active=True
    ).exclude(pk=pk)[:3]
    return render(request, 'project_detail.html', {
        'project': project,
        'related_projects': related_projects,
    })



def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Here you can save to database or send email
        # For now, just return success
        
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': True, 'message': 'Message sent successfully!'})
        
        messages.success(request, 'Message sent successfully! We will contact you soon.')
        return redirect('contact')
    
    return render(request, 'contact.html')



def blog(request):
    all_posts = BlogPost.objects.filter(is_active=True)
    return render(request, 'blog.html', {'posts': all_posts})

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, is_active=True)
    related_posts = BlogPost.objects.filter(
        category=post.category, 
        is_active=True
    ).exclude(pk=post.pk)[:3]
    return render(request, 'blog_detail.html', {
        'post': post,
        'related_posts': related_posts,
    })