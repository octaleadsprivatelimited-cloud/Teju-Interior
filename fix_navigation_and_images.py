#!/usr/bin/env python3
"""
Fix Navigation Menus and Add Missing Images for Teju Interior Website
This script fixes all navigation menus and adds missing images to all pages.
"""

import os
import re
import requests
from urllib.parse import urlparse

# Pages that exist and should be linked
EXISTING_PAGES = {
    'index4.html': 'Home Page 4',
    'project-4col-v2.html': 'Project 4 v2', 
    'service-list.html': 'Services List',
    'blog-3col.html': 'Blog 3 Column',
    'portfolio-detail-v1.html': 'Portfolio v1',
    'about-us.html': 'About Us',
    'testimonial.html': 'Testimonials',
    'our-process.html': 'Our Process',
    'contact.html': 'Contact'
}

# High-quality interior design images for different sections
ADDITIONAL_IMAGES = {
    # Hero/Slider Images for Home Page 4
    "hero-bg-01.jpg": "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80",
    "hero-bg-02.jpg": "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80",
    "hero-bg-03.jpg": "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80",
    
    # Service Section Images
    "service-hero-01.jpg": "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
    "service-hero-02.jpg": "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
    
    # Project Gallery Images
    "project-gallery-01.jpg": "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    "project-gallery-02.jpg": "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    "project-gallery-03.jpg": "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    "project-gallery-04.jpg": "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    "project-gallery-05.jpg": "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    "project-gallery-06.jpg": "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    "project-gallery-07.jpg": "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    "project-gallery-08.jpg": "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    
    # Blog Images
    "blog-featured-01.jpg": "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
    "blog-featured-02.jpg": "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
    "blog-featured-03.jpg": "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
    "blog-featured-04.jpg": "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
    "blog-featured-05.jpg": "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
    "blog-featured-06.jpg": "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
    "blog-featured-07.jpg": "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
    "blog-featured-08.jpg": "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
    "blog-featured-09.jpg": "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
    
    # Portfolio Detail Images
    "portfolio-detail-01.jpg": "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
    "portfolio-detail-02.jpg": "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
    "portfolio-detail-03.jpg": "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
    "portfolio-detail-04.jpg": "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
    "portfolio-detail-05.jpg": "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
    "portfolio-detail-06.jpg": "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80",
    
    # About Us Section Images
    "about-hero.jpg": "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80",
    "about-story-01.jpg": "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    "about-story-02.jpg": "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    "about-story-03.jpg": "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    
    # Testimonial Background Images
    "testimonial-bg-01.jpg": "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80",
    "testimonial-bg-02.jpg": "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80",
    
    # Process Section Images
    "process-step-01.jpg": "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
    "process-step-02.jpg": "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
    "process-step-03.jpg": "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
    "process-step-04.jpg": "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
    "process-step-05.jpg": "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
    "process-step-06.jpg": "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
    
    # Contact Page Images
    "contact-hero.jpg": "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80",
    "contact-office-01.jpg": "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    "contact-office-02.jpg": "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
}

def download_image(url, filename, img_dir="Arch/HTML5_Template/img"):
    """Download an image from URL and save it to the specified directory"""
    try:
        # Create directory if it doesn't exist
        os.makedirs(img_dir, exist_ok=True)
        
        # Download the image
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        # Save the image
        filepath = os.path.join(img_dir, filename)
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        print(f"✅ Downloaded: {filename}")
        return True
        
    except Exception as e:
        print(f"❌ Error downloading {filename}: {str(e)}")
        return False

