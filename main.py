import time
import random


def calculate_state(a: int, b: int, c: int) -> int:
    if a == 1 and b == 1 and c == 1: return 1
    if a == 1 and b == 1 and c == 0: return 0
    if a == 1 and b == 0 and c == 1: return 1
    if a == 1 and b == 0 and c == 0: return 1
    if a == 0 and b == 1 and c == 1: return 0
    if a == 0 and b == 1 and c == 0: return 0
    if a == 0 and b == 0 and c == 1: return 1
    if a == 0 and b == 0 and c == 0: return 0


def print_line(l: list) -> None:
    print("".join(["_" if cell == 0 else "█" for cell in l]))


def create_new_line(previous_line: list[int]) -> list:
    _new_line = []
    for index, byte in enumerate(previous_line):
        # Ignora a primeira e a última colunas
        if index == 0 or index == len(previous_line) - 1:
            _new_line.append(byte)
            continue

        a = previous_line[index-1]
        b = byte
        c = previous_line[index+1]
        _new_line.append(calculate_state(a, b, c))

    return _new_line


if __name__ == "__main__":
    COLS = 101
    line = [0 for _ in range(COLS)]

    # Coloca uma célula no centro da linha
    line[int(len(line) / 2)] = 1

    # line = [random.choice([0, 1]) for _ in range(COLS)]
    print_line(line)

    for _ in range(100):
        line = create_new_line(line)
        print_line(line)
        time.sleep(0.2)