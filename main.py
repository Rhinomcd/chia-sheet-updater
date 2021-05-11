from sheetfu import SpreadsheetApp
from datetime import datetime

SPREADSHEET_ID = '1G7oNS9OHewTztoEFlqR43qYTQNNJipUJcJq6nqp3Bas'
SHEET_NAME = 'Ryan Hax'

def main():
    sa = SpreadsheetApp('secret.json')
    spreadsheet = sa.open_by_id(SPREADSHEET_ID)
    sheet =  spreadsheet.get_sheet_by_name(SHEET_NAME)

    current_plot_cell = sheet.get_range_from_a1(a1_notification='A2')
    current_plot_cell.set_value(get_plot_count())

    last_updated_cell = sheet.get_range_from_a1(a1_notification='B2')
    last_updated_cell.set_value(datetime.now().strftime().isoformat())

def get_plot_count():
    return 5


if __name__ == '__main__':
    main()