def fix_navigation_menu(content, current_page):
    """Fix navigation menu to remove dead links and keep only existing pages"""
    
    # Fix logo link to always point to index4.html
    content = re.sub(r'href="index\.html"', 'href="index4.html"', content)
    
    # Remove dead links from Home submenu
    home_submenu_pattern = r'<li>\s*<a href="index2\.html">\s*Home Page 2\s*</a>\s*</li>'
    content = re.sub(home_submenu_pattern, '', content)
    
    home_submenu_pattern = r'<li>\s*<a href="index3\.html">\s*Home Page 3\s*</a>\s*</li>'
    content = re.sub(home_submenu_pattern, '', content)
    
    home_submenu_pattern = r'<li>\s*<a href="index5\.html">\s*Home Page 5\s*</a>\s*</li>'
    content = re.sub(home_submenu_pattern, '', content)
    
    home_submenu_pattern = r'<li>\s*<a href="index6\.html">\s*Home Page 6\s*</a>\s*</li>'
    content = re.sub(home_submenu_pattern, '', content)
    
    # Remove dead links from Projects submenu
    project_patterns = [
        r'<li>\s*<a href="project-2col-v1\.html">\s*Project 2 Column v1\s*</a>\s*</li>',
        r'<li>\s*<a href="project-2col-v2\.html">\s*Project 2 Column v2\s*</a>\s*</li>',
        r'<li>\s*<a href="project-3col-v1\.html">\s*Project 3 Column v1\s*</a>\s*</li>',
        r'<li>\s*<a href="project-3col-v2\.html">\s*Project 3 Column v2\s*</a>\s*</li>',
        r'<li>\s*<a href="project-4col-v1\.html">\s*Project 4 Column v1\s*</a>\s*</li>',
    ]
    
    for pattern in project_patterns:
        content = re.sub(pattern, '', content)
    
    # Remove dead links from Services submenu
    service_patterns = [
        r'<li>\s*<a href="service-v1\.html">\s*Services v1\s*</a>\s*</li>',
        r'<li>\s*<a href="service-v2\.html">\s*Services v2\s*</a>\s*</li>',
    ]
    
    for pattern in service_patterns:
        content = re.sub(pattern, '', content)
    
    # Remove dead links from Pages submenu
    page_patterns = [
        r'<li>\s*<a href="about-us\.html">\s*About Us\s*</a>\s*</li>',
        r'<li>\s*<a href="our-process\.html">\s*Our Process\s*</a>\s*</li>',
        r'<li>\s*<a href="testimonial\.html">\s*Testimonials\s*</a>\s*</li>',
    ]
    
    for pattern in page_patterns:
        content = re.sub(pattern, '', content)
    
    # Remove dead links from Blog submenu
    blog_patterns = [
        r'<li>\s*<a href="blog-2col\.html">\s*Blog 2 Column\s*</a>\s*</li>',
        r'<li>\s*<a href="blog-4col\.html">\s*Blog 4 Column\s*</a>\s*</li>',
        r'<li>\s*<a href="blog-detail\.html">\s*Blog Detail\s*</a>\s*</li>',
        r'<li>\s*<a href="blog-list\.html">\s*Blog List\s*</a>\s*</li>',
    ]
    
    for pattern in blog_patterns:
        content = re.sub(pattern, '', content)
    
    # Update main navigation links to point to existing pages
    content = re.sub(r'href="project-2col-v1\.html"', 'href="project-4col-v2.html"', content)
    content = re.sub(r'href="service-v1\.html"', 'href="service-list.html"', content)
    content = re.sub(r'href="blog-2col\.html"', 'href="blog-3col.html"', content)
    
    return content

