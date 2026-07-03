import re
for fname in ['sql-training.html', 'on-job-support.html', 'index.html', 'proxy-job-support.html']:
    content = open(fname, encoding='utf-8').read()
    lines = content.splitlines()
    for line in lines:
        if 'type="tel"' in line or "type='tel'" in line:
            print(f'{fname}:  {line.strip()[:120]}')
