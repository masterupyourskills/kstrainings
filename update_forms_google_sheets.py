"""
update_forms_google_sheets.py
-----------------------------
Updates all KS Trainings HTML pages to submit forms to Google Sheets via Apps Script.
Also updates generate_all_courses.py template.

Run this AFTER you have deployed your Google Apps Script and obtained the Web App URL.
Then replace APPS_SCRIPT_URL below with your actual Web App URL.

Usage:
  python update_forms_google_sheets.py
"""

import os
import re

# ===== CONFIGURATION =====
# Replace this with your actual deployed Apps Script Web App URL
APPS_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbx4Ip9MnWcXhBuPr-wJ6SvYev2skqSpWdGBaz8mlccyGNF6H4VN1db28DVmdc7twp7I/exec"
SITE_DIR = r"D:\Anti_gravity\kstrainings.com"

# ===== SHARED submitForm SCRIPT =====
# This unified submitForm handles all pages.
# It reads the data-page attribute from the form (or falls back to the page title),
# then posts a JSON payload to the Apps Script endpoint.

SUBMIT_FORM_JS_TEMPLATE = """
  // ===== GOOGLE SHEETS FORM SUBMISSION =====
  var KS_APPS_SCRIPT_URL = '{apps_script_url}';

  function submitForm(formOrEvent) {{
    var form = (formOrEvent && formOrEvent.target) ? formOrEvent.target : formOrEvent;
    if (formOrEvent && typeof formOrEvent.preventDefault === 'function') formOrEvent.preventDefault();

    var msgEl = document.getElementById('ksFormMsg');
    var btn   = document.getElementById('ksSubmitBtn');
    if (!msgEl || !btn) return;

    // Honeypot
    if (form.elements['website'] && form.elements['website'].value !== '') return;

    // Captcha
    var c = form.elements['captcha'];
    if (c && c.value.trim() !== '7') {{
      msgEl.style.cssText = 'display:block;background:#fee2e2;color:#b91c1c;padding:12px 16px;border-radius:8px;font-size:.9rem;font-weight:600;margin-top:14px;';
      msgEl.textContent = 'Anti-spam check failed. Answer is 7.';
      return;
    }}

    var name         = (form.elements['name']          ? form.elements['name'].value.trim()          : '');
    var email        = (form.elements['email']         ? form.elements['email'].value.trim()         : '');
    var phone        = (form.elements['phone']         ? form.elements['phone'].value.trim()         : '');
    var course       = (form.elements['course']        ? form.elements['course'].value.trim()        : '');
    var serviceType  = (form.elements['service_type']  ? form.elements['service_type'].value         : '');
    var platform     = (form.elements['platform']      ? form.elements['platform'].value             : '');
    var bizName      = (form.elements['business_name'] ? form.elements['business_name'].value.trim() : '');
    var supportType  = (form.elements['support_type']  ? form.elements['support_type'].value         : '');
    var description  = (form.elements['description']   ? form.elements['description'].value.trim()   : '');
    var courseService = course || serviceType || platform;

    // Determine page name from form attribute or document title
    var pageName = (form.getAttribute('data-page') || document.title || 'Unknown Page').split('|')[0].trim();

    btn.disabled = true;
    msgEl.style.cssText = 'display:block;background:#eff6ff;color:#1d4ed8;padding:12px 16px;border-radius:8px;font-size:.9rem;font-weight:600;margin-top:14px;';
    msgEl.textContent = 'Submitting...';

    // Save to localStorage
    try {{
      var rec = {{
        id: Date.now(),
        submitted_at: new Date().toLocaleString('en-IN'),
        page: pageName,
        name: name, email: email, phone: phone,
        course_service: courseService, business_name: bizName,
        support_type: supportType, description: description,
        status: 'New'
      }};
      var all = JSON.parse(localStorage.getItem('ks_submissions') || '[]');
      all.unshift(rec);
      localStorage.setItem('ks_submissions', JSON.stringify(all));
    }} catch (e) {{}}

    function showOK() {{
      msgEl.style.cssText = 'display:block;background:#dcfce7;color:#15803d;padding:12px 16px;border-radius:8px;font-size:.9rem;font-weight:600;margin-top:14px;';
      msgEl.textContent = 'Thank you ' + (name || 'there') + '! Our team will contact you at ' + (phone || email) + ' within 24 hours.';
      form.reset();
      btn.disabled = false;
    }}

    // Post to Google Sheets via Apps Script
    var payload = JSON.stringify({{
      page_name:     pageName,
      name:          name,
      email:         email,
      phone:         phone,
      course_service: courseService,
      business_name: bizName,
      support_type:  supportType || serviceType,
      description:   description
    }});

    if (KS_APPS_SCRIPT_URL && KS_APPS_SCRIPT_URL !== 'https://script.google.com/macros/s/AKfycbx4Ip9MnWcXhBuPr-wJ6SvYev2skqSpWdGBaz8mlccyGNF6H4VN1db28DVmdc7twp7I/exec') {{
      fetch(KS_APPS_SCRIPT_URL, {{
        method: 'POST',
        body: payload,
        headers: {{ 'Content-Type': 'text/plain' }}
      }})
      .then(function(r) {{ return r.json(); }})
      .then(function() {{ showOK(); }})
      .catch(function() {{ showOK(); }});
    }} else {{
      showOK();
    }}
  }}
  // ===== END GOOGLE SHEETS FORM SUBMISSION =====
"""

