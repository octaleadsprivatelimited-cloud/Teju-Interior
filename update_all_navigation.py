#!/usr/bin/env python3
"""
Update Navigation Menus for All Pages
This script updates navigation menus across all HTML pages with the new structure.
"""

import os
import re

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
        
        # Update page titles
        if "home.html" in filepath:
            content = re.sub(r'<title>.*?</title>', '<title>Teju Interior - Home</title>', content)
        elif "project.html" in filepath:
            content = re.sub(r'<title>.*?</title>', '<title>Teju Interior - Project</title>', content)
        elif "services.html" in filepath:
            content = re.sub(r'<title>.*?</title>', '<title>Teju Interior - Services</title>', content)
        elif "blog.html" in filepath:
            content = re.sub(r'<title>.*?</title>', '<title>Teju Interior - Blog</title>', content)
        elif "portfolio.html" in filepath:
            content = re.sub(r'<title>.*?</title>', '<title>Teju Interior - Portfolio</title>', content)
        elif "about-us.html" in filepath:
            content = re.sub(r'<title>.*?</title>', '<title>Teju Interior - About Us</title>', content)
        elif "testimonial.html" in filepath:
            content = re.sub(r'<title>.*?</title>', '<title>Teju Interior - Testimonials</title>', content)
        elif "our-process.html" in filepath:
            content = re.sub(r'<title>.*?</title>', '<title>Teju Interior - Our Process</title>', content)
        elif "contact.html" in filepath:
            content = re.sub(r'<title>.*?</title>', '<title>Teju Interior - Contact</title>', content)
        
        # Write back to file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Updated: {filepath}")
        return True
        
    except Exception as e:
        print(f"❌ Error updating {filepath}: {str(e)}")
        return False

def main():
    """Main function to update navigation on all pages"""
    print("🔧 Updating navigation menus across all pages...")
    print("=" * 60)
    
    # List of HTML files to process
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
    
    processed_count = 0
    for filepath in html_files:
        if os.path.exists(filepath):
            if update_navigation_menu(filepath):
                processed_count += 1
        else:
            print(f"⚠️ File not found: {filepath}")
    
    print("=" * 60)
    print(f"📊 Summary:")
    print(f"✅ HTML files processed: {processed_count}/{len(html_files)}")
    print("\n🎉 Navigation menus updated across all pages!")
    print("New structure:")
    print("• Home (direct link)")
    print("• Project (direct link)")
    print("• Services (direct link)")
    print("• Blog (direct link)")
    print("• Pages dropdown: Portfolio, About Us, Testimonials, Our Process")
    print("• Contact (direct link)")

if __name__ == "__main__":
    main()
