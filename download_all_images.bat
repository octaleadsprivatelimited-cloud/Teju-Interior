@echo off
echo Downloading comprehensive image collection for Teju Interior website...
echo This will update images across ALL pages in the project.
echo.

REM Create img directory if it doesn't exist
if not exist "Arch\HTML5_Template\img" mkdir "Arch\HTML5_Template\img"

echo ===============================================
echo Downloading About Us page images...
echo ===============================================
curl -L "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" -o "Arch\HTML5_Template\img\we-are-01.jpg"
curl -L "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" -o "Arch\HTML5_Template\img\we-are-02.jpg"
curl -L "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" -o "Arch\HTML5_Template\img\we-are-03.jpg"
curl -L "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" -o "Arch\HTML5_Template\img\we-are-04.jpg"
curl -L "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" -o "Arch\HTML5_Template\img\we-are-05.jpg"
curl -L "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" -o "Arch\HTML5_Template\img\we-are-06.jpg"

echo ===============================================
echo Downloading Team member photos...
echo ===============================================
curl -L "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80" -o "Arch\HTML5_Template\img\our-team-01.jpg"
curl -L "https://images.unsplash.com/photo-1494790108755-2616b612b786?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80" -o "Arch\HTML5_Template\img\our-team-02.jpg"
curl -L "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80" -o "Arch\HTML5_Template\img\our-team-03.jpg"
curl -L "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80" -o "Arch\HTML5_Template\img\our-team-04.jpg"
curl -L "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80" -o "Arch\HTML5_Template\img\our-team-05.jpg"
curl -L "https://images.unsplash.com/photo-1544005313-94ddf0286df2?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80" -o "Arch\HTML5_Template\img\our-team-06.jpg"
curl -L "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80" -o "Arch\HTML5_Template\img\our-team-07.jpg"
curl -L "https://images.unsplash.com/photo-1494790108755-2616b612b786?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80" -o "Arch\HTML5_Template\img\our-team-08.jpg"
curl -L "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80" -o "Arch\HTML5_Template\img\our-team-09.jpg"
curl -L "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80" -o "Arch\HTML5_Template\img\our-team-10.jpg"
curl -L "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80" -o "Arch\HTML5_Template\img\our-team-11.jpg"
curl -L "https://images.unsplash.com/photo-1544005313-94ddf0286df2?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80" -o "Arch\HTML5_Template\img\our-team-12.jpg"
curl -L "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixlib=rb-4.0.3&auto=format&fit=crop&w=400&q=80" -o "Arch\HTML5_Template\img\our-team-13.jpg"

echo ===============================================
echo Downloading Testimonial images...
echo ===============================================
curl -L "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80" -o "Arch\HTML5_Template\img\testi-01.jpg"
curl -L "https://images.unsplash.com/photo-1494790108755-2616b612b786?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80" -o "Arch\HTML5_Template\img\testi-02.jpg"
curl -L "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80" -o "Arch\HTML5_Template\img\testi-03.jpg"
curl -L "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80" -o "Arch\HTML5_Template\img\testi-04.jpg"
curl -L "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80" -o "Arch\HTML5_Template\img\testi-05.jpg"
curl -L "https://images.unsplash.com/photo-1544005313-94ddf0286df2?ixlib=rb-4.0.3&auto=format&fit=crop&w=200&q=80" -o "Arch\HTML5_Template\img\testi-06.jpg"

echo ===============================================
echo Downloading Service images...
echo ===============================================
curl -L "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" -o "Arch\HTML5_Template\img\service-01.jpg"
curl -L "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" -o "Arch\HTML5_Template\img\service-02.jpg"
curl -L "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" -o "Arch\HTML5_Template\img\service-03.jpg"
curl -L "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" -o "Arch\HTML5_Template\img\service-04.jpg"
curl -L "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" -o "Arch\HTML5_Template\img\service-05.jpg"
curl -L "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" -o "Arch\HTML5_Template\img\service-06.jpg"

echo ===============================================
echo Downloading Process images...
echo ===============================================
curl -L "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" -o "Arch\HTML5_Template\img\process-01.jpg"
curl -L "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" -o "Arch\HTML5_Template\img\process-02.jpg"
curl -L "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" -o "Arch\HTML5_Template\img\process-03.jpg"
curl -L "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" -o "Arch\HTML5_Template\img\process-04.jpg"
curl -L "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" -o "Arch\HTML5_Template\img\process-05.jpg"
curl -L "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" -o "Arch\HTML5_Template\img\process-06.jpg"
curl -L "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" -o "Arch\HTML5_Template\img\process-07.jpg"
curl -L "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" -o "Arch\HTML5_Template\img\process-08.jpg"

echo ===============================================
echo Downloading Contact page images...
echo ===============================================
curl -L "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80" -o "Arch\HTML5_Template\img\bg-contact.jpg"
curl -L "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80" -o "Arch\HTML5_Template\img\bg-contact-02.jpg"

echo ===============================================
echo Downloading Menu canvas images...
echo ===============================================
curl -L "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" -o "Arch\HTML5_Template\img\item-menu-canvas-01.jpg"
curl -L "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" -o "Arch\HTML5_Template\img\item-menu-canvas-02.jpg"

echo ===============================================
echo Downloading Cart item images...
echo ===============================================
curl -L "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=300&q=80" -o "Arch\HTML5_Template\img\cart-item-01.jpg"
curl -L "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=300&q=80" -o "Arch\HTML5_Template\img\cart-item-02.jpg"

echo ===============================================
echo Downloading Recent project images...
echo ===============================================
curl -L "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" -o "Arch\HTML5_Template\img\recent-pro-01.jpg"
curl -L "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" -o "Arch\HTML5_Template\img\recent-pro-02.jpg"
curl -L "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" -o "Arch\HTML5_Template\img\recent-pro-03.jpg"
curl -L "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" -o "Arch\HTML5_Template\img\recent-pro-04.jpg"
curl -L "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" -o "Arch\HTML5_Template\img\recent-pro-05.jpg"
curl -L "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" -o "Arch\HTML5_Template\img\recent-pro-06.jpg"

echo ===============================================
echo Downloading Gallery images...
echo ===============================================
curl -L "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" -o "Arch\HTML5_Template\img\gallery-01.jpg"
curl -L "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" -o "Arch\HTML5_Template\img\gallery-02.jpg"
curl -L "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" -o "Arch\HTML5_Template\img\gallery-03.jpg"
curl -L "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" -o "Arch\HTML5_Template\img\gallery-04.jpg"
curl -L "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" -o "Arch\HTML5_Template\img\gallery-05.jpg"
curl -L "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" -o "Arch\HTML5_Template\img\gallery-06.jpg"
curl -L "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" -o "Arch\HTML5_Template\img\gallery-07.jpg"

echo.
echo ✅ Comprehensive image download completed!
echo 📁 Images saved to: Arch\HTML5_Template\img\
echo.
echo 🎨 Images added for:
echo • About Us page (team photos, company images)
echo • Service pages (service-specific images)
echo • Contact page (background images)
echo • Gallery/Portfolio pages (project images)
echo • Blog pages (blog post images)
echo • Testimonial sections (client photos)
echo • Process pages (workflow images)
echo.
echo Next steps:
echo 1. Test all pages to ensure images load correctly
echo 2. Check responsive layout on different devices
echo 3. Commit and push changes to GitHub
echo 4. Deploy to Vercel
echo.
pause
