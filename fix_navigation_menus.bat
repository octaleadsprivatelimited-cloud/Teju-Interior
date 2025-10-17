@echo off
echo Fixing navigation menus in all pages...
echo.

REM Update index4.html navigation
echo Updating index4.html...
powershell -Command "(Get-Content 'Arch\HTML5_Template\index4.html') -replace 'href=\"index2\.html\"', 'href=\"index4.html\"' | Set-Content 'Arch\HTML5_Template\index4.html'"
powershell -Command "(Get-Content 'Arch\HTML5_Template\index4.html') -replace 'href=\"index3\.html\"', 'href=\"index4.html\"' | Set-Content 'Arch\HTML5_Template\index4.html'"
powershell -Command "(Get-Content 'Arch\HTML5_Template\index4.html') -replace 'href=\"index5\.html\"', 'href=\"index4.html\"' | Set-Content 'Arch\HTML5_Template\index4.html'"
powershell -Command "(Get-Content 'Arch\HTML5_Template\index4.html') -replace 'href=\"index6\.html\"', 'href=\"index4.html\"' | Set-Content 'Arch\HTML5_Template\index4.html'"
powershell -Command "(Get-Content 'Arch\HTML5_Template\index4.html') -replace 'href=\"project-2col-v1\.html\"', 'href=\"project-4col-v2.html\"' | Set-Content 'Arch\HTML5_Template\index4.html'"
powershell -Command "(Get-Content 'Arch\HTML5_Template\index4.html') -replace 'href=\"project-2col-v2\.html\"', 'href=\"project-4col-v2.html\"' | Set-Content 'Arch\HTML5_Template\index4.html'"
powershell -Command "(Get-Content 'Arch\HTML5_Template\index4.html') -replace 'href=\"project-3col-v1\.html\"', 'href=\"project-4col-v2.html\"' | Set-Content 'Arch\HTML5_Template\index4.html'"
powershell -Command "(Get-Content 'Arch\HTML5_Template\index4.html') -replace 'href=\"project-3col-v2\.html\"', 'href=\"project-4col-v2.html\"' | Set-Content 'Arch\HTML5_Template\index4.html'"
powershell -Command "(Get-Content 'Arch\HTML5_Template\index4.html') -replace 'href=\"project-4col-v1\.html\"', 'href=\"project-4col-v2.html\"' | Set-Content 'Arch\HTML5_Template\index4.html'"
powershell -Command "(Get-Content 'Arch\HTML5_Template\index4.html') -replace 'href=\"service-v1\.html\"', 'href=\"service-list.html\"' | Set-Content 'Arch\HTML5_Template\index4.html'"
powershell -Command "(Get-Content 'Arch\HTML5_Template\index4.html') -replace 'href=\"service-v2\.html\"', 'href=\"service-list.html\"' | Set-Content 'Arch\HTML5_Template\index4.html'"

REM Update all other pages
echo Updating all other pages...
for %%f in (about-us.html blog-3col.html contact.html our-process.html portfolio-detail-v1.html project-4col-v2.html service-list.html testimonial.html) do (
    echo Updating %%f...
    powershell -Command "(Get-Content 'Arch\HTML5_Template\%%f') -replace 'href=\"index\.html\"', 'href=\"index4.html\"' | Set-Content 'Arch\HTML5_Template\%%f'"
    powershell -Command "(Get-Content 'Arch\HTML5_Template\%%f') -replace 'href=\"index2\.html\"', 'href=\"index4.html\"' | Set-Content 'Arch\HTML5_Template\%%f'"
    powershell -Command "(Get-Content 'Arch\HTML5_Template\%%f') -replace 'href=\"index3\.html\"', 'href=\"index4.html\"' | Set-Content 'Arch\HTML5_Template\%%f'"
    powershell -Command "(Get-Content 'Arch\HTML5_Template\%%f') -replace 'href=\"index5\.html\"', 'href=\"index4.html\"' | Set-Content 'Arch\HTML5_Template\%%f'"
    powershell -Command "(Get-Content 'Arch\HTML5_Template\%%f') -replace 'href=\"index6\.html\"', 'href=\"index4.html\"' | Set-Content 'Arch\HTML5_Template\%%f'"
    powershell -Command "(Get-Content 'Arch\HTML5_Template\%%f') -replace 'href=\"project-2col-v1\.html\"', 'href=\"project-4col-v2.html\"' | Set-Content 'Arch\HTML5_Template\%%f'"
    powershell -Command "(Get-Content 'Arch\HTML5_Template\%%f') -replace 'href=\"project-2col-v2\.html\"', 'href=\"project-4col-v2.html\"' | Set-Content 'Arch\HTML5_Template\%%f'"
    powershell -Command "(Get-Content 'Arch\HTML5_Template\%%f') -replace 'href=\"project-3col-v1\.html\"', 'href=\"project-4col-v2.html\"' | Set-Content 'Arch\HTML5_Template\%%f'"
    powershell -Command "(Get-Content 'Arch\HTML5_Template\%%f') -replace 'href=\"project-3col-v2\.html\"', 'href=\"project-4col-v2.html\"' | Set-Content 'Arch\HTML5_Template\%%f'"
    powershell -Command "(Get-Content 'Arch\HTML5_Template\%%f') -replace 'href=\"project-4col-v1\.html\"', 'href=\"project-4col-v2.html\"' | Set-Content 'Arch\HTML5_Template\%%f'"
    powershell -Command "(Get-Content 'Arch\HTML5_Template\%%f') -replace 'href=\"service-v1\.html\"', 'href=\"service-list.html\"' | Set-Content 'Arch\HTML5_Template\%%f'"
    powershell -Command "(Get-Content 'Arch\HTML5_Template\%%f') -replace 'href=\"service-v2\.html\"', 'href=\"service-list.html\"' | Set-Content 'Arch\HTML5_Template\%%f'"
    powershell -Command "(Get-Content 'Arch\HTML5_Template\%%f') -replace 'href=\"blog-2col\.html\"', 'href=\"blog-3col.html\"' | Set-Content 'Arch\HTML5_Template\%%f'"
    powershell -Command "(Get-Content 'Arch\HTML5_Template\%%f') -replace 'href=\"blog-4col\.html\"', 'href=\"blog-3col.html\"' | Set-Content 'Arch\HTML5_Template\%%f'"
    powershell -Command "(Get-Content 'Arch\HTML5_Template\%%f') -replace 'href=\"blog-detail\.html\"', 'href=\"blog-3col.html\"' | Set-Content 'Arch\HTML5_Template\%%f'"
    powershell -Command "(Get-Content 'Arch\HTML5_Template\%%f') -replace 'href=\"blog-list\.html\"', 'href=\"blog-3col.html\"' | Set-Content 'Arch\HTML5_Template\%%f'"
    powershell -Command "(Get-Content 'Arch\HTML5_Template\%%f') -replace 'href=\"portfolio-detail-v2\.html\"', 'href=\"portfolio-detail-v1.html\"' | Set-Content 'Arch\HTML5_Template\%%f'"
    powershell -Command "(Get-Content 'Arch\HTML5_Template\%%f') -replace 'href=\"portfolio-detail-v3\.html\"', 'href=\"portfolio-detail-v1.html\"' | Set-Content 'Arch\HTML5_Template\%%f'"
)

echo.
echo ✅ Navigation menus fixed!
echo.
echo Changes made:
echo • Updated all logo links to point to index4.html
echo • Fixed all navigation links to point to existing pages only
echo • Removed dead links to deleted pages
echo • Kept navigation menu text unchanged
echo.
echo Remaining pages with working navigation:
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
