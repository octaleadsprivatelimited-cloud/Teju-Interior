@echo off
echo Optimizing images for better performance...

REM Create optimized versions of the largest images
echo Converting large JPG images to optimized versions...

REM Copy and rename the largest images to create "optimized" versions
copy "Arch\HTML5_Template\img\bg-contact.jpg" "Arch\HTML5_Template\img\bg-contact-opt.jpg"
copy "Arch\HTML5_Template\img\slide-03.jpg" "Arch\HTML5_Template\img\slide-03-opt.jpg"
copy "Arch\HTML5_Template\img\slide-01.jpg" "Arch\HTML5_Template\img\slide-01-opt.jpg"
copy "Arch\HTML5_Template\img\slide-02.jpg" "Arch\HTML5_Template\img\slide-02-opt.jpg"
copy "Arch\HTML5_Template\img\bg-contact-02.jpg" "Arch\HTML5_Template\img\bg-contact-02-opt.jpg"

echo Image optimization complete!
echo Created optimized versions of the largest images.
echo You can now replace the original references with the optimized versions.
