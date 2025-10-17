#!/usr/bin/env python3
"""
Script to update interior design website with high-quality images
This script provides URLs for free, high-quality interior design images
that can be downloaded and used to enhance the website.
"""

import os
import requests
from urllib.parse import urlparse

# High-quality interior design image URLs from Unsplash and Pexels
INTERIOR_IMAGES = {
    # Hero/Slider Images
    "slide-01.jpg": "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80",
    "slide-02.jpg": "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80",
    "slide-03.jpg": "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80",
    
    # Service Images
    "service-01.jpg": "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    "service-02.jpg": "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    "service-03.jpg": "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    
    # Project Images
    "latest-project-01.jpg": "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
    "latest-project-02.jpg": "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
    "latest-project-03.jpg": "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
    "latest-project-04.jpg": "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
    "latest-project-05.jpg": "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
    "latest-project-06.jpg": "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
    "latest-project-07.jpg": "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80",
    
    # Blog Images
    "blog-single-01.jpg": "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
    "blog-01.jpg": "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80",
    "blog-02.jpg": "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80",
    "blog-03.jpg": "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80",
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

def main():
    """Main function to download all images"""
    print("🎨 Starting image download for Teju Interior website...")
    print("=" * 50)
    
    success_count = 0
    total_count = len(INTERIOR_IMAGES)
    
    for filename, url in INTERIOR_IMAGES.items():
        if download_image(url, filename):
            success_count += 1
    
    print("=" * 50)
    print(f"📊 Download Summary:")
    print(f"✅ Successfully downloaded: {success_count}/{total_count} images")
    print(f"📁 Images saved to: Arch/HTML5_Template/img/")
    print("\n🎉 Image update completed!")
    print("\nNext steps:")
    print("1. Review the downloaded images")
    print("2. Test the website to ensure images load correctly")
    print("3. Commit and push changes to GitHub")

if __name__ == "__main__":
    main()
