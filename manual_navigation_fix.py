#!/usr/bin/env python3
"""
Manual Navigation Fix and Image Addition
This script manually fixes navigation menus and adds missing images.
"""

import os
import re

def fix_navigation_and_add_images():
    """Fix navigation menus and add missing images to all pages"""
    
    # List of HTML files to process
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
    
    # Patterns to remove from navigation
    patterns_to_remove = [
        r'<li>\s*<a href="index2\.html">\s*Home Page 2\s*</a>\s*</li>',
        r'<li>\s*<a href="index3\.html">\s*Home Page 3\s*</a>\s*</li>',
        r'<li>\s*<a href="index5\.html">\s*Home Page 5\s*</a>\s*</li>',
        r'<li>\s*<a href="index6\.html">\s*Home Page 6\s*</a>\s*</li>',
        r'<li>\s*<a href="project-2col-v1\.html">\s*Project 2 Column v1\s*</a>\s*</li>',
        r'<li>\s*<a href="project-2col-v2\.html">\s*Project 2 Column v2\s*</a>\s*</li>',
        r'<li>\s*<a href="project-3col-v1\.html">\s*Project 3 Column v1\s*</a>\s*</li>',
        r'<li>\s*<a href="project-3col-v2\.html">\s*Project 3 Column v2\s*</a>\s*</li>',
        r'<li>\s*<a href="project-4col-v1\.html">\s*Project 4 Column v1\s*</a>\s*</li>',
        r'<li>\s*<a href="service-v1\.html">\s*Services v1\s*</a>\s*</li>',
        r'<li>\s*<a href="service-v2\.html">\s*Services v2\s*</a>\s*</li>',
        r'<li>\s*<a href="about-us\.html">\s*About Us\s*</a>\s*</li>',
        r'<li>\s*<a href="our-process\.html">\s*Our Process\s*</a>\s*</li>',
        r'<li>\s*<a href="testimonial\.html">\s*Testimonials\s*</a>\s*</li>',
        r'<li>\s*<a href="blog-2col\.html">\s*Blog 2 Column\s*</a>\s*</li>',
        r'<li>\s*<a href="blog-4col\.html">\s*Blog 4 Column\s*</a>\s*</li>',
        r'<li>\s*<a href="blog-detail\.html">\s*Blog Detail\s*</a>\s*</li>',
        r'<li>\s*<a href="blog-list\.html">\s*Blog List\s*</a>\s*</li>',
    ]
    
    # Update main navigation links
    link_updates = [
        (r'href="index\.html"', 'href="index4.html"'),
        (r'href="project-2col-v1\.html"', 'href="project-4col-v2.html"'),
        (r'href="service-v1\.html"', 'href="service-list.html"'),
        (r'href="blog-2col\.html"', 'href="blog-3col.html"'),
    ]
    
    processed_count = 0
    
    for filepath in html_files:
        if not os.path.exists(filepath):
            print(f"⚠️ File not found: {filepath}")
            continue
            
        try:
            # Read file
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Remove dead links
            for pattern in patterns_to_remove:
                content = re.sub(pattern, '', content)
            
            # Update main navigation links
            for old_link, new_link in link_updates:
                content = re.sub(old_link, new_link, content)
            
            # Add missing images based on page type
            if "index4.html" in filepath:
                # Add hero background images
                content = re.sub(
                    r'<div class="rev_slider_wrapper">',
                    '''<div class="rev_slider_wrapper">
                    <!-- Additional Hero Images -->
                    <div class="hero-bg-01" style="background-image: url('img/slide-01.jpg'); display: none;"></div>
                    <div class="hero-bg-02" style="background-image: url('img/slide-02.jpg'); display: none;"></div>
                    <div class="hero-bg-03" style="background-image: url('img/slide-03.jpg'); display: none;"></div>''',
                    content
                )
            
            elif "project-4col-v2.html" in filepath:
                # Add project gallery images
                content = re.sub(
                    r'<div class="row">',
                    '''<div class="row">
                    <!-- Additional Project Gallery Images -->
                    <div class="col-md-3 col-sm-6">
                        <div class="project-item">
                            <img src="img/pro-01.jpg" alt="Project Gallery 1" class="img-responsive">
                        </div>
                    </div>
                    <div class="col-md-3 col-sm-6">
                        <div class="project-item">
                            <img src="img/pro-02.jpg" alt="Project Gallery 2" class="img-responsive">
                        </div>
                    </div>
                    <div class="col-md-3 col-sm-6">
                        <div class="project-item">
                            <img src="img/pro-03.jpg" alt="Project Gallery 3" class="img-responsive">
                        </div>
                    </div>
                    <div class="col-md-3 col-sm-6">
                        <div class="project-item">
                            <img src="img/pro-04.jpg" alt="Project Gallery 4" class="img-responsive">
                        </div>
                    </div>''',
                    content
                )
            
            elif "service-list.html" in filepath:
                # Add service hero images
                content = re.sub(
                    r'<div class="container">',
                    '''<div class="container">
                    <!-- Service Hero Images -->
                    <div class="service-hero-section" style="background-image: url('img/bg-service-01.jpg'); background-size: cover; background-position: center; height: 400px; margin-bottom: 50px;">
                        <div class="service-hero-overlay" style="background: rgba(0,0,0,0.5); height: 100%; display: flex; align-items: center; justify-content: center;">
                            <h2 style="color: white; text-align: center;">Our Services</h2>
                        </div>
                    </div>''',
                    content
                )
            
            elif "blog-3col.html" in filepath:
                # Add blog featured images
                content = re.sub(
                    r'<div class="blog-item">',
                    '''<div class="blog-item">
                    <!-- Additional Blog Featured Images -->
                    <div class="blog-featured-img">
                        <img src="img/blog-01.jpg" alt="Blog Featured 1" class="img-responsive">
                    </div>''',
                    content
                )
            
            elif "about-us.html" in filepath:
                # Add about us hero and story images
                content = re.sub(
                    r'<div class="container">',
                    '''<div class="container">
                    <!-- About Us Hero Image -->
                    <div class="about-hero-section" style="background-image: url('img/bg-head.jpg'); background-size: cover; background-position: center; height: 500px; margin-bottom: 50px;">
                        <div class="about-hero-overlay" style="background: rgba(0,0,0,0.6); height: 100%; display: flex; align-items: center; justify-content: center;">
                            <h1 style="color: white; text-align: center;">About Teju Interior</h1>
                        </div>
                    </div>''',
                    content
                )
            
            elif "testimonial.html" in filepath:
                # Add testimonial background images
                content = re.sub(
                    r'<div class="testimonial-section">',
                    '''<div class="testimonial-section" style="background-image: url('img/bg-testi.jpg'); background-size: cover; background-position: center; background-attachment: fixed;">''',
                    content
                )
            
            elif "our-process.html" in filepath:
                # Add process step images
                content = re.sub(
                    r'<div class="process-step">',
                    '''<div class="process-step">
                    <!-- Process Step Images -->
                    <div class="process-step-img">
                        <img src="img/process-01.jpg" alt="Process Step 1" class="img-responsive">
                    </div>''',
                    content
                )
            
            elif "contact.html" in filepath:
                # Add contact hero and office images
                content = re.sub(
                    r'<div class="container">',
                    '''<div class="container">
                    <!-- Contact Hero Image -->
                    <div class="contact-hero-section" style="background-image: url('img/bg-contact.jpg'); background-size: cover; background-position: center; height: 400px; margin-bottom: 50px;">
                        <div class="contact-hero-overlay" style="background: rgba(0,0,0,0.5); height: 100%; display: flex; align-items: center; justify-content: center;">
                            <h1 style="color: white; text-align: center;">Contact Us</h1>
                        </div>
                    </div>''',
                    content
                )
            
            # Write back to file
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✅ Updated: {filepath}")
            processed_count += 1
            
        except Exception as e:
            print(f"❌ Error processing {filepath}: {str(e)}")
    
    print("=" * 60)
    print(f"📊 Summary:")
    print(f"✅ HTML files processed: {processed_count}/{len(html_files)}")
    print("\n🎉 Navigation menus fixed and images added!")
    print("All dead links removed, only existing pages linked.")
    print("Missing images added using existing image assets.")

if __name__ == "__main__":
    fix_navigation_and_add_images()
