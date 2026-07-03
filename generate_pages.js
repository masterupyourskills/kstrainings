const fs = require('fs');

const courses = [
  { file: 'aws-training.html', name: 'AWS', cat: 'Cloud' },
  { file: 'azure-training.html', name: 'Microsoft Azure', cat: 'Cloud' },
  { file: 'gcp-training.html', name: 'Google Cloud', cat: 'Cloud' },
  { file: 'devops-training.html', name: 'DevOps', cat: 'DevOps' },
  { file: 'vmware-training.html', name: 'VMware vSphere', cat: 'Infra' },
  { file: 'linux-training.html', name: 'Linux Administration', cat: 'Infra' },
  { file: 'sccm-training.html', name: 'SCCM', cat: 'Infra' },
  { file: 'ccna-training.html', name: 'CCNA R&S', cat: 'Network' },
  { file: 'data-science-training.html', name: 'Data Science', cat: 'Data' },
  { file: 'tableau-training.html', name: 'Tableau', cat: 'BI' },
  { file: 'powerbi-training.html', name: 'Power BI', cat: 'BI' },
  { file: 'sas-training.html', name: 'SAS', cat: 'Analytics' },
  { file: 'abinitio-training.html', name: 'Ab Initio', cat: 'ETL' },
  { file: 'splunk-training.html', name: 'Splunk', cat: 'Ops' },
  { file: 'salesforce-training.html', name: 'Salesforce', cat: 'CRM' },
  { file: 'servicenow-training.html', name: 'ServiceNow', cat: 'ITSM' },
  { file: 'guidewire-training.html', name: 'Guidewire', cat: 'Insurance' },
  { file: 'pega-training.html', name: 'Pega', cat: 'BPM' },
  { file: 'mulesoft-training.html', name: 'MuleSoft', cat: 'Integration' },
  { file: 'sap-hybris-training.html', name: 'SAP Hybris', cat: 'Commerce' },
  { file: 'oracle-hcm-training.html', name: 'Oracle Fusion HCM', cat: 'ERP' },
  { file: 'adobe-aem-training.html', name: 'Adobe AEM', cat: 'CMS' },
  { file: 'java-training.html', name: 'Java', cat: 'Dev' },
  { file: 'python-training.html', name: 'Python (Django)', cat: 'Dev' },
  { file: 'dotnet-training.html', name: 'NET', cat: 'Dev' },
  { file: 'php-training.html', name: 'PHP', cat: 'Dev' },
  { file: 'ui-developer-training.html', name: 'UI Developer', cat: 'Frontend' },
  { file: 'oracle-sql-training.html', name: 'Oracle SQL / PL-SQL', cat: 'DB' },
  { file: 'ethical-hacking-training.html', name: 'Ethical & Web-App Hacking', cat: 'Security' },
  { file: 'cyberark-training.html', name: 'CyberArk', cat: 'Security' },
  { file: 'selenium-training.html', name: 'Selenium', cat: 'Testing' },
  { file: 'agile-scrum-training.html', name: 'Agile Scrum Master', cat: 'Agile' }
];

