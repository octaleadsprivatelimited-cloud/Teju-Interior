#!/usr/bin/env python3
"""
Navigation Update Script for Teju Interior Website
This script updates all navigation menus to remove dead links and keep only the required pages.
"""

import os
import re

# Pages to keep
KEEP_PAGES = [
    'index4.html',           # Home Page 4
    'project-4col-v2.html',  # Project 4 v2
    'service-list.html',     # Services List
    'blog-3col.html',        # Blog 3 Column
    'portfolio-detail-v1.html', # Portfolio v1
    'about-us.html',         # About Us
    'testimonial.html',      # Testimonials
    'our-process.html',      # Our Process
    'contact.html'           # Contact
]

def update_navigation_in_file(filepath):
    """Update navigation menu in a single HTML file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update Home menu - remove submenu, keep only Home Page 4
        home_pattern = r'<li class="li-has-sub">\s*<a href="[^"]*">\s*Home\s*</a>\s*<ul class="sub-menu ul--no-style">.*?</ul>\s*</li>'
        home_replacement = '''<li>
              <a href="index4.html">
                Home
              </a>
            </li>'''
        content = re.sub(home_pattern, home_replacement, content, flags=re.DOTALL)
        
        # Update Projects menu - keep only Project 4 v2
        projects_pattern = r'<li class="li-has-sub">\s*<a href="[^"]*">\s*Projects\s*</a>\s*<ul class="sub-menu ul--no-style">.*?</ul>\s*</li>'
        projects_replacement = '''<li>
              <a href="project-4col-v2.html">
                Projects
              </a>
            </li>'''
        content = re.sub(projects_pattern, projects_replacement, content, flags=re.DOTALL)
        
        # Update Services menu - keep only Services List
        services_pattern = r'<li class="li-has-sub">\s*<a href="[^"]*">\s*Services\s*</a>\s*<ul class="sub-menu ul--no-style">.*?</ul>\s*</li>'
        services_replacement = '''<li>
              <a href="service-list.html">
                Services
              </a>
            </li>'''
        content = re.sub(services_pattern, services_replacement, content, flags=re.DOTALL)
        
        # Update Pages menu - keep only required pages
        pages_pattern = r'<li class="li-has-sub">\s*<a href="">\s*Pages\s*</a>\s*<ul class="sub-menu ul--no-style">.*?</ul>\s*</li>'
        pages_replacement = '''<li class="li-has-sub">
              <a href="">
                Pages
              </a>
              <ul class="sub-menu ul--no-style">
                <li>
                  <a href="portfolio-detail-v1.html">
                    Portfolio Detail v1
                  </a>
                </li>
                <li>
                  <a href="about-us.html">
                    About Us
                  </a>
                </li>
                <li>
                  <a href="testimonial.html">
                    Testimonial
                  </a>
                </li>
                <li>
                  <a href="our-process.html">
                    Our Process
                  </a>
                </li>
              </ul>
            </li>'''
        content = re.sub(pages_pattern, pages_replacement, content, flags=re.DOTALL)
        
        # Update Blog menu - keep only Blog 3 Column
        blog_pattern = r'<li class="li-has-sub">\s*<a href="[^"]*">\s*Blog\s*</a>\s*<ul class="sub-menu ul--no-style">.*?</ul>\s*</li>'
        blog_replacement = '''<li>
              <a href="blog-3col.html">
                Blog
              </a>
            </li>'''
        content = re.sub(blog_pattern, blog_replacement, content, flags=re.DOTALL)
        
        # Remove Shop menu entirely
        shop_pattern = r'<li class="li-has-sub">\s*<a href="[^"]*">\s*Shop\s*</a>\s*<ul class="sub-menu ul--no-style">.*?</ul>\s*</li>'
        content = re.sub(shop_pattern, '', content, flags=re.DOTALL)
        
        # Update Contact link
        content = re.sub(r'href="contact\.html"', 'href="contact.html"', content)
        
        # Update logo links to point to index4.html
        content = re.sub(r'href="index\.html"', 'href="index4.html"', content)
        
        # Write updated content back to file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Updated navigation in: {filepath}")
        return True
        
    except Exception as e:
        print(f"❌ Error updating {filepath}: {str(e)}")
        return False

def main():
    """Main function to update all navigation menus"""
    print("🔄 Updating navigation menus across all pages...")
    print("=" * 60)
    
    # Get all HTML files in the template directory
    template_dir = "Arch/HTML5_Template"
    html_files = [f for f in os.listdir(template_dir) if f.endswith('.html')]
    
    success_count = 0
    total_count = len(html_files)
    
    for html_file in html_files:
        filepath = os.path.join(template_dir, html_file)
        if update_navigation_in_file(filepath):
            success_count += 1
    
    print("=" * 60)
    print(f"📊 Navigation Update Summary:")
    print(f"✅ Successfully updated: {success_count}/{total_count} files")
    print("\n🎯 Navigation changes:")
    print("• Home: Simplified to single link (Home Page 4)")
    print("• Projects: Simplified to single link (Project 4 v2)")
    print("• Services: Simplified to single link (Services List)")
    print("• Pages: Kept only required pages (Portfolio, About, Testimonial, Process)")
    print("• Blog: Simplified to single link (Blog 3 Column)")
    print("• Shop: Removed entirely")
    print("• Contact: Kept as single link")
    print("\n🎉 Navigation cleanup completed!")

if __name__ == "__main__":
    main()
