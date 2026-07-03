"""
add_confetti_test.py
---------------------
Adds a full-screen Confetti Party + Thank You Popup to index.html for testing.
"""
import re, os

SITE_DIR = r'D:\Anti_gravity\kstrainings.com'
index_file = os.path.join(SITE_DIR, 'index.html')

content = open(index_file, encoding='utf-8').read()

# 1. Add confetti script + custom styles + popup HTML right before </body>
popup_html_css = """
<!-- ================= CONFETTI & POPUP ================= -->
<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
<style>
  .ks-success-overlay {
    position: fixed;
    top: 0; left: 0; width: 100%; height: 100%;
    background: rgba(15, 23, 42, 0.85);
    backdrop-filter: blur(8px);
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
    overlay.classList.remove('show');
    setTimeout(function() { overlay.style.display = 'none'; }, 400);
  }
  function triggerParty(userName) {
    var overlay = document.getElementById('ksSuccessOverlay');
    document.getElementById('ksSuccessName').textContent = userName || 'there';
    overlay.style.display = 'flex';
    setTimeout(function() { overlay.classList.add('show'); }, 10);

    // Confetti Animation
    var duration = 3 * 1000;
    var end = Date.now() + duration;
    (function frame() {
      confetti({
        particleCount: 5,
        angle: 60,
        spread: 55,
        origin: { x: 0 },
        colors: ['#2563eb', '#10b981', '#f59e0b', '#ef4444']
      });
      confetti({
        particleCount: 5,
        angle: 120,
        spread: 55,
        origin: { x: 1 },
        colors: ['#2563eb', '#10b981', '#f59e0b', '#ef4444']
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

if 'ksSuccessOverlay' not in content:
    content = content.replace('</body>', popup_html_css)

# 2. Modify showOK() inside the submitForm block
old_show_ok = """    function showOK() {
      msgEl.style.cssText = 'display:block;background:#dcfce7;color:#15803d;padding:12px 16px;border-radius:8px;font-size:.9rem;font-weight:600;margin-top:14px;';
      msgEl.textContent = 'Thank you ' + (name || 'there') + '! Our team will contact you at ' + (phone || email) + ' within 24 hours.';
      form.reset();
      btn.disabled = false;
    }"""

new_show_ok = """    function showOK() {
      // Hide the default inline message and show the party popup instead!
      msgEl.style.display = 'none';
      form.reset();
      btn.disabled = false;
      if (typeof triggerParty === 'function') {
        triggerParty(name);
      }
    }"""

if old_show_ok in content:
    content = content.replace(old_show_ok, new_show_ok)
else:
    print("Warning: Could not find exactly old showOK(). Attempting regex replace...")
    content = re.sub(
        r'function showOK\(\)\s*\{.*?btn\.disabled = false;\s*\}',
        new_show_ok.strip(),
        content,
        flags=re.DOTALL
    )

open(index_file, 'w', encoding='utf-8').write(content)
print("Updated index.html with Party Popup!")