const template = (course) => `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>${course.name} Training & Certification | KS Trainings</title>
<meta name="description" content="Master ${course.name} with KS Trainings. Get live, instructor-led training from real-time experts with 100% job support and placement assistance. Start your ${course.name} career today.">
<meta name="keywords" content="${course.name} training, online ${course.name} course, ${course.name} certification, KS Trainings, IT courses">
<style>
  :root{
    --bg:#ffffff;
    --bg-2:#f4f7fc;
    --card:#ffffff;
    --line:#e6ebf3;
    --text:#0f172a;
    --muted:#5b6b86;
    --brand:#3b5bff;
    --brand-2:#0ea5e9;
    --accent:#7c3aed;
    --radius:16px;
    --max:1140px;
    --shadow:0 10px 30px rgba(20,40,90,.08);
  }
  *{box-sizing:border-box;margin:0;padding:0}
  body{
    font-family:'Segoe UI',system-ui,-apple-system,Roboto,Helvetica,Arial,sans-serif;
    background:var(--bg);color:var(--text);line-height:1.6;
    -webkit-font-smoothing:antialiased;
  }
  a{color:inherit;text-decoration:none}
  .wrap{max-width:var(--max);margin:0 auto;padding:0 22px}
  .grad-text{background:linear-gradient(90deg,var(--brand),var(--brand-2));-webkit-background-clip:text;background-clip:text;color:transparent}
  .btn{
    display:inline-block;padding:13px 26px;border-radius:999px;font-weight:600;
    border:1px solid transparent;transition:.2s transform,.2s box-shadow;cursor:pointer;
  }
  .btn:hover{transform:translateY(-2px)}
  .btn-primary{background:linear-gradient(90deg,var(--brand),var(--accent));color:#fff;box-shadow:0 10px 30px rgba(108,140,255,.35)}
  .btn-ghost{border:1px solid var(--line);color:var(--text);background:#fff}
  section{padding:84px 0}
  .eyebrow{color:var(--brand-2);font-weight:700;letter-spacing:.14em;text-transform:uppercase;font-size:.78rem}
  h2.title{font-size:clamp(1.8rem,3.4vw,2.6rem);margin:10px 0 14px;line-height:1.15}
  .sub{color:var(--muted);max-width:640px}

  /* Header */
  header{position:sticky;top:0;z-index:50;backdrop-filter:blur(12px);
    background:rgba(255,255,255,.82);border-bottom:1px solid var(--line)}
  .nav{display:flex;align-items:center;justify-content:space-between;height:70px}
  .logo{display:flex;align-items:center;gap:10px;font-weight:800;font-size:1.2rem}
  .logo .mark{width:34px;height:34px;border-radius:9px;background:linear-gradient(135deg,var(--brand),var(--brand-2));display:grid;place-items:center;color:#06112b;font-weight:900}
  .nav-links{display:flex;gap:28px;align-items:center}
  .nav-links a{color:var(--muted);font-weight:500;font-size:.95rem;transition:.2s}
  .nav-links a:hover{color:var(--text)}

  /* Hero */
  .hero{position:relative;overflow:hidden;padding:96px 0 70px;background:var(--bg-2)}
  .hero h1{font-size:clamp(2.2rem,5vw,3.5rem);line-height:1.08;letter-spacing:-.02em}
  .hero p.lead{color:var(--muted);font-size:1.12rem;margin:20px 0 30px;max-width:560px}

  /* Content */
  .content-section{padding:60px 0}
  .content-section p { margin-bottom: 20px; }
  .content-section ul { margin-left: 20px; margin-bottom: 20px; }

  /* Footer */
  footer{border-top:1px solid var(--line);padding:48px 0 28px;background:var(--bg-2)}
  .foot-grid{display:grid;grid-template-columns:1.5fr 1fr 1fr 1fr;gap:28px}
  footer h5{font-size:.95rem;margin-bottom:14px}
  footer a{display:block;color:var(--muted);font-size:.9rem;margin-bottom:8px;transition:.2s}
  footer a:hover{color:var(--text)}
  .copy{margin-top:34px;padding-top:20px;border-top:1px solid var(--line);color:var(--muted);font-size:.85rem;text-align:center}

  @media (max-width:900px){
    .foot-grid{grid-template-columns:1fr 1fr}
    .nav-links{display:none}
  }
</style>
</head>
<body>

<header>
  <div class="wrap nav">
    <a href="index.html" class="logo"><span class="mark">KS</span> KS Trainings</a>
    <nav class="nav-links">
      <a href="index.html#courses">Courses</a>
      <a href="index.html#features">Why Us</a>
      <a href="index.html#contact">Contact</a>
      <a href="index.html#demo" class="btn btn-primary" style="padding:9px 20px">Free Demo</a>
    </nav>
  </div>
</header>

<section class="hero">
  <div class="wrap">
    <span class="eyebrow">${course.cat} Course</span>
    <h1>Master <span class="grad-text">${course.name}</span> Training</h1>
    <p class="lead">Join our industry-leading ${course.name} certification program. Learn from working professionals and get 100% job support and placement assistance.</p>
    <a href="index.html#demo" class="btn btn-primary">Book a Free Demo</a>
  </div>
</section>

<section class="content-section wrap">
  <h2>Why Learn ${course.name}?</h2>
  <p>${course.name} is one of the most highly demanded skills in the IT industry today. By mastering ${course.name}, you unlock lucrative career opportunities across top enterprises globally.</p>
  
  <h2>Course Features</h2>
  <ul>
    <li>Real-time projects and hands-on scenarios</li>
    <li>Experienced industry trainers</li>
    <li>Flexible online & classroom timings</li>
    <li>Interview preparation and resume building</li>
    <li>Dedicated placement cell</li>
  </ul>
</section>

<footer>
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <div class="logo" style="margin-bottom:12px"><span class="mark">KS</span> KS Trainings</div>
        <p style="color:var(--muted);font-size:.9rem;max-width:300px">Your one-stop solution for IT course training — live, expert-led, with on-job support and placement assistance across the globe.</p>
      </div>
      <div>
        <h5>Courses</h5>
        <a href="index.html#courses">Cloud &amp; DevOps</a>
        <a href="index.html#courses">Data &amp; Analytics</a>
        <a href="index.html#courses">Enterprise Apps</a>
        <a href="index.html#courses">Development</a>
      </div>
      <div>
        <h5>Company</h5>
        <a href="index.html#features">Why Us</a>
        <a href="index.html#support">On-Job Support</a>
        <a href="index.html#testimonials">Reviews</a>
        <a href="index.html#contact">Contact</a>
      </div>
      <div>
        <h5>Get started</h5>
        <a href="index.html#demo">Free Demo</a>
        <a href="index.html#contact">Corporate Training</a>
        <a href="tel:+919441803173">📞 +91-9441803173</a>
        </div>
    </div>
    <div class="copy">© 2026 KS Trainings. All rights reserved.</div>
  </div>
</footer>
</body>
</html>\`;

courses.forEach(c => {
  fs.writeFileSync(c.file, template(c));
  console.log('Created ' + c.file);
});
