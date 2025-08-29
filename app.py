import streamlit as st
import openai
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Set your OpenAI API key
openai.api_key = st.secrets["openai_api_key"]

# Authorize Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_dict(
    st.secrets["gcp_service_account"], scope
)
gc = gspread.authorize(creds)

# 🔍 Debug: List all accessible Google Sheets
sheets = gc.openall()
for s in sheets:
    print("🔍 Accessible Sheet Title:", s.title)

# ✅ Open your Google Sheet by key
try:
    sheet = gc.open_by_key(st.secrets["google_sheet_key"])
    worksheet = sheet.sheet1  # or use .worksheet("Sheet1") if needed
except Exception as e:
    st.error(f"❌ Could not open Google Sheet: {e}")
    st.stop()

# 🎯 Streamlit app layout starts
st.title("📸 Viral Instagram Post Generator")

email = st.text_input("Enter your email to continue:")
if not email:
    st.stop()

# ⏳ Check usage from the sheet
records = worksheet.get_all_records()
user_found = False
for i, row in enumerate(records):
    if row["email"].lower() == email.lower():
        usage_count = row["usagecount"]
        user_found = True
        break

if not user_found:
    worksheet.append_row([email, 1, ""])
    usage_count = 1
else:
    if usage_count >= 5:
        st.warning("⚠️ You have used all 5 free chances. Please upgrade to continue.")
        st.stop()
    else:
        records[i]["usagecount"] += 1
        worksheet.update_cell(i + 2, 2, usage_count + 1)  # Row index starts at 2

# ✅ Prompt user for Instagram topic
topic = st.text_input("Enter your Instagram post topic:")
if not topic:
    st.stop()

# ✨ Call OpenAI API for content
prompt = f"Create a viral, attractive Instagram post with the topic '{topic}' in minimum 5 lines. Give: 1) Content Idea, 2) Caption, 3) Hashtags, 4) Tagline, 5) CTA. Make it trendy and unique."
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.9,
)

st.subheader("📢 Your Viral Instagram Post:")
st.write(response["choices"][0]["message"]["content"])
