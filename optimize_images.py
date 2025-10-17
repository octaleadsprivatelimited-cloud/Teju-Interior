#!/usr/bin/env python3
"""
Image optimization script to convert JPG images to WebP format
and update HTML references accordingly.
"""

import os
import glob
from PIL import Image
import re

def convert_to_webp(input_path, output_path, quality=85):
    """Convert image to WebP format with specified quality."""
    try:
        with Image.open(input_path) as img:
            # Convert to RGB if necessary (WebP doesn't support RGBA)
            if img.mode in ('RGBA', 'LA'):
                # Create white background for transparent images
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'RGBA':
                    background.paste(img, mask=img.split()[-1])
                else:
                    background.paste(img)
                img = background
            elif img.mode != 'RGB':
                img = img.convert('RGB')
            
            img.save(output_path, 'WebP', quality=quality, optimize=True)
            return True
    except Exception as e:
        print(f"Error converting {input_path}: {e}")
        return False

def update_html_references(html_file, old_ext, new_ext):
    """Update image references in HTML files."""
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace image references
        pattern = rf'src="img/([^"]+)\.{old_ext}"'
        replacement = rf'src="img/\1.{new_ext}"'
        updated_content = re.sub(pattern, replacement, content)
        
        # Also update data-background and href attributes
        pattern2 = rf'(data-background|href)="img/([^"]+)\.{old_ext}"'
        replacement2 = rf'\1="img/\2.{new_ext}"'
        updated_content = re.sub(pattern2, replacement2, updated_content)
        
        if content != updated_content:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f"Updated references in {html_file}")
            return True
        return False
    except Exception as e:
        print(f"Error updating {html_file}: {e}")
        return False

def main():
    """Main optimization function."""
    img_dir = "Arch/HTML5_Template/img"
    html_files = [
        "Arch/HTML5_Template/home.html",
        "Arch/HTML5_Template/services.html", 
        "Arch/HTML5_Template/project.html",
        "Arch/HTML5_Template/portfolio.html",
        "Arch/HTML5_Template/blog.html",
        "Arch/HTML5_Template/testimonial.html",
        "Arch/HTML5_Template/our-process.html",
        "Arch/HTML5_Template/about-us.html",
        "Arch/HTML5_Template/contact.html"
    ]
    
    # Get all JPG files
    jpg_files = glob.glob(os.path.join(img_dir, "*.jpg"))
    
    print(f"Found {len(jpg_files)} JPG files to optimize")
    
    converted_count = 0
    updated_html_count = 0
    
    # Convert images to WebP
    for jpg_file in jpg_files:
        webp_file = jpg_file.replace('.jpg', '.webp')
        
        # Skip if WebP already exists and is newer
        if os.path.exists(webp_file) and os.path.getmtime(webp_file) > os.path.getmtime(jpg_file):
            print(f"WebP already exists and is newer: {os.path.basename(webp_file)}")
            continue
            
        print(f"Converting {os.path.basename(jpg_file)} to WebP...")
        if convert_to_webp(jpg_file, webp_file, quality=85):
            converted_count += 1
            print(f"✓ Converted {os.path.basename(jpg_file)}")
        else:
            print(f"✗ Failed to convert {os.path.basename(jpg_file)}")
    
    # Update HTML references
    print("\nUpdating HTML references...")
    for html_file in html_files:
        if os.path.exists(html_file):
            if update_html_references(html_file, 'jpg', 'webp'):
                updated_html_count += 1
    
    print(f"\nOptimization complete!")
    print(f"Converted {converted_count} images to WebP")
    print(f"Updated {updated_html_count} HTML files")

if __name__ == "__main__":
    main()
