from csv_reader import CsvData
from console_ui import ConsoleUI

def main():
    data = CsvData("data/transactions_2.csv")
    headers: list[str] = data.get_headers()
    rows: list[list[str]] = data.get_rows()
    display_headers: set = set()
    ui = ConsoleUI()

    entry = float("-inf")
    while entry < 0 or entry > len(headers) - 1:
        entry = ui.selection_menu("Select the entry for the outgoing amount: ", headers, display_headers)
    display_headers.add(entry)

    entry = float("-inf")
    while entry < 0 or entry > len(headers) - 1:
        entry = ui.selection_menu("Select the entry for the charge description: ", headers, display_headers)
    display_headers.add(entry)
    
    entry = float("-inf")
    while entry != -1:
        entry = ui.selection_menu("Select any additional columns to include. Press 0 to continue. ", headers, display_headers)
        if entry != -1:
            display_headers.add(entry)

    

    header_strs = []
    data_strs = []

    for i in display_headers:
        header_strs.append(headers[i])
    
    for row in rows:
        data = []
        for i in display_headers:
            data.append(row[i])
        data_strs.append(data)

    ui.display_table(header_strs, data_strs)

# def get_choice():
#     


if __name__ == "__main__":
    main()