@echo off
echo 🔧 Fixing navigation menus across all pages...
echo ============================================================

python fix_all_pages_navigation.py

echo.
echo ✅ Navigation menus fixed across all pages!
echo 🔗 All dead links removed, only existing pages linked
echo.
echo Next steps:
echo 1. Test all navigation links
echo 2. Add missing images to pages
echo 3. Commit and push changes
echo.
pause
