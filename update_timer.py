"""
update_timer.py
---------------
Updates the popup auto-close timer from 7 seconds (7000ms) to 4 seconds (4000ms).
"""
import glob, os, re

SITE_DIR = r'D:\Anti_gravity\kstrainings.com'
pages = glob.glob(os.path.join(SITE_DIR, '*.html'))
pages = [p for p in pages if 'admin' not in os.path.basename(p)]

# Include the generator file
pages.append(os.path.join(SITE_DIR, 'generate_all_courses.py'))

updated = 0
for p in pages:
    if os.path.exists(p):
        content = open(p, encoding='utf-8').read()
        if '7000);' in content and 'closeSuccessPopup' in content:
            new_content = content.replace('7000);', '4000);')
            open(p, 'w', encoding='utf-8').write(new_content)
            updated += 1

print(f'Updated timer to 4 seconds in {updated} files!')
