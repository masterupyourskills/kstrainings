"""
apply_nexa_blue_logo.py
-----------------------
Updates the logo styling to a 'Nexa Blue' theme.
"""
import glob, os, re

SITE_DIR = r'D:\Anti_gravity\kstrainings.com'
pages = glob.glob(os.path.join(SITE_DIR, '*.html'))
pages = [p for p in pages if 'admin' not in os.path.basename(p)]
pages.append(os.path.join(SITE_DIR, 'generate_all_courses.py'))

# Nexa Blue is a deep, rich navy (e.g. #001A36 or #002244).
NEXA_CSS = """  .logo { display: flex; align-items: center; gap: 12px; text-decoration: none; }
  .logo img { 
    height: 52px; width: 52px; 
    object-fit: contain; 
    border-radius: 50%; 
    border: 2px solid #002244; 
    box-shadow: 0 0 12px rgba(0, 34, 68, 0.2);
    background: #fff;
    padding: 2px;
  }
  .logo-name { 
    font-size: 1.45rem; 
    font-weight: 900; 
    color: #002244; /* Nexa Blue */
    text-transform: uppercase;
    letter-spacing: 0.5px;
    line-height: 1.1;
  }
  .logo-sub { 
    font-size: 0.68rem; 
    color: #2563eb; /* Complementary accent blue */
    font-weight: 700; 
    letter-spacing: .1em; 
    text-transform: uppercase; 
    margin-top: 2px;
  }"""

updated = 0
for p in pages:
    if os.path.exists(p):
        content = open(p, encoding='utf-8').read()
        original = content
        
        # Replace the CSS
        pattern = r'\.logo\s*\{.*?\}.*?\.logo-sub\s*\{.*?\}'
        if re.search(pattern, content, flags=re.DOTALL):
            content = re.sub(pattern, NEXA_CSS.strip(), content, flags=re.DOTALL)
            
        # Ensure image is the standard ks-logo.jpg
        content = content.replace('premium-ks-logo.jpg', 'ks-logo.jpg')

        if content != original:
            open(p, 'w', encoding='utf-8').write(content)
            updated += 1

print(f'Applied Nexa Blue Logo theme in {updated} files!')
