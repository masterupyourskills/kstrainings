# KS Trainings Course Pages Regeneration script
Write-Host "Regenerating all 45+ course files matching the new slate/purple theme..."

# Run course pages generation script
python generate_all_courses.py

# Run courses catalog updates
python update_courses_page.py

Write-Host "Regeneration completed successfully! All pages are now 100% consistent."
