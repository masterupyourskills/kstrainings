"""Inject Google Sheets submitForm into remaining legacy training pages."""
import sys, re, os
sys.stdout.reconfigure(encoding='utf-8')

APPS_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbx4Ip9MnWcXhBuPr-wJ6SvYev2skqSpWdGBaz8mlccyGNF6H4VN1db28DVmdc7twp7I/exec'
SITE_DIR = r'D:\Anti_gravity\kstrainings.com'

legacy_files = [
    'abinitio-training.html',
    'ccna-training.html',
    'dotnet-training.html',
    'linux-training.html',
    'oracle-sql-training.html',
    'php-training.html',
    'sas-training.html',
    'sccm-training.html',
    'splunk-training.html',
    'vmware-training.html',
]

new_submit = """
  // ===== GOOGLE SHEETS FORM SUBMISSION =====
  var KS_APPS_SCRIPT_URL = '""" + APPS_SCRIPT_URL + """';
  function submitForm(formOrEvent) {
    var form = (formOrEvent && formOrEvent.target) ? formOrEvent.target : formOrEvent;
    if (formOrEvent && typeof formOrEvent.preventDefault === 'function') formOrEvent.preventDefault();
    var msgEl = document.getElementById('ksFormMsg');
    var btn = document.getElementById('ksSubmitBtn');
    if (!msgEl || !btn) return;
    if (form.elements['website'] && form.elements['website'].value !== '') return;
    var c = form.elements['captcha'];
    if (c && c.value.trim() !== '7') {
      msgEl.style.cssText = 'display:block;background:#fee2e2;color:#b91c1c;padding:12px 16px;border-radius:8px;font-size:.9rem;font-weight:600;margin-top:14px;';
      msgEl.textContent = 'Anti-spam check failed. Answer is 7.'; return;
    }
    var name = (form.elements['name'] ? form.elements['name'].value.trim() : '');
    var email = (form.elements['email'] ? form.elements['email'].value.trim() : '');
    var phone = (form.elements['phone'] ? form.elements['phone'].value.trim() : '');
    var course = (form.elements['course'] ? form.elements['course'].value.trim() : '');
    var serviceType = (form.elements['service_type'] ? form.elements['service_type'].value : '');
    var supportType = serviceType;
    var description = (form.elements['description'] ? form.elements['description'].value.trim() : '');
    var pageName = (form.getAttribute('data-page') || document.title || 'Course Page').split('|')[0].trim();
    btn.disabled = true;
    msgEl.style.cssText = 'display:block;background:#eff6ff;color:#1d4ed8;padding:12px 16px;border-radius:8px;font-size:.9rem;font-weight:600;margin-top:14px;';
    msgEl.textContent = 'Submitting...';
    try {
      var rec = {id:Date.now(),submitted_at:new Date().toLocaleString('en-IN'),page:pageName,name:name,email:email,phone:phone,course_service:course||serviceType,support_type:supportType,description:description,status:'New'};
      var all = JSON.parse(localStorage.getItem('ks_submissions')||'[]'); all.unshift(rec); localStorage.setItem('ks_submissions',JSON.stringify(all));
    } catch(e) {}
    function showOK() {
      msgEl.style.cssText = 'display:block;background:#dcfce7;color:#15803d;padding:12px 16px;border-radius:8px;font-size:.9rem;font-weight:600;margin-top:14px;';
      msgEl.textContent = 'Thank you ' + (name||'there') + '! Our team will contact you at ' + (phone||email) + ' within 24 hours.';
      form.reset(); btn.disabled = false;
    }
    if (KS_APPS_SCRIPT_URL && KS_APPS_SCRIPT_URL !== 'https://script.google.com/macros/s/AKfycbx4Ip9MnWcXhBuPr-wJ6SvYev2skqSpWdGBaz8mlccyGNF6H4VN1db28DVmdc7twp7I/exec') {
      fetch(KS_APPS_SCRIPT_URL, {method:'POST',body:JSON.stringify({page_name:pageName,name:name,email:email,phone:phone,course_service:course||serviceType,support_type:supportType,description:description}),headers:{'Content-Type':'text/plain'}})
      .then(function(r){return r.json();}).then(function(){showOK();}).catch(function(){showOK();});
    } else { showOK(); }
  }
  // ===== END GOOGLE SHEETS FORM SUBMISSION =====
"""

for fname in legacy_files:
    fpath = os.path.join(SITE_DIR, fname)
    if not os.path.exists(fpath):
        print(f'SKIP (not found): {fname}')
        continue
    content = open(fpath, 'r', encoding='utf-8').read()
    if 'KS_APPS_SCRIPT_URL' in content:
        print(f'ALREADY DONE: {fname}')
        continue
    # Find and inject into the last inline script block
    script_positions = list(re.finditer(r'<script(?:\s[^>]*)?>.*?</script>', content, re.DOTALL))
    inline = [m for m in script_positions if 'src=' not in m.group(0)]
    if inline:
        last = inline[-1]
        inner_start = last.start() + last.group(0).index('>') + 1
        content = content[:inner_start] + '\n' + new_submit + '\n' + content[inner_start:]
    else:
        content = content.replace('</body>', '<script>\n' + new_submit + '\n</script>\n</body>', 1)
    # Add data-page to forms
    page_label = fname.replace('-training.html','').replace('.html','').replace('-',' ').title() + ' Training'
    content = re.sub(
        r'(<form\b(?![^>]*data-page)[^>]*)(>)',
        lambda m, pl=page_label: m.group(1) + f' data-page="{pl}"' + m.group(2),
        content
    )
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Updated: {fname}')

print('Done!')
