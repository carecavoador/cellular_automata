import pyxel


LARGURA, ALTURA = 701, 900
MEIO = LARGURA // 2

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


linha = MEIO * '0' + '1' + MEIO * '0'
step = 0


pyxel.init(LARGURA, ALTURA, display_scale=1)
def update():
    global step
    global linha
    
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

    step += 1
    linha = create_new_line(linha)

def draw():
    global linha
    # pyxel.cls(0)
    for index, cell in enumerate(linha):
        if cell == '1':
            pyxel.pset(index, step, 2)

pyxel.run(update, draw)
