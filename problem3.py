class Cell:
    content: str | None
    def __init__(self, content: str | None) -> None:
        self.content = content

def create_table() -> list[list[Cell]]:
    table = [
        [Cell(None), Cell('X'), Cell('X'), Cell(None)],
        [Cell('X'), Cell('O'), Cell('O'), Cell('X')],
        [Cell('X'), Cell('O'), Cell('O'), Cell('X')],
        [Cell(None), Cell('X'), Cell('X'), Cell(None)]
    ]
    return table

def print_table(table: list[list[Cell]]) -> None:
    for row in table:
        for cell in row:
            if cell.content is None:
                # Print empty space
                print(' ', end='')
            else:
                # Print the cell's content itself
                print(cell.content, end='')
        # Print newline character sequence after each line
        print()

def main() -> None:
    table = create_table()
    print_table(table)

if __name__ == '__main__':
    main()