def get_submit_form_js():
    return SUBMIT_FORM_JS_TEMPLATE.format(apps_script_url=APPS_SCRIPT_URL)


def inject_submit_form(content, page_label):
    """
    Inject/replace the submitForm function in a page's last <script> block.
    Also adds data-page attribute to the form elements for page identification.
    """
    # 1) Remove any existing submitForm function definitions (old Formspree or empty ones)
    content = re.sub(
        r'var FORMSPREE_ID\s*=\s*[\'"][^\'"]*[\'"]\s*;?\s*',
        '',
        content
    )
    content = re.sub(
        r'function submitForm\s*\(.*?\)\s*\{.*?(?=\}\s*(function|\s*//\s*=+\s*END|</script>))',
        '',
        content,
        flags=re.DOTALL
    )

    # 2) Add data-page attribute to all <form> elements that don't already have it
    content = re.sub(
        r'(<form\b(?![^>]*data-page)[^>]*)(>)',
        lambda m: m.group(1) + f' data-page="{page_label}"' + m.group(2),
        content
    )

    # 3) Inject the new submitForm into the LAST <script> block
    # Find all <script> block positions
    script_positions = list(re.finditer(r'<script(?:\s[^>]*)?>.*?</script>', content, re.DOTALL))
    
    inline_scripts = [m for m in script_positions if 'src=' not in m.group(0)]
    
    if inline_scripts:
        last = inline_scripts[-1]
        # Insert submitForm at the start of the last inline script
        inner_start = last.start() + last.group(0).index('>') + 1
        new_js = get_submit_form_js()
        content = content[:inner_start] + '\n' + new_js + '\n' + content[inner_start:]
    else:
        # No inline script — insert before </body>
        new_js = get_submit_form_js()
        content = content.replace('</body>', f'<script>\n{new_js}\n</script>\n</body>', 1)

    return content


def fix_index_html(page_label='Home Page - KS Trainings'):
    """
    Fix index.html which calls submitForm(event) but has no definition.
    Also the form uses onsubmit='submitForm(event)'.
    """
    filepath = os.path.join(SITE_DIR, 'index.html')
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Ensure the form has the correct onsubmit
    content = re.sub(
        r'onsubmit=["\']submitForm\(event\)["\']',
        'onsubmit="event.preventDefault(); submitForm(this);"',
        content
    )

    content = inject_submit_form(content, page_label)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  ✅ Updated: index.html")


def fix_static_page(filename, page_label):
    """Fix a static support/service page."""
    filepath = os.path.join(SITE_DIR, filename)
    if not os.path.exists(filepath):
        print(f"  ⚠️  SKIP (not found): {filename}")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    content = inject_submit_form(content, page_label)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  ✅ Updated: {filename}")


