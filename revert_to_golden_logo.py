"""
revert_to_golden_logo.py
------------------------
Restores the Golden Premium Logo styling and reverts the image back to ks-logo.jpg.
"""
import glob, os, re

SITE_DIR = r'D:\Anti_gravity\kstrainings.com'
pages = glob.glob(os.path.join(SITE_DIR, '*.html'))
pages = [p for p in pages if 'admin' not in os.path.basename(p)]
pages.append(os.path.join(SITE_DIR, 'generate_all_courses.py'))

GOLDEN_CSS = """  .logo { display: flex; align-items: center; gap: 12px; text-decoration: none; }
  .logo img { 
    height: 52px; width: 52px; 
    object-fit: contain; 
    border-radius: 50%; 
    border: 2px solid #D4AF37; 
    box-shadow: 0 0 10px rgba(212,175,55,0.4);
    background: #fff;
    padding: 2px;
  }
  .logo-name { 
    font-size: 1.4rem; 
    font-weight: 900; 
    background: linear-gradient(135deg, #B8860B 0%, #FFDF00 50%, #DAA520 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }
  .logo-sub { 
    font-size: 0.65rem; 
    color: #8B6508; 
    font-weight: 700; 
    letter-spacing: .1em; 
    text-transform: uppercase; 
  }"""

updated = 0
for p in pages:
    if os.path.exists(p):
        content = open(p, encoding='utf-8').read()
        original = content
        
        # 1. Update the CSS to Golden Premium
        pattern = r'\.logo\s*\{.*?\}.*?\.logo-sub\s*\{.*?\}'
        if re.search(pattern, content, flags=re.DOTALL):
            content = re.sub(pattern, GOLDEN_CSS.strip(), content, flags=re.DOTALL)
            
        # 2. Revert the image source
        content = content.replace('premium-ks-logo.jpg', 'ks-logo.jpg')

        if content != original:
            open(p, 'w', encoding='utf-8').write(content)
            updated += 1

print(f'Reverted to Golden Premium Logo in {updated} files!')
