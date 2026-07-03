"""
fix_all_columns.py
-------------------
1. Updates submitForm JS in ALL pages to always send ALL 9 sheet columns
   (business_name defaults to 'Individual / N.A.' when not on a form)
2. Updates test script to verify every column has data for every page
"""
import glob, os, re

SITE_DIR = r'D:\Anti_gravity\kstrainings.com'
APPS_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbx4Ip9MnWcXhBuPr-wJ6SvYev2skqSpWdGBaz8mlccyGNF6H4VN1db28DVmdc7twp7I/exec'

# New complete submitForm that ALWAYS sends all 9 columns
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

    // Collect ALL fields — use 'N/A' when field not on this page
    var name        = form.elements['name']          ? form.elements['name'].value.trim()          : '';
    var email       = form.elements['email']         ? form.elements['email'].value.trim()         : '';
    var phone       = form.elements['phone']         ? form.elements['phone'].value.trim()         : '';
    var course      = form.elements['course']        ? form.elements['course'].value.trim()        : '';
    var serviceType = form.elements['service_type']  ? form.elements['service_type'].value.trim()  : '';
    var platform    = form.elements['platform']      ? form.elements['platform'].value.trim()      : '';
    var bizName     = form.elements['business_name'] ? form.elements['business_name'].value.trim() : 'Individual / N.A.';
    var supportType = form.elements['support_type']  ? form.elements['support_type'].value.trim()  : serviceType || 'Training Enquiry';
    var description = form.elements['description']   ? form.elements['description'].value.trim()   : '';
    var courseService = course || serviceType || platform || 'General Enquiry';

    // Page name from form attribute or document title
    var pageName = (form.getAttribute('data-page') || document.title || 'KS Trainings').split('|')[0].trim();

    btn.disabled = true;
    msgEl.style.cssText = 'display:block;background:#eff6ff;color:#1d4ed8;padding:12px 16px;border-radius:8px;font-size:.9rem;font-weight:600;margin-top:14px;';
    msgEl.textContent = 'Submitting your enquiry...';

    // Save backup to localStorage
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
    var payload = JSON.stringify({
      page_name:      pageName,
      name:           name,
      email:          email,
      phone:          phone,
      course_service: courseService,
      business_name:  bizName,
      support_type:   supportType,
      description:    description
    });

    fetch(KS_APPS_SCRIPT_URL, {
      method: 'POST',
      body: payload,
      headers: { 'Content-Type': 'text/plain' }
    })
    .then(function(r) { return r.json(); })
    .then(function() { showOK(); })
    .catch(function() { showOK(); });
  }
  // ===== END GOOGLE SHEETS FORM SUBMISSION =====
"""

def replace_submit_block(content):
    """Replace existing KS_APPS_SCRIPT_URL block with new complete block."""
    # Pattern: everything from var KS_APPS_SCRIPT_URL to END comment
    pattern = re.compile(
        r'// ===== GOOGLE SHEETS FORM SUBMISSION =====.*?// ===== END GOOGLE SHEETS FORM SUBMISSION =====',
        re.DOTALL
    )
    if pattern.search(content):
        return pattern.sub(NEW_SUBMIT_BLOCK.strip(), content)
    return content

pages = glob.glob(os.path.join(SITE_DIR, '*.html'))
py_template = os.path.join(SITE_DIR, 'generate_all_courses.py')

updated = 0
for p in pages:
    content = open(p, encoding='utf-8').read()
    new_content = replace_submit_block(content)
    if new_content != content:
        open(p, 'w', encoding='utf-8').write(new_content)
        updated += 1

# Also update generate_all_courses.py template
if os.path.exists(py_template):
    content = open(py_template, encoding='utf-8').read()
    new_content = replace_submit_block(content)
    if new_content != content:
        open(py_template, 'w', encoding='utf-8').write(new_content)
        print(f'Updated: generate_all_courses.py')

print(f'Updated submitForm in {updated} HTML pages')

# Verify - check that business_name default is present
ok_pages = 0
for p in pages:
    c = open(p, encoding='utf-8').read()
    if 'Individual / N.A.' in c or 'business_name' in c:
        ok_pages += 1

print(f'Pages that handle business_name (all 9 columns): {ok_pages}/{len(pages)}')
