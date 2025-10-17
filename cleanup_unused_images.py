#!/usr/bin/env python3
"""
Cleanup Unused Images Script for Teju Interior Website
This script identifies and removes unused images from the project.
"""

import os
import re
import glob

def get_used_images():
    """Get list of all images referenced in HTML files"""
    used_images = set()
    template_dir = "Arch/HTML5_Template"
    
    # Get all HTML files
    html_files = glob.glob(os.path.join(template_dir, "*.html"))
    
    for html_file in html_files:
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find all img src references
            img_pattern = r'src="img/([^"]+)"'
            matches = re.findall(img_pattern, content)
            used_images.update(matches)
            
            # Find all background-image references
            bg_pattern = r'background-image:\s*url\([\'"]?img/([^\'"]+)[\'"]?\)'
            bg_matches = re.findall(bg_pattern, content)
            used_images.update(bg_matches)
            
        except Exception as e:
            print(f"Error reading {html_file}: {e}")
    
    return used_images

def get_all_images():
    """Get list of all images in the img directory"""
    img_dir = "Arch/HTML5_Template/img"
    all_images = set()
    
    if os.path.exists(img_dir):
        for file in os.listdir(img_dir):
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.svg')):
                all_images.add(file)
    
    return all_images

def main():
    """Main function to clean up unused images"""
    print("🧹 Cleaning up unused images...")
    print("=" * 50)
    
    # Get used and all images
    used_images = get_used_images()
    all_images = get_all_images()
    
    # Find unused images
    unused_images = all_images - used_images
    
    print(f"📊 Image Analysis:")
    print(f"Total images in project: {len(all_images)}")
    print(f"Images currently used: {len(used_images)}")
    print(f"Unused images: {len(unused_images)}")
    
    if unused_images:
        print(f"\n🗑️  Unused images to remove:")
        for img in sorted(unused_images):
            print(f"  • {img}")
        
        # Remove unused images
        img_dir = "Arch/HTML5_Template/img"
        removed_count = 0
        
        for img in unused_images:
            img_path = os.path.join(img_dir, img)
            try:
                if os.path.exists(img_path):
                    os.remove(img_path)
                    removed_count += 1
                    print(f"✅ Removed: {img}")
            except Exception as e:
                print(f"❌ Error removing {img}: {e}")
        
        print(f"\n🎉 Cleanup Summary:")
        print(f"✅ Removed {removed_count} unused images")
        print(f"📁 Kept {len(used_images)} used images")
        
    else:
        print("\n✅ No unused images found - all images are being used!")
    
    print(f"\n📋 Used images:")
    for img in sorted(used_images):
        print(f"  • {img}")

if __name__ == "__main__":
    main()
