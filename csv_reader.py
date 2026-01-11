class CsvData:
    def __init__(self, path: str, delimiter: str=","):
        self.path = path
        data = self.__read_file(delimiter)
        self.__headers: list[str] = data[0]
        self.__rows: list[list[str]] = data[1]
    
    def __read_file(self, delimiter: str) -> tuple[list[str], list[list[str]]]:
        headers = []
        rows = []
        with open(self.path) as f:
            headers = f.readline()[:-1].split(delimiter)
            for line in f.readlines():
                row = line[:-1].split(delimiter)
                if row != ['']:
                    rows.append(row)
        return (headers, rows)

    def get_headers(self) -> list[str]:
        return self.__headers

    def get_rows(self) -> list[list[str]]:
        return self.__rows

    def __repr__(self) -> str:
        header_string = f"Header:\n{self.__str_line(self.__headers)}"
        rows_string = "Rows:\n"
        for row in self.__rows:
            rows_string += self.__str_line(row)
        return header_string + '\n' + rows_string
        
    def __str_line(self, data: list) -> str:
        output = ""
        for item in data:
            output += item + ", "
        return output[:-2] + '\n'