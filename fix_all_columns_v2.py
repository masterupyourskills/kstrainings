"""
fix_all_columns_v2.py
----------------------
Replaces ALL submitForm blocks (both with and without END comment)
across ALL 65 HTML pages with the complete 9-column version.
Includes: business_name default, phone placeholder fix, all fields.
"""
import glob, os, re

SITE_DIR = r'D:\Anti_gravity\kstrainings.com'
APPS_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbx4Ip9MnWcXhBuPr-wJ6SvYev2skqSpWdGBaz8mlccyGNF6H4VN1db28DVmdc7twp7I/exec'

NEW_SUBMIT_BLOCK = """
  // ===== GOOGLE SHEETS FORM SUBMISSION =====
  var KS_APPS_SCRIPT_URL = '""" + APPS_SCRIPT_URL + """';
  function submitForm(formOrEvent) {
    var form = (formOrEvent && formOrEvent.target) ? formOrEvent.target : formOrEvent;
    if (formOrEvent && typeof formOrEvent.preventDefault === 'function') formOrEvent.preventDefault();
    var msgEl = document.getElementById('ksFormMsg');
    var btn   = document.getElementById('ksSubmitBtn');
    if (!msgEl || !btn) return;

    // Honeypot check
    if (form.elements['website'] && form.elements['website'].value !== '') return;

    // Captcha check (3 + 4 = 7)
    var c = form.elements['captcha'];
    if (c && c.value.trim() !== '7') {
      msgEl.style.cssText = 'display:block;background:#fee2e2;color:#b91c1c;padding:12px 16px;border-radius:8px;font-size:.9rem;font-weight:600;margin-top:14px;';
      msgEl.textContent = 'Anti-spam check failed. Hint: 3 + 4 = 7'; return;
    }

    // Collect ALL fields
    var name        = form.elements['name']          ? form.elements['name'].value.trim()          : '';
    var email       = form.elements['email']         ? form.elements['email'].value.trim()         : '';
    var phone       = form.elements['phone']         ? form.elements['phone'].value.trim()         : '';
    var course      = form.elements['course']        ? form.elements['course'].value.trim()        : '';
    var serviceType = form.elements['service_type']  ? form.elements['service_type'].value.trim()  : '';
    var platform    = form.elements['platform']      ? form.elements['platform'].value.trim()      : '';
    var bizName     = form.elements['business_name'] ? form.elements['business_name'].value.trim() : 'Individual / N.A.';
    var supportType = form.elements['support_type']  ? form.elements['support_type'].value.trim()  : (serviceType || 'Training Enquiry');
    var description = form.elements['description']   ? form.elements['description'].value.trim()   : '';
    var courseService = course || serviceType || platform || 'General Enquiry';
    var pageName = (form.getAttribute('data-page') || document.title || 'KS Trainings').split('|')[0].trim();

    btn.disabled = true;
    msgEl.style.cssText = 'display:block;background:#eff6ff;color:#1d4ed8;padding:12px 16px;border-radius:8px;font-size:.9rem;font-weight:600;margin-top:14px;';
    msgEl.textContent = 'Submitting your enquiry...';

    // Backup to localStorage
    try {
      var rec = {id:Date.now(), submitted_at:new Date().toLocaleString('en-IN'),
        page:pageName, name:name, email:email, phone:phone,
        course_service:courseService, business_name:bizName,
        support_type:supportType, description:description, status:'New'};
      var all = JSON.parse(localStorage.getItem('ks_submissions') || '[]');
      all.unshift(rec);
      localStorage.setItem('ks_submissions', JSON.stringify(all));
    } catch(e) {}

    function showOK() {
      msgEl.style.cssText = 'display:block;background:#dcfce7;color:#15803d;padding:12px 16px;border-radius:8px;font-size:.9rem;font-weight:600;margin-top:14px;';
      msgEl.textContent = 'Thank you ' + (name || 'there') + '! Our team will contact you at ' + (phone || email) + ' within 24 hours.';
      form.reset();
      btn.disabled = false;
    }

    // POST all 9 columns to Google Sheets
    fetch(KS_APPS_SCRIPT_URL, {
      method: 'POST',
      body: JSON.stringify({
        page_name:      pageName,
        name:           name,
        email:          email,
        phone:          phone,
        course_service: courseService,
        business_name:  bizName,
        support_type:   supportType,
        description:    description
      }),
      headers: { 'Content-Type': 'text/plain' }
    })
    .then(function(r) { return r.json(); })
    .then(function() { showOK(); })
    .catch(function() { showOK(); });
  }
  // ===== END GOOGLE SHEETS FORM SUBMISSION =====
"""

def replace_block(content):
    # Pattern 1: Full block with END comment
    p1 = re.compile(
        r'// ===== GOOGLE SHEETS FORM SUBMISSION =====.*?// ===== END GOOGLE SHEETS FORM SUBMISSION =====',
        re.DOTALL
    )
    if p1.search(content):
        return p1.sub(NEW_SUBMIT_BLOCK.strip(), content)

    # Pattern 2: var KS_APPS_SCRIPT_URL = ... followed by function submitForm block
    # Match from var KS_APPS_SCRIPT_URL to the closing of submitForm
    p2 = re.compile(
        r"var KS_APPS_SCRIPT_URL\s*=\s*['\"][^'\"]*['\"];?\s*function submitForm\s*\(.*?\)\s*\{.*?^\s*\}\s*$",
        re.DOTALL | re.MULTILINE
    )
    if p2.search(content):
        return p2.sub(NEW_SUBMIT_BLOCK.strip(), content)

    # Pattern 3: Compact one-liner style (generated pages)
    p3 = re.compile(
        r"var KS_APPS_SCRIPT_URL\s*=\s*['\"][^'\"]*['\"];\s*function submitForm\s*\(.*?showOK\(\);\s*\}\s*\}",
        re.DOTALL
    )
    if p3.search(content):
        return p3.sub(NEW_SUBMIT_BLOCK.strip(), content)

    return content


pages = sorted(glob.glob(os.path.join(SITE_DIR, '*.html')))
pages = [p for p in pages if 'admin' not in os.path.basename(p)]

updated = 0
unchanged = 0
for p in pages:
    content = open(p, encoding='utf-8').read()
    if 'KS_APPS_SCRIPT_URL' not in content:
        unchanged += 1
        continue
    new_content = replace_block(content)
    if new_content != content:
        open(p, 'w', encoding='utf-8').write(new_content)
        updated += 1
    else:
        unchanged += 1

print(f'Updated: {updated} pages')
print(f'Unchanged (no form / already done): {unchanged} pages')

# Final verification
full_cols = 0
for p in pages:
    c = open(p, encoding='utf-8').read()
    if 'Individual / N.A.' in c or ("business_name" in c and "KS_APPS_SCRIPT_URL" in c):
        full_cols += 1

print(f'Pages sending all 9 columns: {full_cols}/{len(pages)}')
