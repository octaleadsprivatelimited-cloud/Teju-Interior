#!/usr/bin/env python3
"""
Project Restructuring Script for Teju Interior Website
This script restructures the project according to the new specifications.
"""

import os
import shutil
import re

def restructure_project():
    """Restructure the project according to new specifications"""
    
    print("🏗️ Restructuring Teju Interior Project...")
    print("=" * 60)
    
    # Step 1: Rename main pages
    print("📝 Step 1: Renaming main pages...")
    
    # Rename Home Page 4 to Home
    if os.path.exists("Arch/HTML5_Template/index4.html"):
        os.rename("Arch/HTML5_Template/index4.html", "Arch/HTML5_Template/home.html")
        print("✅ Renamed index4.html → home.html")
    
    # Rename Project 4 v2 to Project
    if os.path.exists("Arch/HTML5_Template/project-4col-v2.html"):
        os.rename("Arch/HTML5_Template/project-4col-v2.html", "Arch/HTML5_Template/project.html")
        print("✅ Renamed project-4col-v2.html → project.html")
    
    # Rename Services List to Services
    if os.path.exists("Arch/HTML5_Template/service-list.html"):
        os.rename("Arch/HTML5_Template/service-list.html", "Arch/HTML5_Template/services.html")
        print("✅ Renamed service-list.html → services.html")
    
    # Rename Blog 3 Column to Blog
    if os.path.exists("Arch/HTML5_Template/blog-3col.html"):
        os.rename("Arch/HTML5_Template/blog-3col.html", "Arch/HTML5_Template/blog.html")
        print("✅ Renamed blog-3col.html → blog.html")
    
    # Rename Portfolio v1 to Portfolio
    if os.path.exists("Arch/HTML5_Template/portfolio-detail-v1.html"):
        os.rename("Arch/HTML5_Template/portfolio-detail-v1.html", "Arch/HTML5_Template/portfolio.html")
        print("✅ Renamed portfolio-detail-v1.html → portfolio.html")
    
    print("\n📝 Step 2: Updating navigation menus...")
    
    # List of files to update
    html_files = [
        "Arch/HTML5_Template/home.html",
        "Arch/HTML5_Template/project.html",
        "Arch/HTML5_Template/services.html",
        "Arch/HTML5_Template/blog.html",
        "Arch/HTML5_Template/portfolio.html",
        "Arch/HTML5_Template/about-us.html",
        "Arch/HTML5_Template/testimonial.html",
        "Arch/HTML5_Template/our-process.html",
        "Arch/HTML5_Template/contact.html"
    ]
    
    for filepath in html_files:
        if os.path.exists(filepath):
            update_navigation_menu(filepath)
            print(f"✅ Updated navigation in {os.path.basename(filepath)}")
    
    print("\n📝 Step 3: Updating vercel.json...")
    update_vercel_config()
    
    print("\n📝 Step 4: Updating root index.html...")
    update_root_index()
    
    print("\n🎉 Project restructuring completed!")
    print("=" * 60)
    print("📊 Summary of changes:")
    print("✅ Home Page 4 → Home (main homepage)")
    print("✅ Project 4 v2 → Project")
    print("✅ Services List → Services")
    print("✅ Blog 3 Column → Blog")
    print("✅ Portfolio v1 → Portfolio")
    print("✅ Pages dropdown: Portfolio, About Us, Testimonials, Our Process")
    print("✅ Contact page maintained")
    print("✅ Navigation menus updated")
    print("✅ Vercel config updated")
    print("✅ Root index.html updated")

def update_navigation_menu(filepath):
    """Update navigation menu for a specific file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update logo link to home.html
        content = re.sub(r'href="index4\.html"', 'href="home.html"', content)
        content = re.sub(r'href="index\.html"', 'href="home.html"', content)
        
        # Update main navigation links
        content = re.sub(r'href="project-4col-v2\.html"', 'href="project.html"', content)
        content = re.sub(r'href="service-list\.html"', 'href="services.html"', content)
        content = re.sub(r'href="blog-3col\.html"', 'href="blog.html"', content)
        content = re.sub(r'href="portfolio-detail-v1\.html"', 'href="portfolio.html"', content)
        
        # Create new navigation structure
        new_navigation = '''<nav class="menu-desktop pull-right">
          <ul class="ul--inline ul--no-style">
            <li>
              <a href="home.html">
                Home
              </a>
            </li>
            <li>
              <a href="project.html">
                Project
              </a>
            </li>
            <li>
              <a href="services.html">
                Services
              </a>
            </li>
            <li>
              <a href="blog.html">
                Blog
              </a>
            </li>
            <li class="li-has-sub">
              <a href="">
                Pages
              </a>
              <ul class="sub-menu ul--no-style">
                <li>
                  <a href="portfolio.html">
                    Portfolio
                  </a>
                </li>
                <li>
                  <a href="about-us.html">
                    About Us
                  </a>
                </li>
                <li>
                  <a href="testimonial.html">
                    Testimonials
                  </a>
                </li>
                <li>
                  <a href="our-process.html">
                    Our Process
                  </a>
                </li>
              </ul>
            </li>
            <li>
              <a href="contact.html">
                Contact
              </a>
            </li>
          </ul>
        </nav>'''
        
        # Replace the entire navigation section
        content = re.sub(
            r'<nav class="menu-desktop pull-right">.*?</nav>',
            new_navigation,
            content,
            flags=re.DOTALL
        )
        
        # Write back to file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
    except Exception as e:
        print(f"❌ Error updating {filepath}: {str(e)}")

def update_vercel_config():
    """Update vercel.json to point to new home.html"""
    vercel_config = '''{
  "version": 2,
  "builds": [
    {
      "src": "Arch/HTML5_Template/**/*",
      "use": "@vercel/static"
    }
  ],
  "routes": [
    {
      "src": "/",
      "dest": "/Arch/HTML5_Template/home.html"
    },
    {
      "src": "/css/(.*)",
      "dest": "/Arch/HTML5_Template/css/$1"
    },
    {
      "src": "/js/(.*)",
      "dest": "/Arch/HTML5_Template/js/$1"
    },
    {
      "src": "/img/(.*)",
      "dest": "/Arch/HTML5_Template/img/$1"
    },
    {
      "src": "/font/(.*)",
      "dest": "/Arch/HTML5_Template/font/$1"
    },
    {
      "src": "/vendor/(.*)",
      "dest": "/Arch/HTML5_Template/vendor/$1"
    },
    {
      "src": "/(.*\\.html)",
      "dest": "/Arch/HTML5_Template/$1"
    }
  ]
}'''
    
    with open("vercel.json", 'w') as f:
        f.write(vercel_config)
    print("✅ Updated vercel.json to point to home.html")

def update_root_index():
    """Update root index.html to redirect to home.html"""
    root_index = '''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="refresh" content="0; url=Arch/HTML5_Template/home.html">
    <title>Teju Interior - Redirecting...</title>
</head>
<body>
    <p>Redirecting to Teju Interior website...</p>
    <script>
        window.location.href = "Arch/HTML5_Template/home.html";
    </script>
</body>
</html>'''
    
    with open("index.html", 'w') as f:
        f.write(root_index)
    print("✅ Updated root index.html to redirect to home.html")

if __name__ == "__main__":
    restructure_project()
