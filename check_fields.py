import re, os

pages_to_check = [
    'index.html',
    'sql-training.html',
    'on-job-support.html',
    'proxy-job-support.html',
    'proxy-interview-support.html',
    'social-media-management.html',
    'video-editing.html',
    'aws-training.html',
    'vmware-training.html'
]

for fname in pages_to_check:
    if not os.path.exists(fname):
        continue
    content = open(fname, encoding='utf-8').read()
    fields = re.findall(r'name=["\']([\w_]+)["\']', content)
    fields = [f for f in set(fields) if f not in ('website','captcha','_replyto')]
    has_biz = 'business_name' in fields
    print(f'{fname}:')
    print(f'  Fields: {sorted(fields)}')
    print(f'  Has business_name: {has_biz}')
    print()
