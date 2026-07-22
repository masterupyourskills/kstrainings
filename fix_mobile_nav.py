import os
import glob
import re

html_files = glob.glob('*.html')

css_fix = """
    /* Mobile Nav Fix */
    @media (max-width: 768px) {
      #mainNav { display: none !important; }
      #mainNav.show-mobile-nav { 
        display: flex !important; 
        flex-direction: column !important; 
        position: absolute !important; 
        top: 78px !important; 
        left: 0 !important; 
        right: 0 !important; 
        background: #fff !important; 
        box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1) !important; 
        padding: 20px !important; 
        z-index: 1000 !important; 
        align-items: stretch !important;
      }
      #mainNav.show-mobile-nav a {
        width: 100% !important;
        text-align: left !important;
        margin-bottom: 5px !important;
      }
      .menu-toggle { display: block !important; }
    }
"""

js_fix = """
<script>
  // Mobile Nav Toggle Fix
  document.addEventListener('DOMContentLoaded', function() {
    var menuToggle = document.getElementById('menuToggle');
    var mainNav = document.getElementById('mainNav');
    if (menuToggle && mainNav) {
      menuToggle.addEventListener('click', function(e) {
        e.preventDefault();
        mainNav.classList.toggle('show-mobile-nav');
        // Clear old inline styles if they were set by previous inline scripts
        mainNav.style.display = '';
        mainNav.style.flexDirection = '';
        mainNav.style.position = '';
        mainNav.style.top = '';
        mainNav.style.left = '';
        mainNav.style.right = '';
        mainNav.style.background = '';
        mainNav.style.boxShadow = '';
        mainNav.style.padding = '';
        mainNav.style.zIndex = '';
      });
    }
  });
</script>
"""

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Apply CSS Fix if not already there
    if '/* Mobile Nav Fix */' not in content:
        content = content.replace('</style>', css_fix + '\n</style>', 1)
        
    # Apply JS Fix if not already there
    if '// Mobile Nav Toggle Fix' not in content:
        # insert before </body>
        if '</body>' in content:
            content = content.replace('</body>', js_fix + '\n</body>')
        else:
            content += js_fix

    # Optional: We don't remove the old script, because overriding it with the class toggle + clearing inline styles works around it, but if it's there it might trigger twice. 
    # Actually, the old script toggles inline styles. If our script runs after, it clears them, but the old script will still run on click and add them back.
    # We should comment out the old JS if it's present.
    # The old JS is:
    # menuToggle.addEventListener('click', function() {
    #     if (mainNav.style.display === 'flex' && mainNav.style.flexDirection === 'column') {
    old_js_pattern = r"menuToggle\.addEventListener\('click',\s*function\(\)\s*\{[\s\S]*?if\s*\(mainNav\.style\.display\s*===\s*'flex'[\s\S]*?\}\);"
    content = re.sub(old_js_pattern, "// old mobile menu toggle removed", content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Processed {len(html_files)} HTML files.")
