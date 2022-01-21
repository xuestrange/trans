import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QHBoxLayout, QVBoxLayout, QLabel
from PyQt5 import QtCore
from translate import translate


class translator(QWidget):

    def __init__(self):
        super().__init__()
        self.isword = None
        self.initUI()
        self.text = None

    def initUI(self):
        self.resize(400, 500)
        self.setWindowTitle("translator")
        # layout setting
        trans_button = QPushButton("translate !")
        star_button = QPushButton("star !")
        hbox = QHBoxLayout()
        hbox.addWidget(trans_button)
        hbox.addWidget(star_button)
        vbox = QVBoxLayout()
        input_label = QLabel("")
        pronounce_label = QLabel("")
        trans_label = QLabel("")
        input_label.adjustSize()
        pronounce_label.adjustSize()
        trans_label.adjustSize()
        input_label.setWordWrap(True)
        pronounce_label.setWordWrap(True)
        trans_label.setWordWrap(True)
        input_label.setObjectName("input_label")
        pronounce_label.setObjectName("pronounce_label")
        trans_label.setObjectName("trans_label")
        star_button.setObjectName("star_button")
        trans_button.setObjectName("trans_button")
        vbox.addWidget(input_label)
        vbox.addWidget(pronounce_label)
        vbox.addWidget(trans_label)
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        trans_button.clicked.connect(self.trans_button_clicked)
        star_button.clicked.connect(self.star_clicked)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.show()

    def trans_button_clicked(self):
        translated_text = translate()
        self.is_word = translated_text[0]
        input_label = self.findChild(QLabel, "input_label")
        pronounce_label = self.findChild(QLabel, "pronounce_label")
        trans_label = self.findChild(QLabel, "trans_label")
        if self.is_word:
            input_label.setText(f"{translated_text[1]} \n")
            pronounce_label.setText(f"{translated_text[2][0]} \n")
            trans_label.setText(translated_text[2][1])
            self.setStyleSheet("QLabel{font-size: 20pt;}")
        else:
            input_label.setText(translated_text[1])
            pronounce_label.setText("")
            trans_label.setText(translated_text[2])
            self.setStyleSheet("QLabel{font-size: 18pt;}")
        self.text = translated_text
        self.findChild(QPushButton, "star_button").setText("star !")

    def star_clicked(self):
        if self.isword:
            with open("~/Documents/words.txt", "a") as f:
                f.write(f"{self.text[1]} \n")
                self.findChild(QPushButton, "star_button").setText("write succeed!")
        else:
            with open("~/Documents/sentences.txt", "a") as f:
                f.write(f"{self.text[1]} \t {self.text[2]} \n")
                self.findChild(QPushButton, "star_button").setText("write succeed!")


def main():
    app = QApplication(sys.argv)
    window = translator()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
