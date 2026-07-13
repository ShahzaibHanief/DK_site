from django.db import models
from django.urls import reverse
from django.utils.text import slugify
import uuid



ICON_CHOICES = [
    ('fa-globe', 'Globe - Web'),
    ('fa-mobile-alt', 'Mobile'),
    ('fa-cloud', 'Cloud'),
    ('fa-robot', 'Robot - AI'),
    ('fa-shield-alt', 'Shield - Security'),
    ('fa-chart-line', 'Chart - Marketing'),
    ('fa-code', 'Code'),
    ('fa-database', 'Database'),
    ('fa-brain', 'Brain - AI'),
    ('fa-laptop-code', 'Laptop Code'),
    ('fa-shopping-cart', 'Shopping Cart'),
    ('fa-hospital', 'Hospital'),
    ('fa-graduation-cap', 'Graduation Cap'),
    # SEO & Marketing
    ('fa-search', 'Search - SEO'),
    ('fa-magnifying-glass', 'Magnifying Glass - SEO'),
    ('fa-ranking-star', 'Ranking Star - SEO'),
    # YouTube Automation
    ('fa-youtube', 'YouTube'),
    ('fa-play-circle', 'Play Circle - Video'),
    ('fa-video', 'Video Camera'),
    ('fa-clapperboard', 'Clapperboard - Video'),
    # Digital Marketing
    ('fa-bullhorn', 'Bullhorn - Marketing'),
    ('fa-megaphone', 'Megaphone - Marketing'),
    ('fa-ads', 'Ads - Marketing'),
    ('fa-hashtag', 'Hashtag - Social Media'),
    ('fa-share-nodes', 'Share Nodes - Social'),
    ('fa-envelope-open-text', 'Email Marketing'),
    ('fa-paper-plane', 'Paper Plane - Marketing'),
]
  













# --- Existing models (keep these) ---
class WorkHour(models.Model):
    DAY_CHOICES = [
        ('Mon-Fri', 'Monday - Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
    day = models.CharField(max_length=20, choices=DAY_CHOICES, unique=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_closed = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['id']
        verbose_name = 'Work Hour'
        verbose_name_plural = 'Work Hours'
    
    def __str__(self):
        if self.is_closed:
            return f"{self.day}: Closed"
        return f"{self.day}: {self.start_time.strftime('%I:%M %p')} - {self.end_time.strftime('%I:%M %p')}"
    
    @property
    def formatted_hours(self):
        if self.is_closed:
            return "Closed"
        return f"{self.start_time.strftime('%I:%M %p')} - {self.end_time.strftime('%I:%M %p')}"


class About(models.Model):
    """About page content - single record"""
    title = models.CharField(max_length=200, default="About Digital King")
    subtitle = models.CharField(max_length=300, default="Innovative IT solutions & training hub in Rajanpur")
    story_title = models.CharField(max_length=200, default="5+ Years of Digital Excellence")
    story_paragraph_1 = models.TextField(default="Founded in 2018, Digital King Software House started as a small team of passionate developers.")
    story_paragraph_2 = models.TextField(default="We blend creativity with cutting-edge technology to deliver solutions that drive real business growth.")
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    mission_title = models.CharField(max_length=100, default="Our Mission")
    mission_text = models.TextField(default="Empower businesses and individuals through innovative technology solutions.")
    vision_title = models.CharField(max_length=100, default="Our Vision")
    vision_text = models.TextField(default="To become Pakistan's leading software house known for quality and innovation.")
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'About Page'
        verbose_name_plural = 'About Page'
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        """Ensure only one active about record exists"""
        if self.is_active:
            About.objects.filter(is_active=True).update(is_active=False)
        super().save(*args, **kwargs)


class Achievement(models.Model):
    """Achievements grid on about page"""
    icon = models.CharField(max_length=50, default='fa-trophy')
    text = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.text


class TeamMember(models.Model):
    """Team members on about page"""
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team/', blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
        verbose_name = 'Team Member'
        verbose_name_plural = 'Team Members'
    
    def __str__(self):
        return f"{self.name} - {self.role}"





class Service(models.Model):
      
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, choices=ICON_CHOICES, default='fa-globe')
    features = models.JSONField(default=list, help_text="List of features: ['Feature 1', 'Feature 2']")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    show_on_home = models.BooleanField(default=False, help_text="Show this service on home page")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
    
    def __str__(self):
        return self.title
    
    @property
    def feature_list(self):
        if isinstance(self.features, list):
            return self.features
        return []







class Course(models.Model):
    LEVEL_CHOICES = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    ]
    
    STATUS_CHOICES = [
        ('Open', 'Open for Enrollment'),
        ('Closed', 'Enrollment Closed'),
        ('Coming Soon', 'Coming Soon'),
    ]
    
    SCHEDULE_CHOICES = [
        ('Weekends', 'Weekends'),
        ('Mon-Wed', 'Monday - Wednesday'),
        ('Thu-Sat', 'Thursday - Saturday'),
        ('Daily', 'Daily'),
        ('Flexible', 'Flexible'),
    ]
   
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=50,choices=ICON_CHOICES, default='fa-code')
    duration = models.CharField(max_length=50, help_text="e.g., 12 Weeks")
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='Beginner')
    schedule = models.CharField(max_length=20, choices=SCHEDULE_CHOICES, default='Weekends')
    slug = models.SlugField(unique=True,blank=True,null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Open')
    short_description = models.TextField(help_text="Short text for card")
    full_description = models.TextField(help_text="Full details for detail page")
    syllabus = models.JSONField(default=list, help_text="List of topics: ['Topic 1', 'Topic 2']")
    projects = models.JSONField(default=list, help_text="List of projects: ['Project 1', 'Project 2']")
    tools = models.JSONField(default=list, help_text="Tools covered: ['Tool 1', 'Tool 2']")
    start_date = models.DateField(blank=True, null=True)
    fee = models.CharField(max_length=50, blank=True, null=True, help_text="e.g., PKR 15,000")
    instructor = models.CharField(max_length=100, blank=True, null=True)
    certificate = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    show_on_home = models.BooleanField(default=False, help_text="Show on home page")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
    
    def __str__(self):
        return f"{self.title} ({self.duration})"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            # Check if slug exists, if yes add number
            while Course.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug

        super().save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'slug': self.slug})
    
    @property
    def syllabus_list(self):
        if isinstance(self.syllabus, list):
            return self.syllabus
        return []
    
    @property
    def projects_list(self):
        if isinstance(self.projects, list):
            return self.projects
        return []
    
    @property
    def tools_list(self):
        if isinstance(self.tools, list):
            return self.tools
        return []



