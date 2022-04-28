from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QComboBox
from PyQt5.QtWidgets import QPushButton, QLineEdit, QLabel
import sys
import numpy as np
from PIL import Image
import os

SCREEN_SIZE = [600, 900]

def gen_res(path_1, path_2):
    abc = 'Rar.exe a rs.rar ' + path_1
    os.system(abc)
    f1 = open(path_2, 'rb')
    f2 = open('rs.rar', 'rb')
    out = open('out.jpg', 'wb')
    out.write(f1.read())
    out.write(f2.read())
    os.remove("resultat.png")

def encode(src, message, dest):
    dest += '.png'
    img = Image.open(src)
    width, height = img.size
    array = np.array(list(img.getdata()))
    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4
    total_pixels = array.size // n
    message += "$t3g0"
    print(message)
    b_message = ''.join([format(ord(i), "08b") for i in message])
    req_pixels = len(b_message)
    if req_pixels > total_pixels:
        pass
    else:
        index = 0
        for p in range(total_pixels):
            for q in range(0, 3):
                if index < req_pixels:
                    array[p][q] = int(bin(array[p][q])[2:9] + b_message[index], 2)
                    index += 1
    array = array.reshape(height, width, n)
    enc_img = Image.fromarray(array.astype('uint8'), img.mode)
    enc_img.save(dest)



def ceasar(lang, line_c, key):
    en_caesar = 'abcdefghijklmnopqrstuvwxyz'
    key = int(key)
    res = ""
    if lang == "en":
        line_c = line_c.lower()
        for i in line_c:
            if i != ' ':
                k = en_caesar.find(i)
                k = en_caesar[(k + key) % 26]
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
                key_number = ord(key_1[key_num]) - 96 - 1
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




class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setGeometry(400, 400, *SCREEN_SIZE)
        self.setWindowTitle('encoder')

        self.get_1 = QPushButton("выберете файл png", self)
        self.get_1.resize(130, 40)
        self.get_1.move(50, 50)
        self.get_1.clicked.connect(self.get_path1)

        self.path_1 = QLabel(self)
        self.path_1.setText("")
        self.path_1.move(200, 50)

        self.get_2 = QPushButton("выберете файл jpg", self)
        self.get_2.resize(130, 40)
        self.get_2.move(50, 150)
        self.get_2.clicked.connect(self.get_path2)

        self.path_2 = QLabel(self)
        self.path_2.setText("")
        self.path_2.move(200, 150)

        self.inp1 = QLabel(self)
        self.inp1.setText("Введите кодируемый текст")
        self.inp1.resize(self.inp1.sizeHint())
        self.inp1.move(50, 220)

        self.input_text = QLineEdit(self)
        self.input_text.move(50, 250)
        self.input_text.resize(400, 100)

        self.inp3 = QLabel(self)
        self.inp3.setText("Выберете сдвиг по шифру цезаря и язык на котором пишете")
        self.inp3.resize(self.inp3.sizeHint())
        self.inp3.move(50, 380)

        self.caesar_coding = QComboBox(self)
        self.caesar_coding.move(250, 400)
        self.lang = QComboBox(self)
        self.lang.addItem(" ")
        self.lang.addItem("en")
        self.lang.move(50, 400)
        self.lang.currentTextChanged.connect(self.gen_caesar)


        self.inp3 = QLabel(self)
        self.inp3.setText("Введите Ключ Виженера")
        self.inp3.resize(self.inp3.sizeHint())
        self.inp3.move(50, 460)

        self.viszhener_key = QLineEdit(self)
        self.viszhener_key.move(50, 480)
        self.viszhener_key.resize(400, 50)

        self.GO = QPushButton("Нажимать после полного выполнения предыдущих шагов", self)
        self.GO.resize(500, 70)
        self.GO.move(50, 600)
        self.GO.clicked.connect(self.generate_result)

    def get_path1(self):
        self.fname1 = QFileDialog.getOpenFileName(self, 'Выбрать файл', '', "Картинка(*.png)")[0]
        if self.fname1 == '':
            self.fname1 = "Вы не выбрали файл"
        self.path_1.setText("Вы выбрали файл:\n" + self.fname1)
        self.path_1.resize(self.path_1.sizeHint())

    def get_path2(self):
        self.fname2 = QFileDialog.getOpenFileName(self, 'Выбрать файл', '', "Картинка(*.jpg)")[0]
        if self.fname2 == '':
            self.fname2 = "Вы не выбрали файл"
        self.path_2.setText("Вы выбрали файл:\n" + self.fname2)
        self.path_2.resize(self.path_2.sizeHint())

    def gen_caesar(self):
        self.caesar_coding.clear()
        if self.lang.currentText() == ' ':
            self.numbers = 0
        elif self.lang.currentText() == "en":
            self.numbers = 26
        for i in range(1, self.numbers + 1):
            self.caesar_coding.addItem(str(i))

    def generate_result(self):
        self.text_caesar = ceasar(self.lang.currentText(), self.input_text.text(), self.caesar_coding.currentText())
        print(self.text_caesar)
        self.text_vizhener = vizhener(self.lang.currentText(), self.text_caesar, self.viszhener_key.text())
        self.viz = ceasar(self.lang.currentText(), self.viszhener_key.text(), self.caesar_coding.currentText())
        encode(self.fname1, self.text_vizhener + ' ' + self.lang.currentText() + ' ' + str(int(self.caesar_coding.currentText()) + 100) + ' ' +
              self.viz, 'resultat')
        gen_res("resultat.png", self.fname2)
        os.remove("rs.rar")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
