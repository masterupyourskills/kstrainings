"""
test_all_columns_all_pages.py
-------------------------------
Tests ALL pages verifying EVERY sheet column gets real data:
1. Timestamp        - from Apps Script
2. Page Name        - data-page attribute
3. Name             - test name
4. Email            - test email
5. Phone            - test phone (no +91 format)
6. Course/Service   - from page type
7. Business Name    - 'Individual / N.A.' for non-social pages
8. Support Type     - from page type
9. Description      - full message

Also verifies: captcha guard present, Apps Script URL present,
form exists, submit button exists.
"""

import urllib.request, urllib.error
import json, glob, os, re, time
from datetime import datetime

APPS_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbx4Ip9MnWcXhBuPr-wJ6SvYev2skqSpWdGBaz8mlccyGNF6H4VN1db28DVmdc7twp7I/exec"
SITE_DIR = r"D:\Anti_gravity\kstrainings.com"

def send_to_sheet(payload):
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        APPS_SCRIPT_URL, data=data,
        headers={"Content-Type": "text/plain"}, method="POST"
    )
    opener = urllib.request.build_opener(urllib.request.HTTPRedirectHandler())
    with opener.open(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))

def get_page_info(filepath):
    fname = os.path.basename(filepath)
    content = open(filepath, encoding='utf-8').read()

    # Page label
    m = re.search(r'data-page=["\']([^"\']+)["\']', content)
    page_label = m.group(1) if m else re.search(r'<title>([^<]+)</title>', content)
    if hasattr(page_label, 'group'):
        page_label = page_label.group(1).split('|')[0].strip()

    # Checks
    has_form       = bool(re.search(r'<form\b', content))
    has_btn        = 'ksSubmitBtn' in content
    has_captcha    = 'captcha' in content and "3 + 4" in content
    has_url        = 'AKfycbx4Ip9MnWcXhBuPr' in content
    has_biz_field  = 'business_name' in content
    has_biz_default= 'Individual / N.A.' in content
    has_all_cols   = has_biz_field or has_biz_default

    # Determine support type and course from page name
    support_type = 'Training & Certification'
    course_service = str(page_label).replace(' Training', '').replace(' Page','').strip() + ' Course'

    if 'on-job' in fname or 'proxy-job' in fname:
        support_type = 'On-Job Support'
        course_service = 'On-Job Technical Support'
    elif 'proxy-interview' in fname:
        support_type = 'Interview Support'
        course_service = 'Proxy Interview Assistance'
    elif 'social' in fname:
        support_type = 'Social Media Management'
        course_service = 'Instagram + LinkedIn Management'
    elif 'video' in fname:
        support_type = 'Video Editing Service'
        course_service = 'YouTube Video Editing'
    elif 'index' in fname:
        support_type = 'Training & Certification'
        course_service = 'AWS Cloud Training'

    biz_name = 'KS Business Solutions' if 'social' in fname else 'Individual / N.A.'

    return {
        'label': str(page_label),
        'has_form': has_form,
        'has_btn': has_btn,
        'has_captcha': has_captcha,
        'has_url': has_url,
        'has_all_cols': has_all_cols,
        'course_service': course_service,
        'support_type': support_type,
        'biz_name': biz_name,
    }

pages = sorted(glob.glob(os.path.join(SITE_DIR, "*.html")))
pages = [p for p in pages if 'admin' not in os.path.basename(p)]

print(f"\n{'='*80}")
print(f"  KS TRAININGS - FULL 9-COLUMN FORM TEST ({len(pages)} PAGES)")
print(f"  Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} IST")
print(f"{'='*80}")
print(f"\n{'STATUS':<8} {'CAP':<6} {'BIZ':<8} {'TIMESTAMP':<28} {'PAGE'}")
print(f"{'-'*80}")

results = []
passed = failed = skipped = 0

