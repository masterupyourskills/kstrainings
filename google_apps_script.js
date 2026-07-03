// ============================================================
// KS Trainings — Google Apps Script for Form Submissions
// Spreadsheet ID: 1V_PA8gf6k17gUyeou0DNznCK1VqQnougShfLEGRiM-E
// ============================================================
// SETUP INSTRUCTIONS:
// 1. Open your Google Sheet: https://docs.google.com/spreadsheets/d/1V_PA8gf6k17gUyeou0DNznCK1VqQnougShfLEGRiM-E/edit
// 2. Click Extensions > Apps Script
// 3. Delete any existing code and paste ALL the code below
// 4. Click Save (Ctrl+S), then click Deploy > New Deployment
// 5. Type: Web app | Execute as: Me | Who has access: Anyone
// 6. Click Deploy, copy the Web App URL
// 7. Replace APPS_SCRIPT_URL in all HTML pages with the Web App URL
// ============================================================

var SHEET_HEADERS = [
  'Timestamp',
  'Page Name',
  'Name',
  'Email',
  'Phone',
  'Course / Service / Platform',
  'Business Name',
  'Support Type',
  'Description / Message'
];

function doPost(e) {
  try {
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var sheet = ss.getActiveSheet();

    // Ensure headers exist
    if (sheet.getLastRow() === 0) {
      sheet.appendRow(SHEET_HEADERS);
      var headerRange = sheet.getRange(1, 1, 1, SHEET_HEADERS.length);
      headerRange.setFontWeight('bold');
      headerRange.setBackground('#1a2456');
      headerRange.setFontColor('#ffffff');
      sheet.setFrozenRows(1);
    }

    // Parse submitted data
    var data;
    try {
      data = JSON.parse(e.postData.contents);
    } catch (err) {
      // Fallback: try URL-encoded params
      data = e.parameter || {};
    }

    var timestamp = new Date().toLocaleString('en-IN', { timeZone: 'Asia/Kolkata' });
    var pageName        = data['page_name']    || data['pageName']    || 'Unknown Page';
    var name            = data['name']         || '';
    var email           = data['email']        || '';
    var phone           = data['phone']        || '';
    var courseService   = data['course']       || data['service_type'] || data['platform'] || data['course_service'] || '';
    var businessName    = data['business_name']|| '';
    var supportType     = data['support_type'] || '';
    var description     = data['description']  || data['message']     || '';

    var row = [
      timestamp,
      pageName,
      name,
      email,
      phone,
      courseService,
      businessName,
      supportType,
      description
    ];

    sheet.appendRow(row);

    // Auto-resize columns for readability
    try {
      sheet.autoResizeColumns(1, SHEET_HEADERS.length);
    } catch (ex) {}

    return ContentService
      .createTextOutput(JSON.stringify({ result: 'success', timestamp: timestamp }))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (err) {
    return ContentService
      .createTextOutput(JSON.stringify({ result: 'error', error: err.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

// Test function — run this manually inside the Apps Script editor to verify
function testInsert() {
  var testData = {
    postData: {
      contents: JSON.stringify({
        page_name: 'Test Page',
        name: 'Test User',
        email: 'test@example.com',
        phone: '+91-9999999999',
        course_service: 'SQL Training',
        business_name: '',
        support_type: 'Training & Certification',
        description: 'This is a test submission from Apps Script editor.'
      })
    }
  };
  var result = doPost(testData);
  Logger.log(result.getContent());
}
