import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC
Json = "app-for-g-suite-cfc8658e9d91.json"
Url = ["https://spreadsheets.google.com/feeds"]
Connect = SAC.from_json_keyfile_name(Json, Url)
GoogleSheets = gspread.authorize(Connect)
Sheet = GoogleSheets.open_by_key("1fAJfChndnE9977X8iHVjAZbhepJLSDvXfbfBZvwe7So")
Sheets = Sheet.sheet1
datas = ["03/11", "15:00", "dinner", "taipei"]
// 先塞一筆假資料
Sheets.append_row(dataTitle)
Sheets.append_row(datas)
print("寫入成功")
print(Sheets.get_all_values())