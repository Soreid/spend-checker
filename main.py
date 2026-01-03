from csv_reader import CsvData
from console_ui import ConsoleUI

def main():
    data = CsvData("data/transactions.csv")
    headers: list[str] = data.get_headers()
    rows: list[list[str]] = data.get_rows()
    display_headers: set = set()
    ui = ConsoleUI()

    # Get required column entries

    amount_col = request_selection(ui, "Select the entry for the charge amount: ", headers, display_headers)
    desc_col = request_selection(ui, "Select the entry for the charge description: ", headers, display_headers)

    display_headers.add(amount_col)
    display_headers.add(desc_col)
    
    entry = float("-inf")
    while entry != -1:
        entry = request_selection(ui, "Select any additional columns to include. Press 0 to continue. ", headers, display_headers)
        if entry != -1:
            display_headers.add(entry)

    # Collect data for included columns

    header_strs = []
    data_strs = []

    for i in display_headers:
        header_strs.append(headers[i])
    
    for row in rows:
        data = []
        for i in display_headers:
            data.append(row[i])
        data_strs.append(data)

    category_init(header_strs, data_strs)

    category_col = header_strs.index("Category")

    # Table Execution

    while True:
        show_menu(ui, header_strs, data_strs, "Enter: Search Description | X: Exit Program")
        entry = input().lower()
        match entry:
            case "":
                matches = ui.search(get_col_vals(rows, desc_col))
                new_rows = get_rows_by_col(data_strs, matches) # What if nothing matches?
                if len(new_rows[0]) == 0:
                    print("No results found.")
                else:
                    show_menu(ui, header_strs, new_rows, "C: Set Category | Enter: Clear Search")
                    search_entry = input()
                    if search_entry == "":
                        pass
                    elif search_entry == "c":
                        category = input("Enter Category for these transactions: ")
                        for row in new_rows:
                            row[category_col] = category

            case "x":
                print("Exiting program...")
                break

# Helper Functions

def request_selection(ui: ConsoleUI, text: str, selections: list[str], ignore: list[int]) -> int:
    entry = ui.selection_menu(text, selections, ignore)
    if entry in ignore:
        print("Selection invalid. Please choose a different option.")
        return request_selection(ui, text, selections, ignore)
    return entry

def show_menu(ui: ConsoleUI, headers: list[str], data: list[list[str]], input_list: str) -> None:
    ui.display_table(headers, data)
    print("\n" + input_list)

def get_col_vals(data: list[list[str]], col: int) -> list[str]:
    values = []
    for i in range(len(data)):
        if col < len(data[i]):
            values.append(data[i][col])
    return values

def get_rows_by_col(data: list[list[str]], cols: list[str]) -> list[list[str]]:
    rows = []
    col_index = 0
    for row in data:
        if col_index < len(cols):
            if cols[col_index] in row:
                rows.append(row)
                col_index += 1
        else:
            break
    if len(rows) == 0:
        rows.append([])
    return rows

def category_init(headers: list[str], data: list[list[str]]) -> None:
    if "Category" not in headers:
        headers.append("Category")
        for row in data:
            row.append("")

if __name__ == "__main__":
    main()