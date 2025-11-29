class csv_data:
    def __init__(self, path: str, delimiter: str=","):
        self.path = path
        data = self.read_file(delimiter)
        self.headers: list[str] = data[0]
        self.rows: list[list[str]] = data[1]
    
    def read_file(self, delimiter: str) -> tuple[list[str], list[list[str]]]:
        headers = []
        rows = []
        with open(self.path) as f:
            headers = f.readline()[:-1].split(delimiter)
            for line in f.readlines():
                rows.append(line[:-1].split(delimiter))
        return (headers, rows)

    def __repr__(self):
        header_string = "Header:\n"
        for header in self.headers:
            header_string += header + ", "
        header_string = header_string[:-2]

        rows_string = "Rows:\n"
        for row in self.rows:
            for item in row:
                rows_string += item + ", "
            rows_string = rows_string[:-2]
            rows_string += '\n'

        return header_string + '\n' + rows_string
        