class ContactInfo(models.Model):
    """Contact page information - single record"""
    address = models.TextField(default="Main Ghala Mandi Road, Rajanpur, Punjab, Pakistan")
    phone = models.CharField(max_length=50, default="+92 300 1234567")
    email = models.EmailField(default="info@digitalking.com.pk")
    whatsapp = models.CharField(max_length=50, blank=True, null=True, default="+92 300 1234567")
    map_embed_url = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        default="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d215527.47870880097!2d70.123456!3d29.123456!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3938f5c6a5b8b8b9%3A0x8b8b8b8b8b8b8b8b!2sRajanpur!5e0!3m2!1sen!2s!4v1700000000000!5m2!1sen!2s"
    )
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = 'Contact Info'
        verbose_name_plural = 'Contact Info'
    
    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        """Ensure only one active contact info exists"""
        if self.is_active:
            ContactInfo.objects.filter(is_active=True).update(is_active=False)
        super().save(*args, **kwargs)


class SocialLink(models.Model):
    """Social media links"""
    PLATFORM_CHOICES = [
        ('facebook', 'Facebook'),
        ('linkedin', 'LinkedIn'),
        ('instagram', 'Instagram'),
        ('twitter', 'Twitter'),
        ('youtube', 'YouTube'),
        ('tiktok', 'TikTok'),
        ('whatsapp', 'WhatsApp'),
    ]
    
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    url = models.URLField()
    icon = models.CharField(max_length=50, default='fa-facebook-f')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.platform
    
    @property
    def icon_class(self):
        icon_map = {
            'facebook': 'fab fa-facebook-f',
            'linkedin': 'fab fa-linkedin-in',
            'instagram': 'fab fa-instagram',
            'twitter': 'fab fa-twitter',
            'youtube': 'fab fa-youtube',
            'tiktok': 'fab fa-tiktok',
            'whatsapp': 'fab fa-whatsapp',
        }
        return icon_map.get(self.platform, 'fas fa-link')



class ProjectCategory(models.Model):
    """Project categories for filtering"""
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Project Category'
        verbose_name_plural = 'Project Categories'
    
    def __str__(self):
        return self.name


class Project(models.Model):
    """Portfolio projects"""
    title = models.CharField(max_length=100)
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE, related_name='projects')
    slug = models.SlugField(unique=True,null=True,blank=True)
    description = models.TextField()
    short_description = models.TextField(help_text="Short text for card view")
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    tech_stack = models.JSONField(default=list, help_text="Technologies: ['React', 'Node.js']")
    stats = models.JSONField(default=dict, help_text='{"users": "50K+", "label": "Users"}')
    year = models.PositiveIntegerField(default=2024)
    is_featured = models.BooleanField(default=False, help_text="Show on home page")
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            # Check if slug exists, if yes add number
            while Course.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug

        super().save(*args, **kwargs)

    
    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'slug': self.slug})
    
    @property
    def tech_list(self):
        if isinstance(self.tech_stack, list):
            return self.tech_stack
        return []
    
    @property
    def stat_display(self):
        if isinstance(self.stats, dict):
            return self.stats
        return {"value": "N/A", "label": "N/A"}
    


class SiteStat(models.Model):
    """Dynamic stats for projects page"""
    label = models.CharField(max_length=50)           # e.g., "Projects Completed"
    value = models.CharField(max_length=20)           # e.g., "150+"
    suffix = models.CharField(max_length=10, blank=True, null=True)  # +, %, etc.
    icon = models.CharField(max_length=50, default='fa-check')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
        verbose_name = 'Site Stat'
        verbose_name_plural = 'Site Stats'
    
    def __str__(self):
        return f"{self.value} {self.label}"
    





class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    category = models.CharField(max_length=50, default='General')  # ← Free text, no choices
    excerpt = models.TextField(help_text="Short summary for card view")
    content = models.TextField(help_text="Full blog post content")
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    author = models.CharField(max_length=100, default='Digital King Team')
    published_date = models.DateField()
    read_time = models.PositiveIntegerField(default=5, help_text="Estimated read time in minutes")
    is_featured = models.BooleanField(default=False, help_text="Show on home page")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-published_date', '-created_at']
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})
    
    @property
    def formatted_date(self):
        return self.published_date.strftime('%b %d, %Y')
    



class Subject(models.Model):
    title = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"
        ordering = ['title']
    
    def __str__(self):
        return self.title


class ContactForm(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    contact = models.CharField(max_length=20)
    
    # ✅ ForeignKey - Admin se subjects set honge
    subject = models.ForeignKey(
        Subject,
        on_delete=models.SET_NULL,  # Subject delete ho to null ho jaye
        null=True,
        blank=True,
        related_name='contacts'
    )
    
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.subject}"