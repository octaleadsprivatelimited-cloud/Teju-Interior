@echo off
echo 🎨 Downloading additional images for all pages...
echo ============================================================

python comprehensive_image_update.py

echo.
echo ✅ Additional images download completed!
echo 📁 All images saved to: Arch\HTML5_Template\img\
echo.
echo Next steps:
echo 1. Update HTML files to use new images
echo 2. Test responsive layout
echo 3. Commit and push changes
echo.
pause
