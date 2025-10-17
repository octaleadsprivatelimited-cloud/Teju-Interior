@echo off
echo Downloading high-quality interior design images for Teju Interior website...
echo.

REM Create img directory if it doesn't exist
if not exist "Arch\HTML5_Template\img" mkdir "Arch\HTML5_Template\img"

echo Downloading hero/slider images...
curl -L "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80" -o "Arch\HTML5_Template\img\slide-01.jpg"
curl -L "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80" -o "Arch\HTML5_Template\img\slide-02.jpg"
curl -L "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80" -o "Arch\HTML5_Template\img\slide-03.jpg"

echo Downloading service images...
curl -L "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" -o "Arch\HTML5_Template\img\service-01.jpg"
curl -L "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" -o "Arch\HTML5_Template\img\service-02.jpg"
curl -L "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" -o "Arch\HTML5_Template\img\service-03.jpg"

echo Downloading project gallery images...
curl -L "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" -o "Arch\HTML5_Template\img\latest-project-01.jpg"
curl -L "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" -o "Arch\HTML5_Template\img\latest-project-02.jpg"
curl -L "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" -o "Arch\HTML5_Template\img\latest-project-03.jpg"
curl -L "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" -o "Arch\HTML5_Template\img\latest-project-04.jpg"
curl -L "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" -o "Arch\HTML5_Template\img\latest-project-05.jpg"
curl -L "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" -o "Arch\HTML5_Template\img\latest-project-06.jpg"
curl -L "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" -o "Arch\HTML5_Template\img\latest-project-07.jpg"

echo Downloading blog images...
curl -L "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" -o "Arch\HTML5_Template\img\blog-single-01.jpg"
curl -L "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80" -o "Arch\HTML5_Template\img\blog-01.jpg"
curl -L "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80" -o "Arch\HTML5_Template\img\blog-02.jpg"
curl -L "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80" -o "Arch\HTML5_Template\img\blog-03.jpg"

echo.
echo ✅ Image download completed!
echo 📁 Images saved to: Arch\HTML5_Template\img\
echo.
echo Next steps:
echo 1. Test the website to ensure images load correctly
echo 2. Commit and push changes to GitHub
echo 3. Deploy to Vercel
echo.
pause
