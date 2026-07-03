"""
clean_leftover_js.py
--------------------
Cleans up leftover syntax errors after the submitForm block that was accidentally
left behind by the previous regex replacement.
"""
import glob, os, re

SITE_DIR = r'D:\Anti_gravity\kstrainings.com'
pages = glob.glob(os.path.join(SITE_DIR, '*.html'))
pages = [p for p in pages if 'admin' not in os.path.basename(p)]
pages.append(os.path.join(SITE_DIR, 'generate_all_courses.py'))

updated = 0
for p in pages:
    if os.path.exists(p):
        content = open(p, encoding='utf-8').read()
        
        # We want to remove everything between 
        # "// ===== END GOOGLE SHEETS FORM SUBMISSION ====="
        # and
        # "</script>"
        
        # Regex explanation:
        # Match the end comment, any whitespace/newlines, then capture the leftover junk, up to </script>
        pattern = r'(// ===== END GOOGLE SHEETS FORM SUBMISSION =====)(.*?)(</script>)'
        
        match = re.search(pattern, content, flags=re.DOTALL)
        if match:
            junk = match.group(2)
            if junk.strip(): # if there is actually leftover code (not just whitespace)
                # Ensure we only remove it if it looks like the leftover variables/fetch
                if 'var name =' in junk or 'fetch(' in junk:
                    new_content = content[:match.start(2)] + "\n  " + content[match.end(2):]
                    open(p, 'w', encoding='utf-8').write(new_content)
                    updated += 1

print(f'Cleaned leftover JS in {updated} files!')
