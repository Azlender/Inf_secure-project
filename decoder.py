from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from PyQt5.QtWidgets import QPushButton, QLabel
import sys
import numpy as np
from PIL import Image
import os
import patoolib



def Decode(src):
    img = Image.open(src, 'r')
    array = np.array(list(img.getdata()))

    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4
    total_pixels = array.size//n

    hidden_bits = ""
    for p in range(total_pixels):
        for q in range(0, 3):
            hidden_bits += (bin(array[p][q])[2:][-1])

    hidden_bits = [hidden_bits[i:i+8] for i in range(0, len(hidden_bits), 8)]

    message = ""
    for i in range(len(hidden_bits)):
        if message[-5:] == "$t3g0":
            break
        else:
            message += chr(int(hidden_bits[i], 2))
    print(message)
    if "$t3g0" in message:
        return message[0:-5]
    else:
        return 'no message'


def unpack(file):
    os.rename(file, 'out.rar')
    patoolib.extract_archive("out.rar", outdir=os.getcwd())
    os.remove('out.rar')
def ceasar(lang, line_c, key):
    en_caesar = 'abcdefghijklmnopqrstuvwxyz'
    key = -int(key)
    res = ""
    if lang == "en":
        line_c = line_c.lower()
        for i in line_c:
            if i != ' ':
                k = en_caesar.find(i)
                k = en_caesar[k + key]
                res += k
            else:
                res += ' '
    return res

def vizhener(lang, line, key):
    ln = line
    res = ""
    table_en = [
        ["b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
         "x", "y", "z", "a"],
        ["c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
         "y", "z", "a", "b"],
        ["d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y",
         "z", "a", "b", "c"],
        ["e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
         "a", "b", "c", "d"],
        ["f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a",
         "b", "c", "d", "e"],
        ["g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b",
         "c", "d", "e", "f"],
        ["h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c",
         "d", "e", "f", "g"],
        ["i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d",
         "e", "f", "g", "h"],
        ["j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e",
         "f", "g", "h", "i"],
        ["k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f",
         "g", "h", "i", "j"],
        ["l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g",
         "h", "i", "j", "k"],
        ["m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h",
         "i", "j", "k", "l"],
        ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
         "j", "k", "l", "m"],
        ["o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
         "k", "l", "m", "n"],
        ["p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
         "l", "m", "n", "o"],
        ["q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
         "m", "n", "o", "p"],
        ["r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
         "n", "o", "p", "q"],
        ["s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
         "o", "p", "q", "r"],
        ["t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
         "p", "q", "r", "s"],
        ["u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
         "q", "r", "s", "t"],
        ["v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
         "r", "s", "t", "u"],
        ["w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
         "s", "t", "u", "v"],
        ["x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
         "t", "u", "v", "w"],
        ["y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
         "u", "v", "w", "x"],
        ["z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
         "v", "w", "x", "y"],
        ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z"]
    ]

    if lang == "en":
        key_1 = key
        key_len = len(key_1)
        key_num = 0
        for i in ln:
            if i != ' ':
                key_number = 96 - ord(key_1[key_num]) - 1
                k = ord(i)
                k = int(k - 96 - 1)
                rs = table_en[k][key_number]
                res += rs
                if key_num + 1 < key_len:
                    key_num += 1
                else:
                    key_num = 0
            else:
                res += ' '
    return res


SCREEN_SIZE = [700, 250]

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setGeometry(400, 400, *SCREEN_SIZE)
        self.setWindowTitle('decoder')



        self.path_1 = QLabel(self)
        self.path_1.setText("Вы еще не выбрали файл")
        self.path_1.move(200, 60)

        self.get_1 = QPushButton("выберете файл jpg", self)
        self.get_1.resize(130, 40)
        self.get_1.move(50, 50)
        self.get_1.clicked.connect(self.get_path1)


        self.GO = QPushButton("Нажимать после полного выполнения предыдущих шагов", self)
        self.GO.resize(500, 70)
        self.GO.move(50, 150)
        self.GO.clicked.connect(self.gen_rs)

    def get_path1(self):
        self.fname1 = QFileDialog.getOpenFileName(self, 'Выбрать файл', '', "Картинка(*.jpg)")[0]
        if self.fname1 == '':
            self.fname1 = "Вы не выбрали файл"
        self.path_1.setText("Вы выбрали файл:\n" + self.fname1)
        self.path_1.resize(self.path_1.sizeHint())

    def gen_rs(self):
        unpack(self.fname1)
        self.msg_non_dec = Decode('resultat.png').split(' ')
        self.lang = str(self.msg_non_dec[-3])
        self.caesar_code = str(int(self.msg_non_dec[-2]) - 100)
        self.vizhener_code = ceasar(self.lang, self.msg_non_dec[-1], self.caesar_code)
        self.line = ' '.join(self.msg_non_dec[0:-3])
        self.result = vizhener(self.lang, ceasar(self.lang, self.line, int(self.caesar_code)), self.vizhener_code)
        print(self.result)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
