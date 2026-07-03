"""Fix phone number placeholder across all pages - replace +91 XXXXX format."""
import glob, os, re

SITE_DIR = r'D:\Anti_gravity\kstrainings.com'
pages = glob.glob(os.path.join(SITE_DIR, '*.html'))
py_files = [
    os.path.join(SITE_DIR, 'generate_all_courses.py'),
    os.path.join(SITE_DIR, 'update_courses_page.py'),
]

NEW_PLACEHOLDER = 'Mobile / WhatsApp Number *'

updated_pages = 0
for p in pages + py_files:
    if not os.path.exists(p):
        continue
    content = open(p, encoding='utf-8').read()
    original = content

    # Replace all +91 placeholder variations using regex
    content = re.sub(
        r'placeholder=["\'][+]91[\s\-X0-9]+["\']',
        f'placeholder="{NEW_PLACEHOLDER}"',
        content
    )
    # Also fix: Phone / WhatsApp * on index.html - keep as is (already clean)
    # Fix test script phone number
    content = content.replace(
        'placeholder="Phone / WhatsApp *"',
        'placeholder="Mobile / WhatsApp Number *"'
    )

    if content != original:
        open(p, 'w', encoding='utf-8').write(content)
        updated_pages += 1
        print(f'Fixed: {os.path.basename(p)}')

print(f'\nTotal updated: {updated_pages} files')

# Verify
remaining = 0
for p in pages:
    c = open(p, encoding='utf-8').read()
    if '+91 XXXXX' in c or '+91-XXXXX' in c:
        remaining += 1
        print(f'Still has +91 format: {os.path.basename(p)}')

if remaining == 0:
    print('All +91 placeholders fixed successfully!')
