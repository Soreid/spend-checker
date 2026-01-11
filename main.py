from csv_reader import CsvData
from console_ui import ConsoleUI

def main():
    data = CsvData("data/transactions.csv")
    headers: list[str] = data.get_headers()
    rows: list[list[str]] = data.get_rows()
    display_cols: set = set()
    category_totals: dict = {}
    ui = ConsoleUI()

    # Get required column entries

    category_init(headers, rows)
    category_col = headers.index("Category")
    display_cols.add(category_col)

    amount_col = request_selection(ui, "Select the entry for the charge amount: ", headers, display_cols)
    display_cols.add(amount_col)
    
    desc_col = request_selection(ui, "Select the entry for the charge description: ", headers, display_cols)
    display_cols.add(desc_col)
    
    entry = float("-inf")
    while entry != -1:
        entry = request_selection(ui, "Select any additional columns to include. Press 0 to continue. ", headers, display_cols)
        if entry != -1:
            display_cols.add(entry)

    # Table Execution

    while True:
        show_menu(ui, headers, rows, display_cols, "Enter: Search Description | C: Spending Category Totals | X: Exit Program")
        entry = input().lower()
        match entry:

            # Search Transaction Descriptions
            case "":
                matches = ui.search(get_col_vals(rows, desc_col))
                new_rows = get_rows_by_col(rows, matches)
                if len(new_rows[0]) == 0:
                    print("No results found.")
                else:
                    show_menu(ui, headers, new_rows, display_cols, "C: Set Category | Enter: Clear Search")
                    search_entry = input().lower()
                    if search_entry == "":
                        pass

                    #Categorize Search Results
                    elif search_entry == "c":
                        print('\nPrevious Categories:\n')
                        for category in category_totals.keys():
                            print(category)
                        category = input("\nEnter a Category for these transactions: ")
                        for row in new_rows:
                            update_category(row, category_totals, category, category_col, amount_col)

            # Cagetory Breakdown Table
            case "c":
                header = ["Category", "Total"]
                data = []
                for key in sorted(category_totals):
                    data.append([key, category_totals[key]])
                show_menu(ui, header, data, [0,1], "Enter: Return")
                input()

            # Exit Program
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

def show_menu(ui: ConsoleUI, headers: list[str], data: list[list[str]], display_cols: list[int], input_list: str) -> None:
    ui.display_table(get_display_headers(headers, display_cols), get_display_data(data, display_cols))
    print("\n" + input_list)

def get_display_headers(headers: list[str], display_cols: list[int]) -> list[str]:
    display_headers = []
    for i in display_cols:
        display_headers.append(headers[i])
    return display_headers

def get_display_data(data: list[list[str]], display_cols: list[int]) -> list[list[str]]:
    display_data = []
    for row in data:
        display_row = []
        for i in display_cols:
            display_row.append(row[i])
        display_data.append(display_row)
    return display_data

def get_col_vals(data: list[list[str]], col: int) -> list[str]:
    """Returns a list of values in a single column across the data set."""
    values = []
    for i in range(len(data)):
        if col < len(data[i]):
            values.append(data[i][col])
    return values

def get_unique_col_vals(data: list[list[str]], col: int) -> list[str]:
    values = []
    for i in range(len(data)):
        if col < len(data[i]):
            if data[i][col] not in values:
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

def update_category(row: list[str], category: dict, new_category: str, category_col: int, amount_col: int) -> None:
    """Updates the category listing in the data row and the category dictionary to adjust for the new value...."""
    if row[category_col] != "":
        category[row[category_col]] -= float(row[amount_col])
        if category[row[category_col]] == 0:
            category.pop(row[category_col])
        else:
            category[row[category_col]] = round(category[row[category_col]], 2)

    if new_category in category.keys():
        category[new_category] += float(row[amount_col])
    else:
        category[new_category] = float(row[amount_col])
    category[new_category] = round(category[new_category], 2)
    
    row[category_col] = new_category

if __name__ == "__main__":
    main()