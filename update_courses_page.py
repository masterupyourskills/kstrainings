import os

from generate_all_courses import courses_db

# Append the original static pages that are not dynamically generated so they still show up in the courses grid
static_courses = [
    {
        "filename": "vmware-training.html",
        "name": "VMware vSphere",
        "cat": "cloud",
        "badge": "Infrastructure",
        "icon": '<svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 17h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg>'
    },
    {
        "filename": "linux-training.html",
        "name": "Linux Administration",
        "cat": "cloud",
        "badge": "Infrastructure",
        "icon": '<svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 17h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg>'
    },
    {
        "filename": "sccm-training.html",
        "name": "SCCM",
        "cat": "cloud",
        "badge": "Infrastructure",
        "icon": '<svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 17h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg>'
    },
    {
        "filename": "ccna-training.html",
        "name": "CCNA Routing & Switching",
        "cat": "cloud",
        "badge": "Networking",
        "icon": '<svg viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 17h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg>'
    },
    {
        "filename": "sas-training.html",
        "name": "SAS Analytics",
        "cat": "data-analyst",
        "badge": "Analytics",
        "icon": '<svg viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2z"/></svg>'
    },
    {
        "filename": "abinitio-training.html",
        "name": "Ab Initio",
        "cat": "data-engineer",
        "badge": "ETL",
        "icon": '<svg viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2z"/></svg>'
    },
    {
        "filename": "splunk-training.html",
        "name": "Splunk Observability",
        "cat": "data-engineer",
        "badge": "Observability",
        "icon": '<svg viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2z"/></svg>'
    },
    {
        "filename": "dotnet-training.html",
        "name": ".NET / C# Development",
        "cat": "dev",
        "badge": "Backend",
        "icon": '<svg viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2z"/></svg>'
    },
    {
        "filename": "php-training.html",
        "name": "PHP Development",
        "cat": "dev",
        "badge": "Backend",
        "icon": '<svg viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2z"/></svg>'
    },
    {
        "filename": "oracle-sql-training.html",
        "name": "Oracle SQL / PL-SQL",
        "cat": "data-engineer",
        "badge": "Database",
        "icon": '<svg viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2z"/></svg>'
    }
]

all_courses = courses_db + static_courses

# Build grid HTML with logo embedded
grid_html = ""
for course in all_courses:
    tag_html = '<span class="tag">Trending</span>' if course.get("cat") in ["data-analyst", "data-science", "data-engineer", "video-editing", "photo-editing"] else '<span class="tag">Certification</span>'
    
    grid_html += f"""      <a href="{course['filename']}" class="course-card" data-cat="{course['cat']}">
        <div class="course-icon-wrap" style="width:36px; height:36px; fill:#7c3aed; margin-bottom:12px;">
          {course['icon']}
        </div>
        <span class="cat" style="font-size:0.7rem; font-weight:700; color:#7c3aed; text-transform:uppercase; letter-spacing:.06em;">{course.get('badge', 'IT Course')}</span>
        <h5 style="font-size:0.97rem; font-weight:700; color:#1a2456; margin: 4px 0;">{course['name']}</h5>
        <span class="meta" style="font-size:0.8rem; color:#9ca3af; margin-top:auto;">Live · Projects</span>
        {tag_html}
      </a>
"""

