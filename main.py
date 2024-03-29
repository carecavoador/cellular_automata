import time


rules = {
    '111': '1',
    '110': '0',
    '101': '1',
    '100': '1',
    '011': '0',
    '010': '1',
    '001': '1',
    '000': '0'
}


def create_new_line(previous_line: str) -> str:
    _new_line = ""
    for index, cell in enumerate(previous_line):
        # Ignora a primeira e a última colunas
        if index == 0 or index == len(previous_line) - 1:
            _new_line += cell
            continue

        a = previous_line[index-1]
        b = cell
        c = previous_line[index+1]
        _new_line += rules[a + b + c]

    return _new_line


def print_line(line: str) -> None:
    print("".join(["█" if cell == '0' else " " for cell in line]))


if __name__ == "__main__":
    COLS = 101
    line = (COLS // 2 * '0') + '1' + (COLS // 2 * '0')

    # line = [random.choice([0, 1]) for _ in range(COLS)]
    print_line(line)

    for _ in range(5):
        line = create_new_line(line)
        print_line(line)
        time.sleep(0.1)
