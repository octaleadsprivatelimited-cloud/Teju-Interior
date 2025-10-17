#!/usr/bin/env python3
"""
Fix Navigation Menus for All Pages
This script fixes navigation menus across all HTML pages to remove dead links.
"""

import os
import re

def fix_navigation_menu(content):
    """Fix navigation menu to remove dead links and keep only existing pages"""
    
    # Fix logo link to always point to index4.html
    content = re.sub(r'href="index\.html"', 'href="index4.html"', content)
    
    # Remove dead links from Home submenu
    patterns_to_remove = [
        r'<li>\s*<a href="index2\.html">\s*Home Page 2\s*</a>\s*</li>',
        r'<li>\s*<a href="index3\.html">\s*Home Page 3\s*</a>\s*</li>',
        r'<li>\s*<a href="index5\.html">\s*Home Page 5\s*</a>\s*</li>',
        r'<li>\s*<a href="index6\.html">\s*Home Page 6\s*</a>\s*</li>',
        
        # Remove dead links from Projects submenu
        r'<li>\s*<a href="project-2col-v1\.html">\s*Project 2 Column v1\s*</a>\s*</li>',
        r'<li>\s*<a href="project-2col-v2\.html">\s*Project 2 Column v2\s*</a>\s*</li>',
        r'<li>\s*<a href="project-3col-v1\.html">\s*Project 3 Column v1\s*</a>\s*</li>',
        r'<li>\s*<a href="project-3col-v2\.html">\s*Project 3 Column v2\s*</a>\s*</li>',
        r'<li>\s*<a href="project-4col-v1\.html">\s*Project 4 Column v1\s*</a>\s*</li>',
        
        # Remove dead links from Services submenu
        r'<li>\s*<a href="service-v1\.html">\s*Services v1\s*</a>\s*</li>',
        r'<li>\s*<a href="service-v2\.html">\s*Services v2\s*</a>\s*</li>',
        
        # Remove dead links from Pages submenu
        r'<li>\s*<a href="about-us\.html">\s*About Us\s*</a>\s*</li>',
        r'<li>\s*<a href="our-process\.html">\s*Our Process\s*</a>\s*</li>',
        r'<li>\s*<a href="testimonial\.html">\s*Testimonials\s*</a>\s*</li>',
        
        # Remove dead links from Blog submenu
        r'<li>\s*<a href="blog-2col\.html">\s*Blog 2 Column\s*</a>\s*</li>',
        r'<li>\s*<a href="blog-4col\.html">\s*Blog 4 Column\s*</a>\s*</li>',
        r'<li>\s*<a href="blog-detail\.html">\s*Blog Detail\s*</a>\s*</li>',
        r'<li>\s*<a href="blog-list\.html">\s*Blog List\s*</a>\s*</li>',
    ]
    
    for pattern in patterns_to_remove:
        content = re.sub(pattern, '', content)
    
    # Update main navigation links to point to existing pages
    content = re.sub(r'href="project-2col-v1\.html"', 'href="project-4col-v2.html"', content)
    content = re.sub(r'href="service-v1\.html"', 'href="service-list.html"', content)
    content = re.sub(r'href="blog-2col\.html"', 'href="blog-3col.html"', content)
    
    return content

def process_html_file(filepath):
    """Process a single HTML file to fix navigation"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Fix navigation menu
        content = fix_navigation_menu(content)
        
        # Write back to file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Updated: {filepath}")
        return True
        
    except Exception as e:
        print(f"❌ Error processing {filepath}: {str(e)}")
        return False

def main():
    """Main function to fix navigation on all pages"""
    print("🔧 Fixing navigation menus across all pages...")
    print("=" * 60)
    
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
    
    processed_count = 0
    for filepath in html_files:
        if os.path.exists(filepath):
            if process_html_file(filepath):
                processed_count += 1
        else:
            print(f"⚠️ File not found: {filepath}")
    
    print("=" * 60)
    print(f"📊 Summary:")
    print(f"✅ HTML files processed: {processed_count}/{len(html_files)}")
    print("\n🎉 Navigation menus fixed across all pages!")
    print("All dead links removed, only existing pages linked.")

if __name__ == "__main__":
    main()
