"""
update_logo_blue_premium.py
---------------------------
Updates the logo image to the newly generated AI premium logo,
and restyles the text to a clean, enterprise blue theme matching top institutes.
"""
import glob, os, re

SITE_DIR = r'D:\Anti_gravity\kstrainings.com'
pages = glob.glob(os.path.join(SITE_DIR, '*.html'))
pages = [p for p in pages if 'admin' not in os.path.basename(p)]
pages.append(os.path.join(SITE_DIR, 'generate_all_courses.py'))

NEW_CSS = """  .logo { display: flex; align-items: center; gap: 12px; text-decoration: none; }
  .logo img { 
    height: 52px; width: 52px; 
    object-fit: contain; 
    border-radius: 8px; /* Slightly squared like modern tech logos */
    background: transparent;
  }
  .logo-name { 
    font-size: 1.45rem; 
    font-weight: 900; 
    color: #1a2456;
    letter-spacing: -0.5px;
    line-height: 1.1;
  }
  .logo-sub { 
    font-size: 0.68rem; 
    color: #2563eb; 
    font-weight: 700; 
    letter-spacing: 0.08em; 
    text-transform: uppercase; 
    margin-top: 2px;
  }"""

updated = 0
for p in pages:
    if os.path.exists(p):
        content = open(p, encoding='utf-8').read()
        original = content
        
        # 1. Update the CSS
        pattern = r'\.logo\s*\{.*?\}.*?\.logo-sub\s*\{.*?\}'
        if re.search(pattern, content, flags=re.DOTALL):
            content = re.sub(pattern, NEW_CSS.strip(), content, flags=re.DOTALL)
            
        # 2. Update the image source
        content = content.replace('ks-logo.jpg', 'premium-ks-logo.jpg')

        if content != original:
            open(p, 'w', encoding='utf-8').write(content)
            updated += 1

print(f'Updated logo styling to Blue Premium in {updated} files!')
