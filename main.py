from csv_reader import csv_data
from console_ui import console_ui

def main():
    data = csv_data("data/transactions_2.csv")
    headers: list[str] = data.get_headers()
    rows: list[list[str]] = data.get_rows()
    display_headers: list[int] = []
    ui = console_ui()

    display_headers.append(ui.selection_menu("Select the entry for the outgoing amount: ", headers, display_headers))
    display_headers.append(ui.selection_menu("Select the entry for the charge description: ", headers, display_headers))

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

if __name__ == "__main__":
    main()