# Rebuild courses.html with standard template and the populated grid
courses_html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>IT Courses &amp; Certifications | KS Trainings</title>
<meta name="description" content="Explore live IT courses at KS Trainings — AWS, Azure, DevOps, Data Analyst, Data Engineering, Data Science, Video Editing, Photo Editing and more. Expert trainers, 100% placement assistance, on-job support.">
<link rel="canonical" href="https://kstrainings.com/courses.html">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
  *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
  html {{ scroll-behavior: smooth; }}
  body {{ font-family: 'Inter', 'Segoe UI', Arial, sans-serif; color: #1a2456; background: #fff; line-height: 1.6; }}
  a {{ text-decoration: none; color: inherit; }}

  /* TOP BAR */
  .top-bar {{ background: #1a2456; color: #fff; padding: 8px 0; font-size: 0.82rem; }}
  .top-bar-inner {{ max-width: 1200px; margin: 0 auto; padding: 0 20px; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 8px; }}
  .top-contact {{ display: flex; gap: 20px; align-items: center; flex-wrap: wrap; }}
  .top-contact a {{ color: #ccc; display: flex; align-items: center; gap: 6px; transition: color .2s; }}
  .top-contact a:hover {{ color: #f59e0b; }}

  /* HEADER */
  header {{ background: #fff; border-bottom: 1px solid #e5e7eb; position: sticky; top: 0; z-index: 100; box-shadow: 0 2px 8px rgba(0,0,0,.06); }}
  .header-inner {{ max-width: 1200px; margin: 0 auto; padding: 0 20px; display: flex; align-items: center; justify-content: space-between; height: 70px; }}
  .logo {{ display: flex; align-items: center; gap: 10px; }}
  .logo img {{ height: 48px; width: 48px; object-fit: contain; border-radius: 50%; }}
  .logo-name {{ font-size: 1.3rem; font-weight: 800; color: #1a2456; }}
  .logo-sub {{ font-size: 0.62rem; color: #6b7280; font-weight: 500; letter-spacing: .05em; text-transform: uppercase; }}
  nav {{ display: flex; align-items: center; gap: 4px; }}
  nav a {{ color: #374151; font-weight: 600; font-size: 0.85rem; padding: 8px 12px; border-radius: 6px; transition: .2s; text-transform: uppercase; letter-spacing: .02em; }}
  nav a:hover, nav a.active {{ color: #1a2456; background: #f3f4f6; }}
  .btn-demo {{ background: #1a2456 !important; color: #fff !important; padding: 10px 20px !important; border-radius: 6px; font-weight: 700 !important; }}
  .btn-demo:hover {{ background: #2563eb !important; }}
  .menu-toggle {{ display: none; background: none; border: 1.5px solid #d1d5db; padding: 8px 12px; border-radius: 6px; cursor: pointer; font-size: 1.1rem; color: #374151; }}

  /* PAGE HERO */
  .page-hero {{
    background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 50%, #7c3aed 100%);
    padding: 60px 0;
    text-align: center;
    color: #fff;
  }}
  .page-hero h1 {{ font-size: clamp(1.8rem, 3.5vw, 2.6rem); font-weight: 800; margin-bottom: 12px; }}
  .page-hero h1 span {{ color: #f59e0b; }}
  .page-hero p {{ color: rgba(255,255,255,.8); font-size: 1rem; max-width: 600px; margin: 0 auto 6px; }}
  .breadcrumb {{ font-size: .82rem; color: rgba(255,255,255,.6); margin-top: 16px; }}
  .breadcrumb a {{ color: rgba(255,255,255,.75); }}
  .breadcrumb a:hover {{ color: #fff; }}

  /* WHY US FEATURES */
  .why-section {{ padding: 70px 0; background: #fff; }}
  .section-inner {{ max-width: 1200px; margin: 0 auto; padding: 0 20px; }}
  .section-title {{ text-align: center; margin-bottom: 50px; }}
  .section-title h2 {{ font-size: 1.9rem; font-weight: 800; color: #1a2456; margin-bottom: 10px; }}
  .section-title p {{ color: #6b7280; max-width: 560px; margin: 0 auto; font-size: .93rem; }}
  .section-title .divider {{ width: 60px; height: 4px; background: #7c3aed; margin: 14px auto 0; border-radius: 2px; }}

  .why-grid {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 28px; }}
  .why-card {{
    padding: 30px 24px;
    border: 1px solid #e5e7eb;
    border-radius: 12px;
    background: #fff;
    transition: .25s;
    box-shadow: 0 2px 8px rgba(0,0,0,.04);
  }}
  .why-card:hover {{ transform: translateY(-5px); border-color: #7c3aed; box-shadow: 0 12px 30px rgba(124,58,237,.12); }}
  .why-icon {{
    width: 64px; height: 64px; border-radius: 14px;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.7rem; margin-bottom: 18px;
  }}
  .why-icon.blue {{ background: #1d4ed8; }}
  .why-icon.red {{ background: #dc2626; }}
  .why-icon.green {{ background: #16a34a; }}
  .why-icon.orange {{ background: #d97706; }}
  .why-icon.purple {{ background: #7c3aed; }}
  .why-icon.teal {{ background: #0d9488; }}
  .why-card h4 {{ font-size: 1.05rem; font-weight: 700; color: #1a2456; margin-bottom: 10px; }}
  .why-card p {{ color: #6b7280; font-size: .88rem; line-height: 1.7; }}

  /* COURSE LISTING */
  .courses-section {{ padding: 70px 0; background: #f9fafb; }}
  .course-tabs {{ display: flex; gap: 10px; flex-wrap: wrap; margin-bottom: 32px; }}
  .ctab {{ padding: 9px 20px; border-radius: 4px; border: 1.5px solid #d1d5db; background: #fff; color: #4b5563; font-weight: 600; font-size: .85rem; cursor: pointer; transition: .2s; }}
  .ctab:hover, .ctab.active {{ background: #7c3aed; color: #fff; border-color: #7c3aed; }}
  .courses-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 18px; }}
  .course-card {{
    background: #fff;
    border: 1px solid #e5e7eb;
    border-radius: 10px;
    padding: 22px 18px;
    transition: .2s;
    box-shadow: 0 2px 8px rgba(0,0,0,.04);
    display: flex; flex-direction: column; gap: 6px;
  }}
  .course-card:hover {{ transform: translateY(-3px); border-color: #7c3aed; box-shadow: 0 8px 24px rgba(124,58,237,.12); }}
  .course-card .cat {{ font-size: .7rem; font-weight: 700; color: #7c3aed; text-transform: uppercase; letter-spacing: .06em; }}
  .course-card h5 {{ font-size: .97rem; font-weight: 700; color: #1a2456; }}
  .course-card .meta {{ font-size: .8rem; color: #9ca3af; margin-top: auto; }}
  .course-card .tag {{ display: inline-block; font-size: .68rem; background: #eff6ff; color: #7c3aed; padding: 3px 8px; border-radius: 999px; font-weight: 600; margin-top: 6px; }}

  /* FOOTER */
  footer {{ background: #0f172a; color: #fff; padding: 60px 0 0; }}
  .footer-inner {{ max-width: 1200px; margin: 0 auto; padding: 0 20px; }}
  .footer-grid {{ display: grid; grid-template-columns: 1.8fr 1fr 1fr 1fr; gap: 40px; padding-bottom: 40px; }}
  .footer-brand p {{ color: rgba(255,255,255,.6); font-size: .88rem; margin-top: 12px; line-height: 1.7; }}
  .footer-logo-name {{ font-size: 1.4rem; font-weight: 800; color: #fff; }}
  .footer-col h5 {{ font-size: .88rem; font-weight: 700; text-transform: uppercase; letter-spacing: .08em; color: #a78bfa; margin-bottom: 16px; }}
  .footer-col a {{ display: block; color: rgba(255,255,255,.65); font-size: .88rem; margin-bottom: 10px; transition: .2s; }}
  .footer-col a:hover {{ color: #fff; }}
  .footer-bottom {{ border-top: 1px solid rgba(255,255,255,.1); padding: 20px 0; text-align: center; color: rgba(255,255,255,.5); font-size: .82rem; }}

  


  /* Unified Floating Widgets Styles (Glowing WhatsApp + Standardized Chatbot) */
  .whatsapp-float {{
    position: fixed;
    right: 22px;
    bottom: 22px;
    z-index: 999;
    background: #25d366;
    border-radius: 50%;
    width: 58px;
    height: 58px;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 0 0 0 rgba(37,211,102, 0.6);
    animation: wa-glow-animation 2s infinite;
    transition: transform .2s;
  }}
  .whatsapp-float:hover {{
    transform: scale(1.1);
  }}
  .whatsapp-float svg {{
    width: 32px;
    height: 32px;
    fill: #fff;
  }}
  @keyframes wa-glow-animation {{
    0% {{
      box-shadow: 0 0 0 0 rgba(37,211,102, 0.7);
    }}
    70% {{
      box-shadow: 0 0 0 20px rgba(37,211,102, 0);
    }}
    100% {{
      box-shadow: 0 0 0 0 rgba(37,211,102, 0);
    }}
  }}

  .chat-fab {{
    position: fixed;
    right: 22px;
    bottom: 90px;
    z-index: 999;
    background: linear-gradient(135deg, #7c3aed, #2563eb);
    color: #fff;
    border: none;
    border-radius: 50%;
    width: 58px;
    height: 58px;
    font-size: 1.5rem;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 4px 16px rgba(124,58,237,.3);
    cursor: pointer;
    transition: transform .2s;
  }}
  .chat-fab:hover {{
    transform: scale(1.1);
  }}
  .chat-fab .chat-dot {{
    position: absolute;
    top: 12px;
    right: 12px;
    width: 10px;
    height: 10px;
    background: #22c55e;
    border-radius: 50%;
    border: 2px solid #fff;
  }}

  .chat-panel {{
    position: fixed;
    right: 22px;
    bottom: 164px;
    width: 350px;
    height: 480px;
    background: #fff;
    border-radius: 16px;
    box-shadow: 0 10px 40px rgba(0,0,0,.15);
    z-index: 999;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    opacity: 0;
    pointer-events: none;
    transform: translateY(20px);
    transition: opacity 0.25s ease, transform 0.25s ease;
  }}
  .chat-panel.active {{
    opacity: 1;
    pointer-events: auto;
    transform: translateY(0);
  }}

  .chat-head {{
    background: linear-gradient(90deg, #7c3aed, #2563eb);
    padding: 16px;
    color: #fff;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }}
  .chat-head-info {{
    display: flex;
    align-items: center;
    gap: 10px;
  }}
  .chat-head-av {{
    width: 32px;
    height: 32px;
    border-radius: 50%;
    background: #fff;
    color: #7c3aed;
    display: grid;
    place-items: center;
    font-weight: 800;
    font-size: 0.85rem;
  }}
  .chat-head-text h4 {{
    font-size: 0.9rem;
    font-weight: 700;
    margin: 0;
  }}
  .chat-head-text span {{
    font-size: 0.72rem;
    opacity: 0.85;
    display: block;
  }}
  .chat-close {{
    background: none;
    border: none;
    color: #fff;
    cursor: pointer;
    font-size: 1.4rem;
    opacity: .8;
    transition: opacity .2s;
  }}
  .chat-close:hover {{
    opacity: 1;
  }}

  .chat-body {{
    flex: 1;
    padding: 16px;
    overflow-y: auto;
    display: flex;
    flex-direction: column;
    gap: 12px;
    background: #f8fafc;
  }}
  .msg-row {{
    display: flex;
    width: 100%;
    margin-bottom: 4px;
  }}
  .msg-row.bot {{
    justify-content: flex-start;
  }}
  .msg-row.user {{
    justify-content: flex-end;
  }}
  .msg-bubble {{
    max-width: 85%;
    padding: 10px 14px;
    border-radius: 12px;
    font-size: 0.88rem;
    line-height: 1.45;
  }}
  .msg-row.bot .msg-bubble {{
    background: #fff;
    border: 1px solid #e2e8f0;
    border-bottom-left-radius: 4px;
    color: #1a2456;
  }}
  .msg-row.user .msg-bubble {{
    background: #7c3aed;
    color: #fff;
    border-bottom-right-radius: 4px;
  }}

  .chat-quick {{
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    padding: 8px 12px;
    border-top: 1px solid #e2e8f0;
    background: #f8fafc;
  }}
  .chat-quick button {{
    font-size: 0.72rem;
    padding: 5px 10px;
    border-radius: 999px;
    border: 1px solid #cbd5e1;
    background: #fff;
    color: #475569;
    cursor: pointer;
    transition: all 0.2s;
    font-family: inherit;
    font-weight: 500;
  }}
  .chat-quick button:hover {{
    border-color: #7c3aed;
    color: #7c3aed;
    background: #faf5ff;
  }}

  .chat-foot {{
    padding: 12px;
    background: #fff;
    border-top: 1px solid #e2e8f0;
    display: flex;
    gap: 8px;
  }}
  .chat-input {{
    flex: 1;
    border: 1px solid #cbd5e1;
    border-radius: 999px;
    padding: 8px 14px;
    outline: none;
    font-size: 0.88rem;
    font-family: inherit;
    transition: border-color .2s;
  }}
  .chat-input:focus {{
    border-color: #7c3aed;
  }}
  .chat-send {{
    background: #7c3aed;
    color: #fff;
    border: none;
    border-radius: 50%;
    width: 36px;
    height: 36px;
    cursor: pointer;
    display: grid;
    place-items: center;
    transition: background .2s;
  }}
  .chat-send:hover {{
    background: #2563eb;
  }}

  /* RESPONSIVE */
  @media (max-width: 900px) {{
    .why-grid {{ grid-template-columns: repeat(2, 1fr); }}
    .courses-grid {{ grid-template-columns: repeat(2, 1fr); }}
    .footer-grid {{ grid-template-columns: 1fr 1fr; }}
    nav {{ display: none; }}
    nav.open {{ display: flex; flex-direction: column; position: absolute; top: 70px; left: 0; right: 0; background: #fff; border-top: 1px solid #e5e7eb; padding: 16px 20px; box-shadow: 0 8px 24px rgba(0,0,0,.1); gap: 4px; z-index: 99; }}
    .menu-toggle {{ display: block; }}
  }}
  @media (max-width: 560px) {{
    .why-grid {{ grid-template-columns: 1fr; }}
    .courses-grid {{ grid-template-columns: 1fr; }}
    .footer-grid {{ grid-template-columns: 1fr; }}
  }}
</style>
</head>
<body>

<!-- TOP BAR -->
<div class="top-bar">
  <div class="top-bar-inner">
    <div class="top-contact">
      <a href="mailto:info@kstrainings.com">&#9993; info@kstrainings.com</a>
      <a href="tel:+918675539226">&#128222; +91-8675539226</a>
    </div>
    <span style="color:rgba(255,255,255,.5);font-size:.8rem;">Explore Our IT Certification Courses</span>
  </div>
</div>

<!-- HEADER -->
<header>
  <div class="header-inner">
    <div class="logo">
      <img src="ks-logo.jpg" alt="KS Trainings Logo" onerror="this.style.display='none'">
      <div>
        <div class="logo-name">KS Trainings</div>
        <div class="logo-sub">An Online Training Portal</div>
      </div>
    </div>
    <nav id="mainNav">
      <a href="index.html">Home</a>
      <a href="courses.html" class="active">Courses</a>
      <a href="video-editing.html">Video Editing</a>
      <a href="social-media-management.html">Social Media</a>
      <a href="on-job-support.html">On-Job Support</a>
      <a href="#demo-form" class="btn-demo">Get Free Quote</a>
    </nav>
    <button class="menu-toggle" id="menuToggle" aria-label="Toggle menu">&#9776;</button>
  </div>
</header>

<!-- PAGE HERO -->
<section class="page-hero">
  <h1>Explore Our <span>IT Training Courses</span></h1>
  <p>Live, instructor-led training across diverse IT technologies — taught by real-time industry experts with 10+ years of experience.</p>
  <div class="breadcrumb">
    <a href="index.html">Home</a> &rsaquo; Courses
  </div>
</section>

<!-- WHY CHOOSE US FEATURES -->
<section class="why-section">
  <div class="section-inner">
    <div class="section-title">
      <h2>Why Learn With KS Trainings</h2>
      <p>Everything you need to launch or advance your IT career — from expert-led training to real projects and guaranteed placement support.</p>
      <div class="divider"></div>
    </div>
    <div class="why-grid">
      <div class="why-card">
        <div class="why-icon blue">
          <svg width="32" height="32" viewBox="0 0 24 24" fill="#fff"><path d="M19 3H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V5a2 2 0 0 0-2-2zm-7 3a1 1 0 1 1 0 2 1 1 0 0 1 0-2zm0 4a4 4 0 1 1 0 8 4 4 0 0 1 0-8z"/></svg>
        </div>
        <h4>Latest Courses</h4>
        <p>We don't train you on redundant IT courses. All our courses are the latest and in-demand. You learn only what you can apply in real job scenarios and live projects.</p>
      </div>
      <div class="why-card">
        <div class="why-icon red">
          <svg width="32" height="32" viewBox="0 0 24 24" fill="#fff"><path d="M20 4H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2zm0 14H4v-6h16zm0-8H4V6h16z"/></svg>
        </div>
        <h4>Virtual Classrooms</h4>
        <p>We provide both real and virtual instructions for our courses. Thus we cater to both working and non-working learners with flexible batch timings every day.</p>
      </div>
      <div class="why-card">
        <div class="why-icon green">
          <svg width="32" height="32" viewBox="0 0 24 24" fill="#fff"><path d="M12 2a5 5 0 1 0 0 10A5 5 0 0 0 12 2zm0 12c-5.33 0-8 2.67-8 4v2h16v-2c0-1.33-2.67-4-8-4z"/></svg>
        </div>
        <h4>Expert Trainers</h4>
        <p>All our trainers are experienced professionals with 10+ years of experience under their belt. Rest assured you would be taught by the best talent in the industry.</p>
      </div>
    </div>
  </div>
</section>

<!-- COURSE LISTING -->
<section class="courses-section">
  <div class="section-inner">
    <div class="section-title">
      <h2>All IT Courses</h2>
      <p>Browse our complete catalog of live, instructor-led IT courses. Click any course to view the syllabus, fees, and book a free demo class.</p>
      <div class="divider"></div>
    </div>

    <div class="course-tabs">
      <button class="ctab active" data-cat="all">All Courses</button>
      <button class="ctab" data-cat="cloud">Cloud &amp; DevOps</button>
      <button class="ctab" data-cat="data-analyst">Data Analyst</button>
      <button class="ctab" data-cat="data-engineer">Data Engineering</button>
      <button class="ctab" data-cat="data-science">Data Science</button>
      <button class="ctab" data-cat="video-editing">Video Editing</button>
      <button class="ctab" data-cat="photo-editing">Photo Editing</button>
      <button class="ctab" data-cat="dev">Development</button>
      <button class="ctab" data-cat="security">Security &amp; Testing</button>
    </div>

    <div class="courses-grid" id="courseGrid">
{grid_html}
    </div>
  </div>
</section>

<!-- FOOTER -->
<footer>
  <div class="footer-inner">
    <div class="footer-grid">
      <div class="footer-brand">
        <div class="footer-logo-name">KS Trainings</div>
        <p>IT training, video editing and social media management services. Trusted by 50,000+ professionals and 200+ brands worldwide. kstrainings.com</p>
      </div>
      <div class="footer-col">
        <h5>Quick Links</h5>
        <a href="index.html">Home</a>
        <a href="courses.html">IT Courses</a>
        <a href="video-editing.html">Video Editing</a>
        <a href="social-media-management.html">Social Media</a>
        <a href="on-job-support.html">On-Job Support</a>
        <a href="proxy-job-support.html">Proxy Support</a>
        <a href="proxy-interview-support.html">Interview Support</a>
      </div>
      <div class="footer-col">
        <h5>Our Services</h5>
        <a href="proxy-job-support.html">Daily Task Support</a>
        <a href="proxy-job-support.html">Bug Debugging</a>
        <a href="proxy-job-support.html">Code Optimization</a>
        <a href="proxy-interview-support.html">Interview Preparation</a>
      </div>
      <div class="footer-col">
        <h5>Contact Us</h5>
        <a href="tel:+918675539226">+91-8675539226</a>
        <a href="mailto:info@kstrainings.com">info@kstrainings.com</a>
        <a href="https://wa.me/918675539226" target="_blank">WhatsApp Us</a>
      </div>
    </div>
    <div class="footer-bottom">
      &copy; 2025 KS Trainings. All rights reserved. | kstrainings.com | Best Online IT Training Institute
    </div>
  </div>
</footer>

<!-- WHATSAPP FLOAT -->
<a href="https://wa.me/918675539226" target="_blank" class="whatsapp-float" title="Chat on WhatsApp" aria-label="Chat on WhatsApp">
  <svg viewBox="0 0 32 32"><path d="M16 2a13 13 0 0 0-11 20l-2 7 7-2a13 13 0 1 0 6-25zm0 24c-2 0-4-1-6-2l-1-1-4 1 1-4-1-1a11 11 0 1 1 11 7zm6-9c0-.2-.1-.4-.5-.6l-3-1c-.2 0-.4 0-.5.1l-1 2c-.2.1-.4.1-.7 0a8 8 0 0 1-4-4c-.1-.3 0-.5.2-.7l1-1c.1-.2.2-.4.1-.6l-1-3c-.1-.3-.3-.4-.5-.4h-.5c-.3 0-.7.1-1 .5a4 4 0 0 0-1 3c0 2 1 4 2 5 2 3 5 5 8 6 1 0 3 0 4-1 .4-.4.6-1 .6-1 0-.2-.1-.4-.5-.6z"/></svg>
</a>

<!-- CHATBOT -->
<button class="chat-fab" id="chatFab" aria-label="Open chat assistant">
  <svg viewBox="0 0 24 24" width="26" height="26" fill="#fff"><path d="M20 2H4a2 2 0 0 0-2 2v18l4-4h14a2 2 0 0 0 2-2V4a2 2 0 0 0-2-2zm0 14H6l-2 2V4h16v12z"/></svg>
  <span class="chat-dot"></span>
</button>
<div class="chat-panel" id="chatPanel" role="dialog" aria-label="KS Trainings Chat Assistant">
  <div class="chat-head">
    <div class="chat-head-info">
      <div class="chat-head-av">KS</div>
      <div class="chat-head-text">
        <h4>KS Trainings Assistant</h4>
        <span>Online - Replies instantly</span>
      </div>
    </div>
    <button class="chat-close" id="chatClose" aria-label="Close chat">&times;</button>
  </div>
  <div class="chat-body" id="chatBody"></div>
  <div class="chat-quick" id="chatQuick">
    <button data-q="What are the class schedules?">Batch Timings</button>
    <button data-q="What are the course fees?">Fees Guide</button>
    <button data-q="Do we get course certificates?">Certification</button>
    <button data-q="I want a free live demo class">Demo Session</button>
    <button data-q="How do I contact you?">Contact</button>
  </div>
  <div class="chat-foot">
    <input type="text" class="chat-input" id="chatInput" placeholder="Type your message..." autocomplete="off">
    <button class="chat-send" id="chatSend" aria-label="Send message">➤</button>
  </div>
</div>

<script>
  // Mobile nav toggle
  (function() {{
    var menuToggle = document.getElementById('menuToggle');
    var mainNav = document.getElementById('mainNav');
    if (menuToggle && mainNav) {{
      menuToggle.onclick = function() {{
        mainNav.classList.toggle('open');
      }};
    }}
  }})();

  // Course tabs
  (function() {{
    const ctabs = document.querySelectorAll('.ctab');
    const cards = document.querySelectorAll('#courseGrid .course-card');
    ctabs.forEach(tab => {{
      tab.onclick = function() {{
        ctabs.forEach(t => t.classList.remove('active'));
        tab.classList.add('active');
        const cat = tab.dataset.cat;
        cards.forEach(c => {{
          c.style.display = (cat === 'all' || c.dataset.cat === cat) ? 'flex' : 'none';
        }});
      }};
    }});
  }})();

  // Chatbot logic
  (function() {{
    var chatFab = document.getElementById('chatFab');
    var chatPanel = document.getElementById('chatPanel');
    var chatClose = document.getElementById('chatClose');
    var chatInput = document.getElementById('chatInput');
    var chatBody = document.getElementById('chatBody');
    var chatSend = document.getElementById('chatSend');
    var chatQuick = document.getElementById('chatQuick');
    var chatGreeted = false;

    if (!chatFab || !chatPanel || !chatClose || !chatInput || !chatBody || !chatSend) return;

    function openChat() {{
      chatPanel.classList.add('active');
      if (!chatGreeted) {{
        chatGreeted = true;
        botSay("Hello! Welcome to KS Trainings. How can I help you with IT certification training today?");
      }}
      chatInput.focus();
    }}
    
    chatFab.onclick = function() {{
      if (chatPanel.classList.contains('active')) {{
        chatPanel.classList.remove('active');
      }} else {{
        openChat();
      }}
    }};
    
    chatClose.onclick = function() {{
      chatPanel.classList.remove('active');
    }};

    function addMsg(who, html) {{
      var row = document.createElement('div');
      row.className = 'msg-row ' + who;
      row.innerHTML = '<div class="msg-bubble">' + html + '</div>';
      chatBody.appendChild(row);
      chatBody.scrollTop = chatBody.scrollHeight;
    }}
    
    function botSay(html) {{
      setTimeout(function() {{ addMsg('bot', html); }}, 400);
    }}

    function botReply(text) {{
      var m = text.toLowerCase();
      if(/course|demo|trial|free/.test(m))
        return "You can book a free demo class for our IT training programs. Fill the form on this page or message us directly on WhatsApp.";
      if(/contact|call|phone|email|reach|whatsapp/.test(m))
        return "Mobile/WhatsApp: +91-8675539226<br>Email: info@kstrainings.com. We are available 24/7!";
      if(/support|on.?job|proxy|interview/.test(m))
        return "We offer expert on-job and proxy support for IT training. Fill the form on this page to get a quote within 2 hours.";
      if(/hi|hello|hey/.test(m))
        return "Hello! How can I help you with IT training or support today?";
      return "Thank you for your message. For immediate support and free session bookings, please call/WhatsApp us at +91-8675539226.";
    }}

    function sendChat(q){{
      if(!q.trim()) return;
      addMsg('user', q.replace(/</g,'&lt;'));
      chatInput.value = '';
      botSay(botReply(q));
    }}
    
    chatSend.onclick = function() {{ sendChat(chatInput.value); }};
    chatInput.onkeypress = function(e) {{
      if (e.key === 'Enter') {{
        e.preventDefault();
        sendChat(chatInput.value);
      }}
    }};
    
    if (chatQuick) {{
      chatQuick.onclick = function(e) {{
        var btn = e.target.closest('button');
        if (btn) {{
          e.preventDefault();
          sendChat(btn.getAttribute('data-q') || btn.textContent);
        }}
      }};
    }}
  }})();
</script>
</body>
</html>"""

with open(r"D:\Anti_gravity\WEB_SITE\courses.html", 'w', encoding='utf-8') as f:
    f.write(courses_html_content)

print("courses.html generated successfully with all cards and logos!")
