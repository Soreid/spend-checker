class ConsoleUI:
    def __print_selector(self, items: list, skip_indexes: list = None) -> None:
        for i in range(len(items)):
            if i not in skip_indexes:
                print(f"{i + 1}: {items[i]}")

    def __get_selector(self, text: str, items: list) -> int:
        entry = -1
        while entry <= 0 or entry > len(items):
            try:
                entry = int(input(text))
            except:
                print("Please enter a number to select the associated entry.")
                entry = -1
            if entry <= 0 or entry > len(items):
                print("Selection invalid. Please select a different entry.")
        return entry

    def selection_menu(self, text: str, items: list, ignore: list = None) -> int:
        self.__print_selector(items, ignore)
        return self.__get_selector(text, items)

    def __format_cell(self, data, total_chars = 0) -> str:
        output = str(data)
        if total_chars <= len(output):
            return output
        offset = total_chars - len(output)
        return output + " " * offset

    def __get_col_lengths(self, header: list[str], data: list[list]) -> list[int]:
        max_chars = []
        for i in range(len(header)):
            max_length = len(header[i])
            for j in range(len(data)):
                if len(str(data[j][i])) > max_length:
                    max_length = len(str(data[j][i]))
            max_chars.append(max_length)
        return max_chars
            
    def display_table(self, header: list[str], data: list[list]) -> None:
        padding_set = self.__get_col_lengths(header, data)
        data.insert(0, header)
        for i in range(len(data)):
            line = ""
            for j in range(len(data[i])):
                line += self.__format_cell(data[i][j], padding_set[j])
                if j == len(data[i]) - 1:
                    break
                line += ' | '
            print(line)