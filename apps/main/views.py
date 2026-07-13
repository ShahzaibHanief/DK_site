from django.shortcuts import render, get_object_or_404,redirect
from django.http import JsonResponse
from django.contrib import messages
from .models import (
    WorkHour, About, Achievement, TeamMember, 
    Service, Course, ContactInfo, SocialLink,
    ProjectCategory, Project, SiteStat,BlogPost,ContactForm, Subject
)
from django.core.mail import send_mail
from django.conf import settings





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

def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug, is_active=True)
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


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug, is_active=True)
    related_projects = Project.objects.filter(
        category=project.category, 
        is_active=True
    ).exclude(slug=slug)[:3]
    return render(request, 'project_detail.html', {
        'project': project,
        'related_projects': related_projects,
    })






import threading
from django.core.mail import send_mail
from django.shortcuts import render
from django.conf import settings
from .models import Subject, ContactForm

def send_email_background(subject, body, from_email, recipient_list):
    """Background mein email bhejo — user wait nahi karega"""
    try:
        send_mail(subject, body, from_email, recipient_list, fail_silently=False)
    except Exception as e:
        print(f"Email error: {str(e)}")

def contact(request):
    subjects = Subject.objects.filter(is_active=True)
    
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        subject_id = request.POST.get('subject')
        message = request.POST.get('message', '').strip()
        
        # Validation
        if not all([name, email, phone, message]):
            return render(request, 'contact.html', {
                'subjects': subjects,
                'error': 'Please fill all required fields!'
            })
        
        # Subject object
        subject_obj = None
        if subject_id:
            try:
                subject_obj = Subject.objects.get(id=subject_id)
            except Subject.DoesNotExist:
                pass
        
        # 1. Database save (instant)
        ContactForm.objects.create(
            name=name,
            email=email,
            contact=phone,
            subject=subject_obj,
            message=message
        )
        
        # 2. Admin email — BACKGROUND thread mein
        admin_subject = f"New Contact: {subject_obj.title if subject_obj else 'General'} from {name}"
        admin_body = f"""New Contact Form Submission

Name: {name}
Email: {email}
Phone: {phone}
Subject: {subject_obj.title if subject_obj else 'N/A'}
Message: {message}"""
        
        threading.Thread(
            target=send_email_background,
            args=(admin_subject, admin_body, settings.DEFAULT_FROM_EMAIL, [settings.ADMIN_EMAIL]),
            daemon=True
        ).start()
        
        # 3. User auto-reply — BACKGROUND thread mein
        user_subject = "Thank you for contacting Digital King Skills!"
        user_body = f"""Dear {name},

Thank you for reaching out to us! We have received your message and will get back to you very soon.

Your Submission Details:
------------------------
Name: {name}
Email: {email}
Phone: {phone}
Subject: {subject_obj.title if subject_obj else 'General Inquiry'}
Message: {message}

We typically respond within 24 hours.

Best regards,
Digital King Skills Team
Rajanpur, Punjab, Pakistan
Phone: +92 300 1234567
Email: info@digitalking.com.pk"""
        
        threading.Thread(
            target=send_email_background,
            args=(user_subject, user_body, settings.DEFAULT_FROM_EMAIL, [email]),
            daemon=True
        ).start()
        
        # ✅ INSTANT success page — user wait nahi karega
        return render(request, 'success.html', {
            'name': name,
            'email': email
        })
    
    return render(request, 'contact.html', {'subjects': subjects})



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