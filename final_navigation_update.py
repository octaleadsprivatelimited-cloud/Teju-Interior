#!/usr/bin/env python3
"""
Final Navigation Update for All Pages
This script updates the remaining navigation menus with the new structure.
"""

import os
import re

def update_remaining_pages():
    """Update navigation menus for all remaining pages"""
    
    # List of files to update
    files_to_update = [
        "Arch/HTML5_Template/services.html",
        "Arch/HTML5_Template/blog.html", 
        "Arch/HTML5_Template/portfolio.html",
        "Arch/HTML5_Template/about-us.html",
        "Arch/HTML5_Template/testimonial.html",
        "Arch/HTML5_Template/our-process.html",
        "Arch/HTML5_Template/contact.html"
    ]
    
    # New navigation structure
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
    
    for filepath in files_to_update:
        if os.path.exists(filepath):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Update logo links
                content = re.sub(r'href="index4\.html"', 'href="home.html"', content)
                content = re.sub(r'href="index\.html"', 'href="home.html"', content)
                
                # Update other links
                content = re.sub(r'href="project-4col-v2\.html"', 'href="project.html"', content)
                content = re.sub(r'href="service-list\.html"', 'href="services.html"', content)
                content = re.sub(r'href="blog-3col\.html"', 'href="blog.html"', content)
                content = re.sub(r'href="portfolio-detail-v1\.html"', 'href="portfolio.html"', content)
                
                # Replace navigation section
                content = re.sub(
                    r'<nav class="menu-desktop pull-right">.*?</nav>',
                    new_navigation,
                    content,
                    flags=re.DOTALL
                )
                
                # Update titles
                if "services.html" in filepath:
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
                
            except Exception as e:
                print(f"❌ Error updating {filepath}: {str(e)}")
        else:
            print(f"⚠️ File not found: {filepath}")

if __name__ == "__main__":
    print("🔧 Updating remaining navigation menus...")
    print("=" * 50)
    update_remaining_pages()
    print("=" * 50)
    print("🎉 All navigation menus updated!")
    print("New structure implemented:")
    print("• Home (direct)")
    print("• Project (direct)")
    print("• Services (direct)")
    print("• Blog (direct)")
    print("• Pages dropdown: Portfolio, About Us, Testimonials, Our Process")
    print("• Contact (direct)")