def add_missing_images_to_page(content, page_name):
    """Add missing images to specific pages based on their content"""
    
    if "index4.html" in page_name:
        # Add hero background images
        content = re.sub(
            r'<div class="rev_slider_wrapper">',
            '''<div class="rev_slider_wrapper">
            <!-- Additional Hero Images -->
            <div class="hero-bg-01" style="background-image: url('img/hero-bg-01.jpg'); display: none;"></div>
            <div class="hero-bg-02" style="background-image: url('img/hero-bg-02.jpg'); display: none;"></div>
            <div class="hero-bg-03" style="background-image: url('img/hero-bg-03.jpg'); display: none;"></div>''',
            content
        )
    
    elif "project-4col-v2.html" in page_name:
        # Add project gallery images
        content = re.sub(
            r'<div class="row">',
            '''<div class="row">
            <!-- Additional Project Gallery Images -->
            <div class="col-md-3 col-sm-6">
                <div class="project-item">
                    <img src="img/project-gallery-01.jpg" alt="Project Gallery 1" class="img-responsive">
                </div>
            </div>
            <div class="col-md-3 col-sm-6">
                <div class="project-item">
                    <img src="img/project-gallery-02.jpg" alt="Project Gallery 2" class="img-responsive">
                </div>
            </div>
            <div class="col-md-3 col-sm-6">
                <div class="project-item">
                    <img src="img/project-gallery-03.jpg" alt="Project Gallery 3" class="img-responsive">
                </div>
            </div>
            <div class="col-md-3 col-sm-6">
                <div class="project-item">
                    <img src="img/project-gallery-04.jpg" alt="Project Gallery 4" class="img-responsive">
                </div>
            </div>''',
            content
        )
    
    elif "service-list.html" in page_name:
        # Add service hero images
        content = re.sub(
            r'<div class="container">',
            '''<div class="container">
            <!-- Service Hero Images -->
            <div class="service-hero-section" style="background-image: url('img/service-hero-01.jpg'); background-size: cover; background-position: center; height: 400px; margin-bottom: 50px;">
                <div class="service-hero-overlay" style="background: rgba(0,0,0,0.5); height: 100%; display: flex; align-items: center; justify-content: center;">
                    <h2 style="color: white; text-align: center;">Our Services</h2>
                </div>
            </div>''',
            content
        )
    
    elif "blog-3col.html" in page_name:
        # Add blog featured images
        content = re.sub(
            r'<div class="blog-item">',
            '''<div class="blog-item">
            <!-- Additional Blog Featured Images -->
            <div class="blog-featured-img">
                <img src="img/blog-featured-01.jpg" alt="Blog Featured 1" class="img-responsive">
            </div>''',
            content
        )
    
    elif "about-us.html" in page_name:
        # Add about us hero and story images
        content = re.sub(
            r'<div class="container">',
            '''<div class="container">
            <!-- About Us Hero Image -->
            <div class="about-hero-section" style="background-image: url('img/about-hero.jpg'); background-size: cover; background-position: center; height: 500px; margin-bottom: 50px;">
                <div class="about-hero-overlay" style="background: rgba(0,0,0,0.6); height: 100%; display: flex; align-items: center; justify-content: center;">
                    <h1 style="color: white; text-align: center;">About Teju Interior</h1>
                </div>
            </div>''',
            content
        )
    
    elif "testimonial.html" in page_name:
        # Add testimonial background images
        content = re.sub(
            r'<div class="testimonial-section">',
            '''<div class="testimonial-section" style="background-image: url('img/testimonial-bg-01.jpg'); background-size: cover; background-position: center; background-attachment: fixed;">''',
            content
        )
    
    elif "our-process.html" in page_name:
        # Add process step images
        content = re.sub(
            r'<div class="process-step">',
            '''<div class="process-step">
            <!-- Process Step Images -->
            <div class="process-step-img">
                <img src="img/process-step-01.jpg" alt="Process Step 1" class="img-responsive">
            </div>''',
            content
        )
    
    elif "contact.html" in page_name:
        # Add contact hero and office images
        content = re.sub(
            r'<div class="container">',
            '''<div class="container">
            <!-- Contact Hero Image -->
            <div class="contact-hero-section" style="background-image: url('img/contact-hero.jpg'); background-size: cover; background-position: center; height: 400px; margin-bottom: 50px;">
                <div class="contact-hero-overlay" style="background: rgba(0,0,0,0.5); height: 100%; display: flex; align-items: center; justify-content: center;">
                    <h1 style="color: white; text-align: center;">Contact Us</h1>
                </div>
            </div>''',
            content
        )
    
    return content

def process_html_file(filepath):
    """Process a single HTML file to fix navigation and add images"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Fix navigation menu
        content = fix_navigation_menu(content, filepath)
        
        # Add missing images
        content = add_missing_images_to_page(content, filepath)
        
        # Write back to file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Updated: {filepath}")
        return True
        
    except Exception as e:
        print(f"❌ Error processing {filepath}: {str(e)}")
        return False

def main():
    """Main function to fix navigation and add images"""
    print("🔧 Fixing navigation menus and adding missing images...")
    print("=" * 60)
    
    # Download additional images
    print("📥 Downloading additional images...")
    success_count = 0
    total_count = len(ADDITIONAL_IMAGES)
    
    for filename, url in ADDITIONAL_IMAGES.items():
        if download_image(url, filename):
            success_count += 1
    
    print(f"✅ Downloaded {success_count}/{total_count} images")
    print()
    
    # Process HTML files
    print("🔧 Fixing navigation menus and adding images...")
    html_files = [
        "Arch/HTML5_Template/index4.html",
        "Arch/HTML5_Template/project-4col-v2.html", 
        "Arch/HTML5_Template/service-list.html",
        "Arch/HTML5_Template/blog-3col.html",
        "Arch/HTML5_Template/portfolio-detail-v1.html",
        "Arch/HTML5_Template/about-us.html",
        "Arch/HTML5_Template/testimonial.html",
        "Arch/HTML5_Template/our-process.html",
        "Arch/HTML5_Template/contact.html"
    ]
    
    processed_count = 0
    for filepath in html_files:
        if os.path.exists(filepath):
            if process_html_file(filepath):
                processed_count += 1
        else:
            print(f"⚠️ File not found: {filepath}")
    
    print("=" * 60)
    print(f"📊 Summary:")
    print(f"✅ Images downloaded: {success_count}/{total_count}")
    print(f"✅ HTML files processed: {processed_count}/{len(html_files)}")
    print("\n🎉 Navigation menus fixed and images added!")
    print("Next steps:")
    print("1. Test all navigation links")
    print("2. Verify responsive layout")
    print("3. Commit and push changes")

if __name__ == "__main__":
    main()
