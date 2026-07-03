"""
rollout_confetti.py
-------------------
Injects the Party Popup and Confetti animation into ALL 65 HTML pages
and updates the submitForm function to trigger it.
Also adds a 7-second auto-close to the popup.
"""
import glob, os, re

SITE_DIR = r'D:\Anti_gravity\kstrainings.com'
pages = glob.glob(os.path.join(SITE_DIR, '*.html'))
pages = [p for p in pages if 'admin' not in os.path.basename(p)]

# The HTML/CSS/JS for the popup and confetti
POPUP_BLOCK = """
<!-- ================= CONFETTI & POPUP ================= -->
<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
<style>
  .ks-success-overlay {
    position: fixed;
    top: 0; left: 0; width: 100%; height: 100%;
    background: transparent;
    z-index: 99999;
    display: none;
    align-items: center;
    justify-content: center;
    opacity: 0;
    transition: opacity 0.4s ease;
  }
  .ks-success-overlay.show {
    display: flex;
    opacity: 1;
  }
  .ks-success-modal {
    background: white;
    padding: 40px;
    border-radius: 20px;
    text-align: center;
    max-width: 450px;
    width: 90%;
    box-shadow: 0 25px 50px -12px rgba(0,0,0,0.5);
    transform: scale(0.8) translateY(20px);
    transition: all 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
  }
  .ks-success-overlay.show .ks-success-modal {
    transform: scale(1) translateY(0);
  }
  .ks-success-modal .check-icon {
    width: 80px; height: 80px;
    background: #10b981;
    color: white;
    font-size: 40px;
    line-height: 80px;
    border-radius: 50%;
    margin: 0 auto 20px auto;
    box-shadow: 0 0 20px rgba(16, 185, 129, 0.4);
    animation: popIn 0.6s cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
    animation-delay: 0.2s;
    opacity: 0;
    transform: scale(0);
  }
  @keyframes popIn {
    to { opacity: 1; transform: scale(1); }
  }
  .ks-success-modal h3 {
    font-size: 28px;
    color: #1e293b;
    margin-bottom: 10px;
    font-weight: 800;
  }
  .ks-success-modal p {
    color: #64748b;
    font-size: 16px;
    line-height: 1.6;
    margin-bottom: 25px;
  }
  .ks-success-modal .name-highlight {
    color: #2563eb;
    font-weight: 700;
  }
  .ks-success-modal button {
    background: #2563eb;
    color: white;
    border: none;
    padding: 14px 32px;
    border-radius: 50px;
    font-size: 16px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(37, 99, 235, 0.3);
  }
  .ks-success-modal button:hover {
    background: #1d4ed8;
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(37, 99, 235, 0.4);
  }
</style>

<div class="ks-success-overlay" id="ksSuccessOverlay">
  <div class="ks-success-modal">
    <div class="check-icon">✓</div>
    <h3>Awesome!</h3>
    <p>Thank you <span class="name-highlight" id="ksSuccessName"></span> for reaching out.<br>Our team will contact you very soon!</p>
    <button onclick="closeSuccessPopup()">Continue</button>
  </div>
</div>

<script>
  function closeSuccessPopup() {
    var overlay = document.getElementById('ksSuccessOverlay');
    if(overlay) {
      overlay.classList.remove('show');
      setTimeout(function() { overlay.style.display = 'none'; }, 400);
    }
  }
  function triggerParty(userName) {
    var overlay = document.getElementById('ksSuccessOverlay');
    if(!overlay) return;
    document.getElementById('ksSuccessName').textContent = userName || 'there';
    overlay.style.display = 'flex';
    setTimeout(function() { overlay.classList.add('show'); }, 10);

    // Auto-close after 7 seconds
    setTimeout(function() {
      closeSuccessPopup();
    }, 7000);

    // Confetti Animation
    var duration = 3 * 1000;
    var end = Date.now() + duration;
    (function frame() {
      confetti({
        particleCount: 5,
        angle: 60,
        spread: 55,
        origin: { x: 0 },
        colors: ['#2563eb', '#10b981', '#f59e0b', '#ef4444'],
        zIndex: 100000
      });
      confetti({
        particleCount: 5,
        angle: 120,
        spread: 55,
        origin: { x: 1 },
        colors: ['#2563eb', '#10b981', '#f59e0b', '#ef4444'],
        zIndex: 100000
      });
      if (Date.now() < end) {
        requestAnimationFrame(frame);
      }
    }());
  }
</script>
<!-- ================= END CONFETTI & POPUP ================= -->
</body>
"""

NEW_SHOW_OK = """    function showOK() {
      if(msgEl) msgEl.style.display = 'none';
      if(form) form.reset();
      if(btn) btn.disabled = false;
      if (typeof triggerParty === 'function') {
        triggerParty(name);
      }
    }"""

updated = 0
for p in pages:
    content = open(p, encoding='utf-8').read()
    original = content
    
    # 1. Add Popup Block before </body>
    if 'ks-success-overlay' not in content:
        content = content.replace('</body>', POPUP_BLOCK)
    else:
        # If already exists (like index.html), replace the old block with the new one
        content = re.sub(
            r'<!-- ================= CONFETTI & POPUP ================= -->.*?<!-- ================= END CONFETTI & POPUP ================= -->\s*</body>',
            POPUP_BLOCK,
            content,
            flags=re.DOTALL
        )

    # 2. Modify showOK in the submitForm script
    # Look for the showOK block inside submitForm
    show_ok_pattern = r'function showOK\(\)\s*\{.*?btn\.disabled = false;\s*\}'
    content = re.sub(show_ok_pattern, NEW_SHOW_OK, content, flags=re.DOTALL)

    if content != original:
        open(p, 'w', encoding='utf-8').write(content)
        updated += 1
        print(f'Updated: {os.path.basename(p)}')

# Also update the python generator template
gen = os.path.join(SITE_DIR, 'generate_all_courses.py')
if os.path.exists(gen):
    g_content = open(gen, encoding='utf-8').read()
    if 'ks-success-overlay' not in g_content:
        g_content = g_content.replace('</body>', POPUP_BLOCK)
        g_content = re.sub(r'function showOK\(\)\s*\{.*?btn\.disabled = false;\s*\}', NEW_SHOW_OK, g_content, flags=re.DOTALL)
        open(gen, 'w', encoding='utf-8').write(g_content)
        print('Updated: generate_all_courses.py')

print(f'\nRollout complete! {updated} HTML files updated with auto-closing popup.')
