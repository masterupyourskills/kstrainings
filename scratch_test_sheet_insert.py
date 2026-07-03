"""
scratch_test_sheet_insert.py
-----------------------------
Run this script AFTER you have:
  1. Deployed your Apps Script as a Web App
  2. Set APPS_SCRIPT_URL in update_forms_google_sheets.py
  3. Run update_forms_google_sheets.py again with your real URL

This script sends a real test POST to the Apps Script endpoint
and verifies whether a sample row appears in your Google Sheet.

Usage:
  python scratch_test_sheet_insert.py
"""
import urllib.request
import json

# ===== REPLACE THIS WITH YOUR ACTUAL WEB APP URL =====
APPS_SCRIPT_URL = "APPS_SCRIPT_WEB_APP_URL_PLACEHOLDER"
# ======================================================

TEST_PAYLOAD = {
    "page_name": "Test - Script Verification",
    "name": "KS Test User",
    "email": "test@kstrainings.com",
    "phone": "+91-8675539226",
    "course_service": "SQL Training (Test)",
    "business_name": "",
    "support_type": "Training & Certification",
    "description": "This is an automated test submission. If you see this row in your Google Sheet, the integration is working correctly!"
}

def run_test():
    print("=" * 60)
    print("KS Trainings — Google Sheets Integration Test")
    print("=" * 60)
    print(f"\nTarget URL: {APPS_SCRIPT_URL}")
    
    if APPS_SCRIPT_URL == "APPS_SCRIPT_WEB_APP_URL_PLACEHOLDER":
        print("\n❌ ERROR: You must replace APPS_SCRIPT_URL with your actual deployed Web App URL.")
        print("\nSteps to deploy:")
        print("  1. Open your Google Sheet")
        print("  2. Click Extensions > Apps Script")
        print("  3. Paste the code from google_apps_script.js")
        print("  4. Click Deploy > New Deployment")
        print("  5. Set: Web app | Execute as: Me | Access: Anyone")
        print("  6. Click Deploy & copy the URL")
        print("  7. Replace APPS_SCRIPT_URL in this file and in update_forms_google_sheets.py")
        print("  8. Run update_forms_google_sheets.py again")
        print("  9. Run this script again\n")
        return

    print("\nSending test payload...")
    print(f"Payload: {json.dumps(TEST_PAYLOAD, indent=2)}\n")

    try:
        data = json.dumps(TEST_PAYLOAD).encode('utf-8')
        req = urllib.request.Request(
            APPS_SCRIPT_URL,
            data=data,
            headers={
                'Content-Type': 'text/plain',
                'Content-Length': str(len(data))
            },
            method='POST'
        )
        with urllib.request.urlopen(req, timeout=30) as response:
            body = response.read().decode('utf-8')
            result = json.loads(body)
            
            if result.get('result') == 'success':
                print("✅ SUCCESS! Test row inserted into Google Sheet.")
                print(f"   Timestamp: {result.get('timestamp', 'N/A')}")
                print("\nPlease open your Google Sheet to verify:")
                print("  https://docs.google.com/spreadsheets/d/1V_PA8gf6k17gUyeou0DNznCK1VqQnougShfLEGRiM-E/edit")
                print("\nExpected row columns:")
                print("  | Timestamp | Test - Script Verification | KS Test User | test@kstrainings.com | +91-8675539226 | SQL Training (Test) | | Training & Certification | This is an automated... |")
            else:
                print(f"❌ Server returned error: {result}")
                
    except urllib.error.HTTPError as e:
        print(f"❌ HTTP Error {e.code}: {e.reason}")
        try:
            body = e.read().decode('utf-8')
            print(f"   Response: {body[:500]}")
        except:
            pass
    except urllib.error.URLError as e:
        print(f"❌ URL Error: {e.reason}")
    except json.JSONDecodeError as e:
        print(f"❌ Could not parse response as JSON: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == '__main__':
    run_test()
