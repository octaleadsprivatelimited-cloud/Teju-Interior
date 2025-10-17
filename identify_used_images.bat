@echo off
echo Identifying used images in the project...
echo.

REM Create a temporary file to store all image references
echo Finding all image references in HTML files...
findstr /s /i "src=\"img/" Arch\HTML5_Template\*.html > used_images_temp.txt
findstr /s /i "background-image.*img/" Arch\HTML5_Template\*.html >> used_images_temp.txt

echo.
echo Used images found:
echo ==================
type used_images_temp.txt

echo.
echo Image cleanup analysis completed!
echo.
echo Note: This script identifies used images but doesn't remove them automatically.
echo Review the list above to see which images are actually being used.
echo.
del used_images_temp.txt
pause
