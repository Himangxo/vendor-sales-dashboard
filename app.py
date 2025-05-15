import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

st.title("📊 Vendor Sales Dashboard")

# Google Sheets connection
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# Open the sheet
sheet = client.open("VendorSalesData").sheet1
data = sheet.get_all_records()
df = pd.DataFrame(data)

# Display data
st.dataframe(df)

# Form to add new data
with st.form("sales_form"):
    date = st.date_input("Date")
    vendor = st.text_input("Vendor Name")
    total_sales = st.number_input("Total Sales", min_value=0.0, format="%.2f")
    submitted = st.form_submit_button("Add Entry")

    if submitted:
        sheet.append_row([str(date), vendor, total_sales])
        st.success("Data added!")

