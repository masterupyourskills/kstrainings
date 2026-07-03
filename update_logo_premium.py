"""
update_logo_premium.py
----------------------
Updates the logo styling across all pages to a premium, golden look.
"""
import glob, os, re

SITE_DIR = r'D:\Anti_gravity\kstrainings.com'
pages = glob.glob(os.path.join(SITE_DIR, '*.html'))
pages = [p for p in pages if 'admin' not in os.path.basename(p)]
pages.append(os.path.join(SITE_DIR, 'generate_all_courses.py'))

OLD_CSS = """  .logo { display: flex; align-items: center; gap: 10px; }
  .logo img { height: 48px; width: 48px; object-fit: contain; border-radius: 50%; }
  .logo-name { font-size: 1.3rem; font-weight: 800; color: #1a2456; }
  .logo-sub { font-size: 0.62rem; color: #6b7280; font-weight: 500; letter-spacing: .05em; text-transform: uppercase; }"""

# In generate_all_courses.py it might be height: 56px instead of 48px, wait let's use regex to be safe.
# Actually, I can just replace the entire block or use re.sub for each class

NEW_CSS = """  .logo { display: flex; align-items: center; gap: 12px; text-decoration: none; }
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
        
        # Replace the css block
        # We'll use a regex that captures from `.logo {` up to `.logo-sub { ... }`
        pattern = r'\.logo\s*\{.*?\}.*?\.logo-sub\s*\{.*?\}'
        if re.search(pattern, content, flags=re.DOTALL):
            new_content = re.sub(pattern, NEW_CSS.strip(), content, flags=re.DOTALL)
            if new_content != content:
                open(p, 'w', encoding='utf-8').write(new_content)
                updated += 1

print(f'Updated logo styling to Premium Gold in {updated} files!')
