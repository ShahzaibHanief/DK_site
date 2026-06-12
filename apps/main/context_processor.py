from .models import WorkHour,ContactInfo, SocialLink

def work_hours(request):
    """Makes work hours available in all templates"""
    return {
        'work_hours': WorkHour.objects.all()
    }

def site_settings(request):
    """Makes site settings available in all templates"""
    contact_info = ContactInfo.objects.filter(is_active=True).first()
    social_links = SocialLink.objects.filter(is_active=True)
    
    return {
        'work_hours': WorkHour.objects.all(),
        'contact_info': contact_info,
        'social_links': social_links,
    }