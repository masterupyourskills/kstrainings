"""
fix_faq_and_mobile_js.py
------------------------
Restores the FAQ Accordion and Mobile Menu JS functionality across all pages.
"""
import glob, os

SITE_DIR = r'D:\Anti_gravity\kstrainings.com'
pages = glob.glob(os.path.join(SITE_DIR, '*.html'))
pages = [p for p in pages if 'admin' not in os.path.basename(p)]
pages.append(os.path.join(SITE_DIR, 'generate_all_courses.py'))

FAQ_AND_MOBILE_JS = """
<!-- ================= FAQ & MOBILE MENU JS ================= -->
<script>
  (function() {
    // Mobile Menu
    var menuToggle = document.getElementById('menuToggle');
    var mainNav = document.getElementById('mainNav');
    if (menuToggle && mainNav) {
      menuToggle.addEventListener('click', function() {
        if (mainNav.style.display === 'flex' && mainNav.style.flexDirection === 'column') {
          mainNav.style.display = 'none';
        } else {
          mainNav.style.display = 'flex';
          mainNav.style.flexDirection = 'column';
          mainNav.style.position = 'absolute';
          mainNav.style.top = '78px';
          mainNav.style.left = '0';
          mainNav.style.right = '0';
          mainNav.style.background = '#fff';
          mainNav.style.boxShadow = '0 10px 15px -3px rgba(0,0,0,0.1)';
          mainNav.style.padding = '20px';
          mainNav.style.zIndex = '1000';
        }
      });
    }

    // FAQ Accordion
    var faqQs = document.querySelectorAll('.faq-q');
    faqQs.forEach(function(btn) {
      btn.addEventListener('click', function() {
        var ans = this.nextElementSibling;
        if (ans) {
          if (ans.style.display === 'block') {
            ans.style.display = 'none';
          } else {
            ans.style.display = 'block';
          }
        }
      });
    });
  })();
</script>
<!-- ================= END FAQ & MOBILE MENU JS ================= -->
"""

updated = 0
for p in pages:
    if os.path.exists(p):
        content = open(p, encoding='utf-8').read()
        
        if 'FAQ Accordion' not in content and 'FAQ & MOBILE MENU JS' not in content:
            # Insert before </body>
            if '</body>' in content:
                new_content = content.replace('</body>', FAQ_AND_MOBILE_JS + '\n</body>')
                open(p, 'w', encoding='utf-8').write(new_content)
                updated += 1

print(f'Added FAQ & Mobile Menu JS to {updated} files!')
