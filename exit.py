from django.utils.text import slugify
from apps.main.models import Course,Project

# Fix all null slugs
for project in Project.objects.filter(slug__isnull=True):
    base_slug = slugify(project.title)
    slug = base_slug
    counter = 1
    
    while Project.objects.filter(slug=slug).exists():
        slug = f"{base_slug}-{counter}"
        counter += 1
    
    project.slug = slug
    project.save()
    print(f"✓ {project.title} -> {slug}")

print("All slugs updated!")






# Create the complete updated base.html file

complete_base_html = '''{% load static %}

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    {% block title %}
    <title>Digital King Skills | Software House & IT Training</title>
    {% endblock %}
    
    <!-- Global CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Poppins:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
    
    <link rel="stylesheet" href="{% static 'css/styles.css' %}">
    <link rel="stylesheet" href="{% static 'css/back-image.css' %}">
    <link rel="stylesheet" href="{% static 'css/login.css' %}">
    
    <style>
    /* ============================================
       COMPLETE NAVBAR + MOBILE SIDEBAR FIX
       ============================================ */
    
    /* Prevent horizontal overflow */
    html, body {
        overflow-x: hidden !important;
        max-width: 100vw;
    }
    
    /* ========== NAVBAR CONTAINER ========== */
    #mainNav > .container,
    #mainNav > .container-fluid {
        display: flex !important;
        flex-wrap: nowrap !important;
        justify-content: space-between !important;
        align-items: center !important;
        padding: 8px 12px !important;
        max-width: 100% !important;
        width: 100% !important;
        position: relative !important;
    }
    
    /* ========== NAVBAR BRAND ========== */
    #mainNav .navbar-brand {
        display: flex !important;
        align-items: center !important;
        margin: 0 !important;
        padding: 0 !important;
        width: auto !important;
        max-width: none !important;
        flex: 0 0 auto !important;
        min-width: 0 !important;
    }
    
    #mainNav .logo-wrapper {
        display: flex !important;
        align-items: center !important;
        gap: 6px !important;
        min-width: 0 !important;
        width: auto !important;
    }
    
    #mainNav .logo-img,
    #mainNav .navbar-brand img {
        height: 32px !important;
        width: auto !important;
        flex-shrink: 0 !important;
        display: block !important;
        border-radius: 8px !important;
    }
    
    /* Brand Text - Full Always */
    #mainNav .brand-text {
        font-weight: 800 !important;
        white-space: nowrap !important;
        display: inline-block !important;
        line-height: 1.2 !important;
        color: var(--text-white) !important;
        vertical-align: middle !important;
        max-width: none !important;
        overflow: visible !important;
        text-overflow: clip !important;
    }
    
    #mainNav .brand-highlight {
        color: var(--gold-primary) !important;
    }
    
    /* Responsive Font Size */
    @media (min-width: 1200px) { #mainNav .brand-text { font-size: 1.1rem !important; } }
    @media (min-width: 992px) and (max-width: 1199px) { #mainNav .brand-text { font-size: 0.95rem !important; } }
    @media (min-width: 768px) and (max-width: 991px) { #mainNav .brand-text { font-size: 0.85rem !important; } }
    @media (max-width: 767px) { #mainNav .brand-text { font-size: 0.75rem !important; } }
    @media (max-width: 360px) { #mainNav .brand-text { font-size: 0.7rem !important; } }
    
    /* ========== TOGGLE BUTTON - MOBILE ONLY ========== */
    @media (max-width: 991px) {
        #mainNav .navbar-toggler {
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            border: 1px solid var(--gold-primary) !important;
            padding: 6px 10px !important;
            border-radius: 8px !important;
            background: rgba(245, 166, 35, 0.15) !important;
            margin: 0 !important;
            margin-left: 8px !important;
            flex-shrink: 0 !important;
            flex: 0 0 auto !important;
            order: 2 !important;
            position: relative !important;
            right: 0 !important;
            left: auto !important;
            width: 42px !important;
            height: 38px !important;
            min-width: 42px !important;
            min-height: 38px !important;
            max-width: 42px !important;
            max-height: 38px !important;
            background-color: transparent !important;
            box-shadow: none !important;
            z-index: 1050 !important;
        }
    
        #mainNav .navbar-toggler-icon {
            background-image: url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 30 30'%3e%3cpath stroke='rgba%28245, 166, 35, 1%29' stroke-linecap='round' stroke-miterlimit='10' stroke-width='2' d='M4 7h22M4 15h22M4 23h22'/%3e%3c/svg%3e") !important;
            width: 1.2em !important;
            height: 1.2em !important;
            display: inline-block !important;
        }
    }
    
    /* Desktop - Toggle Hidden */
    @media (min-width: 992px) {
        #mainNav .navbar-toggler {
            display: none !important;
        }
    }
    
    /* Inner Pages Background */
    body:not(.home-page) #mainNav {
        background: var(--teal-dark) !important;
        border-bottom: 1px solid var(--glass-border);
    }
    
    /* Scrolled Navbar */
    #mainNav.scrolled {
        background: var(--teal-dark) !important;
        backdrop-filter: blur(12px);
        padding: 8px 0;
        border-bottom: 1px solid var(--glass-border);
        box-shadow: 0 4px 20px rgba(0,0,0,0.2);
    }
    
    /* ============================================
       MOBILE SIDEBAR - GLASSMORPHISM
       ============================================ */
    @media (max-width: 991px) {
        #mobileSidebar {
            width: 320px !important;
            max-width: 85vw !important;
            background: linear-gradient(180deg, rgba(11, 79, 108, 0.98), rgba(8, 60, 82, 0.99)) !important;
            backdrop-filter: blur(20px) !important;
            -webkit-backdrop-filter: blur(20px) !important;
            border-left: 1px solid rgba(245, 166, 35, 0.3) !important;
            box-shadow: -10px 0 40px rgba(0,0,0,0.5) !important;
        }
        
        #mobileSidebar .offcanvas-header {
            padding: 20px;
            border-bottom: 1px solid rgba(245, 166, 35, 0.2);
            background: rgba(245, 166, 35, 0.05);
        }
        
        #mobileSidebar .offcanvas-header .sidebar-logo {
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        #mobileSidebar .offcanvas-header .sidebar-logo img {
            height: 40px;
            width: auto;
            border-radius: 10px;
        }
        
        #mobileSidebar .offcanvas-header .sidebar-logo span {
            font-weight: 800;
            color: #fff;
            font-size: 1rem;
        }
        
        #mobileSidebar .offcanvas-header .sidebar-logo span .highlight {
            color: #F5A623;
        }
        
        #mobileSidebar .btn-close {
            width: 36px;
            height: 36px;
            border-radius: 50%;
            border: 1px solid rgba(245, 166, 35, 0.3);
            background: rgba(245, 166, 35, 0.1);
            opacity: 1;
            transition: all 0.3s ease;
            filter: invert(1) sepia(1) saturate(5) hue-rotate(350deg);
        }
        
        #mobileSidebar .btn-close:hover {
            background: #F5A623;
            transform: rotate(90deg);
        }
        
        #mobileSidebar .offcanvas-body {
            padding: 0 !important;
            overflow-y: auto;
        }
        
        #mobileSidebar .navbar-nav {
            padding: 15px 0;
            gap: 5px;
        }
        
        #mobileSidebar .navbar-nav .nav-item {
            padding: 0 15px;
        }
        
        #mobileSidebar .navbar-nav .nav-link {
            display: flex;
            align-items: center;
            gap: 15px;
            padding: 14px 18px;
            border-radius: 12px;
            color: #fff;
            font-size: 1rem;
            font-weight: 500;
            transition: all 0.3s ease;
            position: relative;
            text-decoration: none;
        }
        
        #mobileSidebar .navbar-nav .nav-link i {
            font-size: 1.2rem;
            color: #F5A623;
            width: 24px;
            text-align: center;
            transition: all 0.3s ease;
        }
        
        #mobileSidebar .navbar-nav .nav-link:hover,
        #mobileSidebar .navbar-nav .nav-link.active {
            background: rgba(245, 166, 35, 0.15);
            color: #F5A623;
            transform: translateX(5px);
        }
        
        #mobileSidebar .navbar-nav .nav-link.active::before {
            content: '';
            position: absolute;
            left: 0;
            top: 50%;
            transform: translateY(-50%);
            width: 3px;
            height: 60%;
            background: #F5A623;
            border-radius: 0 3px 3px 0;
        }
        
        #mobileSidebar .navbar-nav .nav-link::after {
            content: '\\f054';
            font-family: 'Font Awesome 6 Free';
            font-weight: 900;
            font-size: 0.8rem;
            color: #F5A623;
            margin-left: auto;
            opacity: 0.6;
            transition: all 0.3s ease;
        }
        
        #mobileSidebar .navbar-nav .nav-link:hover::after {
            opacity: 1;
            transform: translateX(3px);
        }
        
        #mobileSidebar .sidebar-footer {
            padding: 20px;
            margin-top: auto;
            border-top: 1px solid rgba(245, 166, 35, 0.2);
        }
        
        #mobileSidebar .sidebar-footer .btn-glow {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            width: 100%;
            padding: 14px 20px;
            font-size: 1rem;
            border-radius: 12px;
            background: linear-gradient(135deg, #F5A623, #FFB74D);
            color: #1A1A2E;
            font-weight: 700;
            text-decoration: none;
            transition: all 0.3s ease;
            border: none;
        }
        
        #mobileSidebar .sidebar-footer .btn-glow:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 25px rgba(245,166,35,0.4);
        }
        
        .offcanvas-backdrop.show {
            opacity: 0.6 !important;
            backdrop-filter: blur(4px);
        }
        
        #mobileSidebar .offcanvas-body::-webkit-scrollbar {
            width: 4px;
        }
        #mobileSidebar .offcanvas-body::-webkit-scrollbar-track {
            background: transparent;
        }
        #mobileSidebar .offcanvas-body::-webkit-scrollbar-thumb {
            background: #F5A623;
            border-radius: 4px;
        }
    }
    </style>
    
    {% block extra_css %}{% endblock %}
</head>
<body>

    <!-- ==================== NAVBAR ==================== -->
    {% block navbar %}
    <nav class="navbar navbar-expand-lg fixed-top" id="mainNav">
        <div class="container">
            <a class="navbar-brand" href="{% url 'home' %}">
                <div class="logo-wrapper">
                    <img src="{% static 'images/logo4.png' %}" alt="Digital King Logo" class="logo-img" style="border-radius: 12px;">
                    <span class="brand-text">DIGITAL <span class="brand-highlight">KING</span> SKILLS</span>
                </div>
            </a>
            
            <!-- Mobile Toggle Button - Offcanvas -->
            <button class="navbar-toggler" type="button" data-bs-toggle="offcanvas" data-bs-target="#mobileSidebar" aria-controls="mobileSidebar" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            
            <!-- Desktop Menu (visible on lg and up) -->
            <div class="collapse navbar-collapse d-none d-lg-flex" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item"><a class="nav-link {% if request.resolver_match.url_name == 'home' %}active{% endif %}" href="{% url 'home' %}">Home</a></li>
                    <li class="nav-item"><a class="nav-link {% if request.resolver_match.url_name == 'about' %}active{% endif %}" href="{% url 'about' %}">About</a></li>
                    <li class="nav-item"><a class="nav-link {% if request.resolver_match.url_name == 'services' %}active{% endif %}" href="{% url 'services' %}">Services</a></li>
                    <li class="nav-item"><a class="nav-link {% if request.resolver_match.url_name == 'training' %}active{% endif %}" href="{% url 'training' %}">Trainings</a></li>
                    <li class="nav-item"><a class="nav-link {% if request.resolver_match.url_name == 'contact' %}active{% endif %}" href="{% url 'contact' %}">Contact</a></li>
                    <li class="nav-item"><a class="nav-link {% if request.resolver_match.url_name == 'blog' %}active{% endif %}" href="{% url 'blog' %}">Blog</a></li>
                    <li class="nav-item"><a class="nav-link {% if request.resolver_match.url_name == 'projects' %}active{% endif %}" href="{% url 'projects' %}">Our Projects</a></li>
                </ul>
                <a href="{% url 'contact' %}" class="btn-glow ms-lg-3">Get Quote <i class="fas fa-arrow-right"></i></a>
            </div>
        </div>
    </nav>

    <!-- Mobile Sidebar - Offcanvas -->
    <div class="offcanvas offcanvas-end d-lg-none" tabindex="-1" id="mobileSidebar" aria-labelledby="mobileSidebarLabel">
        <div class="offcanvas-header">
            <div class="sidebar-logo">
                <img src="{% static 'images/logo4.png' %}" alt="Digital King Logo">
                <span>DIGITAL <span class="highlight">KING</span> SKILLS</span>
            </div>
            <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
        </div>
        <div class="offcanvas-body d-flex flex-column">
            <ul class="navbar-nav">
                <li class="nav-item">
                    <a class="nav-link {% if request.resolver_match.url_name == 'home' %}active{% endif %}" href="{% url 'home' %}">
                        <i class="fas fa-home"></i> Home
                    </a>
                </li>
                <li class="nav-item">
                    <a class="nav-link {% if request.resolver_match.url_name == 'about' %}active{% endif %}" href="{% url 'about' %}">
                        <i class="fas fa-user"></i> About
                    </a>
                </li>
                <li class="nav-item">
                    <a class="nav-link {% if request.resolver_match.url_name == 'services' %}active{% endif %}" href="{% url 'services' %}">
                        <i class="fas fa-cog"></i> Services
                    </a>
                </li>
                <li class="nav-item">
                    <a class="nav-link {% if request.resolver_match.url_name == 'training' %}active{% endif %}" href="{% url 'training' %}">
                        <i class="fas fa-book"></i> Trainings
                    </a>
                </li>
                <li class="nav-item">
                    <a class="nav-link {% if request.resolver_match.url_name == 'contact' %}active{% endif %}" href="{% url 'contact' %}">
                        <i class="fas fa-phone"></i> Contact
                    </a>
                </li>
                <li class="nav-item">
                    <a class="nav-link {% if request.resolver_match.url_name == 'blog' %}active{% endif %}" href="{% url 'blog' %}">
                        <i class="fas fa-file-alt"></i> Blog
                    </a>
                </li>
                <li class="nav-item">
                    <a class="nav-link {% if request.resolver_match.url_name == 'projects' %}active{% endif %}" href="{% url 'projects' %}">
                        <i class="fas fa-briefcase"></i> Our Projects
                    </a>
                </li>
            </ul>
            <div class="sidebar-footer mt-auto">
                <a href="{% url 'contact' %}" class="btn-glow">
                    <i class="fas fa-comment-dots"></i> Get Quote <i class="fas fa-arrow-right"></i>
                </a>
            </div>
        </div>
    </div>
    {% endblock %}

    <!-- ==================== MAIN CONTENT ==================== -->
    {% block content %}{% endblock %}

    <!-- ==================== FOOTER ==================== -->
    {% block footer %}
    <footer class="footer">
        <div class="container">
            <div class="row g-4">
                <div class="col-lg-4">
                    <div class="footer-logo">
                         <img src="{% static 'images/logo4.png' %}" alt="Logo" style="border-radius: 10px; height: 45px;">
                        <span>DIGITAL<span>KING</span></span>
                    </div>
                    <p>Rajanpur's premier software house & IT training institute.</p>
                    <div class="social-links">
                        {% for link in social_links %}
                            <a href="{{ link.url }}" target="_blank" title="{{ link.platform|title }}">
                                <i class="{{ link.icon_class }}"></i>
                            </a>
                        {% empty %}
                            <a href="#"><i class="fab fa-facebook-f"></i></a>
                            <a href="#"><i class="fab fa-linkedin-in"></i></a>
                            <a href="#"><i class="fab fa-instagram"></i></a>
                            <a href="#"><i class="fab fa-twitter"></i></a>
                        {% endfor %}
                    </div>
                </div>
                <div class="col-lg-2 col-md-6">
                    <h4>Quick Links</h4>
                    <ul>
                        <li><a href="{% url 'about' %}">About Us</a></li>
                        <li><a href="{% url 'services' %}">Services</a></li>
                        <li><a href="{% url 'training' %}">Trainings</a></li>
                        <li><a href="{% url 'blog' %}">Blog</a></li>
                    </ul>
                </div>
                <div class="col-lg-3 col-md-6">
                    <h4>Work Hours</h4>
                    <ul class="hours-list">
                        {% for wh in work_hours %}
                            <li><span>{{wh.day}}</span>
                                {% if wh.is_closed %}closed{% else %}{{wh.formatted_hours}}{% endif %}
                            </li>
                        {% empty %}
                            <li><span>Mon-Fri:</span> 9:00 AM - 8:00 PM</li>
                            <li><span>Saturday:</span> 10:00 AM - 4:00 PM</li>
                            <li><span>Sunday:</span> Closed</li>
                        {% endfor %}
                    </ul>
                </div>
                <div class="col-lg-3">
                    <h4>Newsletter</h4>
                    <p>Get latest tech updates</p>
                    <div class="newsletter-form">
                        <input type="email" placeholder="Your email">
                        <button><i class="fas fa-paper-plane"></i></button>
                    </div>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2024 Digital King Software House Rajanpur. All rights reserved.</p>
            </div>
        </div>
    </footer>
    {% endblock %}

    <!-- ==================== GLOBAL SCRIPTS ==================== -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    
    <script>
        AOS.init({
            duration: 800,
            once: true,
            offset: 100
        });

        window.addEventListener('scroll', function() {
            const navbar = document.getElementById('mainNav');
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });
    </script>
    
    {% block extra_js %}{% endblock %}
</body>
</html>'''

# Save to file
with open('/mnt/agents/output/base.html', 'w') as f:
    f.write(complete_base_html)

print("✅ Complete updated base.html saved!")
print(f"File size: {len(complete_base_html)} characters")
print("\n=== FEATURES ===")
print("1. Clean single CSS block - no duplicates")
print("2. Fixed: <nav> (not <<nav>)")
print("3. Full brand text on ALL screens")
print("4. Responsive font sizes")
print("5. Toggle button: mobile only")
print("6. Glassmorphism offcanvas sidebar")
print("7. Smooth Bootstrap 5 animation")
print("8. Icon + arrow for each nav link")
print("9. Active page highlighting")
print("10. Get Quote button at bottom")
