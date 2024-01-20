from PyQt5.QtWidgets import *

app = QApplication([])

window = QWidget()
window.resize(500,500)

textedite = QTextEdit()

startBtn = QPushButton("Створити замітку")

spysok = QLabel("Список заміток")


list1 = QListWidget()

main_line = QHBoxLayout()
v1 = QVBoxLayout()
v2 = QVBoxLayout()

v2.addWidget(spysok)
v2.addWidget(list1)
v2.addWidget(startBtn)

main_line.addLayout(v1)
main_line.addLayout(v2)

v1.addWidget(textedite)

window.setLayout(main_line)
window.show()
app.exec()