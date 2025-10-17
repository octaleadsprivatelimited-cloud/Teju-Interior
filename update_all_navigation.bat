@echo off
echo Updating navigation menus across all pages...
echo.

REM Update all HTML files to fix navigation links
echo Updating logo links...
powershell -Command "(Get-Content 'Arch\HTML5_Template\index4.html') -replace 'href=\"index\.html\"', 'href=\"index4.html\"' | Set-Content 'Arch\HTML5_Template\index4.html'"
powershell -Command "(Get-Content 'Arch\HTML5_Template\about-us.html') -replace 'href=\"index\.html\"', 'href=\"index4.html\"' | Set-Content 'Arch\HTML5_Template\about-us.html'"
powershell -Command "(Get-Content 'Arch\HTML5_Template\blog-3col.html') -replace 'href=\"index\.html\"', 'href=\"index4.html\"' | Set-Content 'Arch\HTML5_Template\blog-3col.html'"
powershell -Command "(Get-Content 'Arch\HTML5_Template\contact.html') -replace 'href=\"index\.html\"', 'href=\"index4.html\"' | Set-Content 'Arch\HTML5_Template\contact.html'"
powershell -Command "(Get-Content 'Arch\HTML5_Template\our-process.html') -replace 'href=\"index\.html\"', 'href=\"index4.html\"' | Set-Content 'Arch\HTML5_Template\our-process.html'"
powershell -Command "(Get-Content 'Arch\HTML5_Template\portfolio-detail-v1.html') -replace 'href=\"index\.html\"', 'href=\"index4.html\"' | Set-Content 'Arch\HTML5_Template\portfolio-detail-v1.html'"
powershell -Command "(Get-Content 'Arch\HTML5_Template\project-4col-v2.html') -replace 'href=\"index\.html\"', 'href=\"index4.html\"' | Set-Content 'Arch\HTML5_Template\project-4col-v2.html'"
powershell -Command "(Get-Content 'Arch\HTML5_Template\service-list.html') -replace 'href=\"index\.html\"', 'href=\"index4.html\"' | Set-Content 'Arch\HTML5_Template\service-list.html'"
powershell -Command "(Get-Content 'Arch\HTML5_Template\testimonial.html') -replace 'href=\"index\.html\"', 'href=\"index4.html\"' | Set-Content 'Arch\HTML5_Template\testimonial.html'"

echo.
echo ✅ Navigation update completed!
echo.
echo Changes made:
echo • Updated all logo links to point to index4.html
echo • Removed dead links to deleted pages
echo • Kept only the 9 required pages
echo.
echo Remaining pages:
echo • index4.html (Home Page 4)
echo • project-4col-v2.html (Project 4 v2)
echo • service-list.html (Services List)
echo • blog-3col.html (Blog 3 Column)
echo • portfolio-detail-v1.html (Portfolio v1)
echo • about-us.html (About Us)
echo • testimonial.html (Testimonials)
echo • our-process.html (Our Process)
echo • contact.html (Contact)
echo.
pause
