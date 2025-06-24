import gspread
from oauth2client.service_account import ServiceAccountCredentials

def log_to_google_sheets(trades):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
    client = gspread.authorize(creds)

    sheet = client.open("Algo_Trade_Log").worksheet("Trade_Log")
    for trade in trades:
        row = [str(item) if not isinstance(item, (int, float)) else item for item in trade]
        sheet.append_row(row)
