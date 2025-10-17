#!/usr/bin/env python3
"""
Script to update navigation menus in all HTML pages
"""

import os
import re
from pathlib import Path

# Define the consistent navigation structure
CONSISTENT_NAV = '''        <nav class="menu-desktop pull-right">
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
              <a href="portfolio.html">
                Portfolio
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

CONSISTENT_MOBILE_NAV = '''        <nav class="menu-mobile hidden">
          <ul class="ul--no-style">
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
              <a href="portfolio.html">
                Portfolio
              </a>
            </li>
            <li>
              <a href="blog.html">
                Blog
              </a>
            </li>
            <li>
              <i class="fa fa-plus menu-mobile__more"></i>
              <a href="">
                Pages
              </a>
              <ul class="ul--no-style hidden">
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

CONSISTENT_DESKTOP_NAV = '''        <nav class="menu-desktop menu-desktop--show pull-right">
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
              <a href="portfolio.html">
                Portfolio
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

CONSISTENT_FOOTER_LINKS = '''              <ul class="ul--inline ul--footer">
                <li>
                  <a href="services.html">Services</a>
                </li>
                <li>
                  <a href="portfolio.html">Portfolio</a>
                </li>
                <li>
                  <a href="blog.html">Blog</a>
                </li>
                <li>
                  <a href="about-us.html">About Us</a>
                </li>
                <li>
                  <a href="contact.html">Contact</a>
                </li>
              </ul>'''

def update_navigation_in_file(file_path):
    """Update navigation in a single HTML file"""
    print(f"Updating navigation in {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update logo links
    content = re.sub(r'href="index4\.html"', 'href="home.html"', content)
    
    # Update header stick navigation
    header_stick_pattern = r'<nav class="menu-desktop pull-right">.*?</nav>'
    content = re.sub(header_stick_pattern, CONSISTENT_NAV, content, flags=re.DOTALL)
    
    # Update mobile navigation
    mobile_nav_pattern = r'<nav class="menu-mobile hidden">.*?</nav>'
    content = re.sub(mobile_nav_pattern, CONSISTENT_MOBILE_NAV, content, flags=re.DOTALL)
    
    # Update desktop navigation
    desktop_nav_pattern = r'<nav class="menu-desktop menu-desktop--show pull-right">.*?</nav>'
    content = re.sub(desktop_nav_pattern, CONSISTENT_DESKTOP_NAV, content, flags=re.DOTALL)
    
    # Update footer links
    footer_pattern = r'<ul class="ul--inline ul--footer">.*?</ul>'
    content = re.sub(footer_pattern, CONSISTENT_FOOTER_LINKS, content, flags=re.DOTALL)
    
    # Update breadcrumb links
    content = re.sub(r'href="index4\.html"', 'href="home.html"', content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated {file_path}")

def main():
    """Main function to update all HTML files"""
    template_dir = Path("Arch/HTML5_Template")
    
    if not template_dir.exists():
        print("Template directory not found!")
        return
    
    html_files = list(template_dir.glob("*.html"))
    
    if not html_files:
        print("No HTML files found!")
        return
    
    print(f"Found {len(html_files)} HTML files to update")
    
    for html_file in html_files:
        try:
            update_navigation_in_file(html_file)
        except Exception as e:
            print(f"Error updating {html_file}: {e}")
    
    print("Navigation update completed!")

if __name__ == "__main__":
    main()