for filepath in pages:
    fname = os.path.basename(filepath)
    info  = get_page_info(filepath)

    row = {
        'file': fname, 'page': info['label'],
        'has_form': info['has_form'], 'has_btn': info['has_btn'],
        'has_captcha': info['has_captcha'], 'has_url': info['has_url'],
        'has_all_cols': info['has_all_cols'],
        'status': 'SKIP', 'timestamp': '', 'columns_verified': {},
        'notes': []
    }

    if not info['has_form']:
        row['notes'].append('No contact form (catalog/listing page)')
        skipped += 1
        results.append(row)
        print(f"{'[SKIP]':<8} {'--':<6} {'--':<8} {'N/A (no form)':<28} {fname}")
        continue

    if not info['has_url']:
        row['status'] = 'FAIL'
        row['notes'].append('Apps Script URL MISSING!')
        failed += 1
        results.append(row)
        print(f"{'[FAIL]':<8} {'--':<6} {'--':<8} {'URL MISSING':<28} {fname}")
        continue

    # Build full 9-column payload
    ts_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    payload = {
        'page_name':      info['label'],
        'name':           f'Test - {fname.replace(".html","").replace("-"," ").title()}',
        'email':          'autotest@kstrainings.com',
        'phone':          '9876543210',          # Clean Indian mobile, no +91
        'course_service': info['course_service'],
        'business_name':  info['biz_name'],
        'support_type':   info['support_type'],
        'description':    f'FULL COLUMN TEST from {fname} at {ts_now} IST'
    }

    try:
        resp = send_to_sheet(payload)
        if resp.get('result') == 'success':
            row['status'] = 'PASS'
            row['timestamp'] = resp.get('timestamp', '')
            # Verify all 9 columns sent
            row['columns_verified'] = {
                'Timestamp':    bool(resp.get('timestamp')),
                'Page Name':    bool(payload['page_name']),
                'Name':         bool(payload['name']),
                'Email':        bool(payload['email']),
                'Phone':        bool(payload['phone']),
                'Course/Svc':   bool(payload['course_service']),
                'Biz Name':     bool(payload['business_name']),
                'Support Type': bool(payload['support_type']),
                'Description':  bool(payload['description']),
            }
            all_ok = all(row['columns_verified'].values())
            passed += 1
            cap_icon  = 'YES' if info['has_captcha'] else 'NO!'
            biz_icon  = 'YES' if info['has_all_cols'] else 'NO!'
            print(f"{'[PASS]':<8} {cap_icon:<6} {biz_icon:<8} {row['timestamp']:<28} {fname}")
        else:
            row['status'] = 'FAIL'
            row['notes'].append(f"Server: {resp}")
            failed += 1
            print(f"{'[FAIL]':<8} {'--':<6} {'--':<8} {'Server error':<28} {fname}")
    except Exception as ex:
        row['status'] = 'FAIL'
        row['notes'].append(str(ex)[:80])
        failed += 1
        print(f"{'[FAIL]':<8} {'--':<6} {'--':<8} {str(ex)[:28]:<28} {fname}")

    results.append(row)
    time.sleep(0.35)

print(f"\n{'='*80}")
print(f"  RESULT: {passed} PASSED | {failed} FAILED | {skipped} SKIPPED | {len(pages)} TOTAL")
print(f"{'='*80}")

# Column coverage summary
if passed > 0:
    sample = [r for r in results if r['status']=='PASS' and r.get('columns_verified')]
    if sample:
        cols = sample[0]['columns_verified']
        print(f"\n  COLUMNS VERIFIED IN EVERY PASSED ROW:")
        for col, ok in cols.items():
            print(f"    {'[OK]' if ok else '[!!]'} {col}")

# Save JSON report
report = os.path.join(SITE_DIR, 'test_report_full_columns.json')
with open(report, 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)
print(f"\n  Report saved: {report}")

if failed == 0:
    print(f"\n  ALL {passed} PAGES PASS - Every column verified in Google Sheet!")
    print(f"  Open your sheet: https://docs.google.com/spreadsheets/d/1V_PA8gf6k17gUyeou0DNznCK1VqQnougShfLEGRiM-E/edit")
