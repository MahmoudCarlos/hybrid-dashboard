import os
import json
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

# 1. قراءة المفاتيح السرية
key_data = json.loads(os.environ['GCP_SA_KEY'])
sheet_id = os.environ['SPREADSHEET_ID']

# 2. تسجيل الدخول لصلاحيات جوجل
scopes = [
    'https://www.googleapis.com/auth/spreadsheets.readonly',
    'https://www.googleapis.com/auth/drive.readonly'
]
creds = Credentials.from_service_account_info(key_data, scopes=scopes)
client = gspread.authorize(creds)

# 3. فتح الشيت وتحميل البيانات
sheet = client.open_by_key(sheet_id).sheet1
data = sheet.get_all_values()

# 4. حفظ البيانات باسم data.csv.csv ليقرأه المتصفح فوراً
df = pd.DataFrame(data)
df.to_csv('data.csv.csv', index=False, header=False)
print("تم سحب أحدث بيانات من شيت جوجل بنجاح وتحديث data.csv.csv!")