def fix_generated_courses():
    """
    Update generate_all_courses.py template to include Google Sheets submitForm.
    """
    filepath = os.path.join(SITE_DIR, 'generate_all_courses.py')
    if not os.path.exists(filepath):
        print(f"  ⚠️  SKIP (not found): generate_all_courses.py")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_submit = f"""var KS_APPS_SCRIPT_URL = '{APPS_SCRIPT_URL}';
    function submitForm(form) {{
      var msgEl = document.getElementById('ksFormMsg');
      var btn = document.getElementById('ksSubmitBtn');
      if (!msgEl || !btn) return;
      if (form.elements['website'] && form.elements['website'].value !== '') return;
      var c = form.elements['captcha'];
      if (!c || c.value.trim() !== '7') {{
        msgEl.style.cssText = 'display:block;background:#fee2e2;color:#b91c1c;padding:12px 16px;border-radius:8px;font-size:.9rem;font-weight:600;margin-top:14px;';
        msgEl.textContent = 'Anti-spam check failed. Answer is 7.'; return;
      }}
      var name = (form.elements['name'] ? form.elements['name'].value.trim() : '');
      var email = (form.elements['email'] ? form.elements['email'].value.trim() : '');
      var phone = (form.elements['phone'] ? form.elements['phone'].value.trim() : '');
      var course = (form.elements['course'] ? form.elements['course'].value.trim() : '');
      var supportType = (form.elements['support_type'] ? form.elements['support_type'].value : '');
      var description = (form.elements['description'] ? form.elements['description'].value.trim() : '');
      var pageName = (form.getAttribute('data-page') || document.title || 'Course Page').split('|')[0].trim();
      btn.disabled = true;
      msgEl.style.cssText = 'display:block;background:#eff6ff;color:#1d4ed8;padding:12px 16px;border-radius:8px;font-size:.9rem;font-weight:600;margin-top:14px;';
      msgEl.textContent = 'Submitting...';
      try {{
        var rec = {{id:Date.now(),submitted_at:new Date().toLocaleString('en-IN'),page:pageName,name:name,email:email,phone:phone,course_service:course,support_type:supportType,description:description,status:'New'}};
        var all = JSON.parse(localStorage.getItem('ks_submissions')||'[]'); all.unshift(rec); localStorage.setItem('ks_submissions',JSON.stringify(all));
      }} catch(e) {{}}
      function showOK() {{
        msgEl.style.cssText = 'display:block;background:#dcfce7;color:#15803d;padding:12px 16px;border-radius:8px;font-size:.9rem;font-weight:600;margin-top:14px;';
        msgEl.textContent = 'Thank you '+name+'! Our team will contact you at '+phone+' within 24 hours.';
        form.reset(); btn.disabled = false;
      }}
      if (KS_APPS_SCRIPT_URL && KS_APPS_SCRIPT_URL !== 'https://script.google.com/macros/s/AKfycbx4Ip9MnWcXhBuPr-wJ6SvYev2skqSpWdGBaz8mlccyGNF6H4VN1db28DVmdc7twp7I/exec') {{
        fetch(KS_APPS_SCRIPT_URL, {{method:'POST',body:JSON.stringify({{page_name:pageName,name:name,email:email,phone:phone,course_service:course,support_type:supportType,description:description}}),headers:{{'Content-Type':'text/plain'}}}})
        .then(function(r){{return r.json();}}).then(function(){{showOK();}}).catch(function(){{showOK();}});
      }} else {{ showOK(); }}
    }}"""

    # Replace old FORMSPREE-based submitForm in the template
    # The template uses string literals containing the JS
    old_pattern = re.compile(
        r"var FORMSPREE_ID\s*=\s*['\"][^'\"]*['\"];?\s*function submitForm\s*\(.*?\)\s*\{.*?(?=\s*(?:var |/\*|//\s*={5,}))",
        re.DOTALL
    )
    if old_pattern.search(content):
        content = old_pattern.sub(new_submit, content, count=1)
        print("  ✅ Replaced FORMSPREE submitForm in generate_all_courses.py")
    else:
        print("  ℹ️  FORMSPREE pattern not found in generate_all_courses.py — may need manual check")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  ✅ Updated: generate_all_courses.py")


def regenerate_course_pages():
    """Re-run the course generator to apply the new submit function to all course pages."""
    gen_path = os.path.join(SITE_DIR, 'generate_all_courses.py')
    if os.path.exists(gen_path):
        import subprocess
        result = subprocess.run(['python', gen_path], capture_output=True, text=True, cwd=SITE_DIR)
        if result.returncode == 0:
            print("  ✅ Course pages regenerated successfully")
        else:
            print(f"  ❌ Course regeneration failed: {result.stderr[:300]}")
    else:
        print("  ⚠️  generate_all_courses.py not found — skipping regeneration")


def verify_updates():
    """Quick verification — count pages that now have the Apps Script URL."""
    import glob
    pages = glob.glob(os.path.join(SITE_DIR, '*.html'))
    with_url = 0
    without_url = 0
    for p in pages:
        try:
            c = open(p, encoding='utf-8').read()
            if 'KS_APPS_SCRIPT_URL' in c:
                with_url += 1
            else:
                without_url += 1
        except:
            pass
    print(f"\n  📊 Verification: {with_url} pages have KS_APPS_SCRIPT_URL, {without_url} pages do not")
    return with_url, without_url


if __name__ == '__main__':
    print("\n🚀 KS Trainings — Google Sheets Form Integration Script")
    print("=" * 60)

    print(f"\n⚙️  Apps Script URL: {APPS_SCRIPT_URL}")
    if APPS_SCRIPT_URL == 'https://script.google.com/macros/s/AKfycbx4Ip9MnWcXhBuPr-wJ6SvYev2skqSpWdGBaz8mlccyGNF6H4VN1db28DVmdc7twp7I/exec':
        print("  ⚠️  NOTE: Using placeholder URL. Forms will save locally only.")
        print("     Replace APPS_SCRIPT_URL in this file after deploying your Apps Script.\n")

    print("\n📄 Updating static pages...")
    fix_index_html('Home Page - KS Trainings')
    fix_static_page('on-job-support.html',         'On-Job Support Page')
    fix_static_page('proxy-job-support.html',      'Proxy Job Support Page')
    fix_static_page('proxy-interview-support.html','Proxy Interview Support Page')
    fix_static_page('video-editing.html',          'Video Editing Services Page')
    fix_static_page('social-media-management.html','Social Media Management Page')
    fix_static_page('courses.html',                'Courses Catalog Page')

    print("\n📦 Updating course page generator...")
    fix_generated_courses()

    print("\n🔄 Regenerating all course pages with new submit function...")
    regenerate_course_pages()

    print("\n🔍 Verifying updates...")
    verify_updates()

    print("\n✅ Done! Next steps:")
    print("   1. Deploy the Apps Script (see google_apps_script.js for instructions)")
    print("   2. Copy the Web App URL")
    print("   3. Open this file, set APPS_SCRIPT_URL = 'your-url-here'")
    print("   4. Run this script again")
    print("   5. Run scratch_test_sheet_insert.py to verify a sample record is saved\n")
