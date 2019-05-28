import gspread
from oauth2client.service_account import ServiceAccountCredentials


def get_locations_id(name):
    name = name.upper()
    scope = ['https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)

    sheet = client.open('Locations and Hashtags').sheet1
    result = sheet.get_all_records()
    location_filtered = [l for l in result if name in l['runner']]
    format = list(map(lambda obj: {'location_id': f"l:{obj['id']}", 'name': obj['location']}, location_filtered))

    return format
