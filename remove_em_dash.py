"""
remove_em_dash.py
-----------------
Replaces the em dash character '—' with a standard hyphen '-' across all HTML pages.
"""
import glob, os

SITE_DIR = r'D:\Anti_gravity\kstrainings.com'
pages = glob.glob(os.path.join(SITE_DIR, '*.html'))
pages.append(os.path.join(SITE_DIR, 'generate_all_courses.py'))

updated = 0
for p in pages:
    if os.path.exists(p):
        content = open(p, encoding='utf-8').read()
        
        if '—' in content:
            new_content = content.replace('—', '-')
            open(p, 'w', encoding='utf-8').write(new_content)
            updated += 1

print(f'Replaced em dash with hyphen in {updated} files!')
