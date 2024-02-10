from PyQt6.QtWidgets import *

import json

try:
    with open("notes_data.json", "r", encoding="utf-8") as file:
        notes = json.load(file)
except:
    notes = {}

app = QApplication([])

app.setStyleSheet("""
    QWidget {
        background-color:#000000 ;
        color : #ffffff;

    }

    QPushButton {
        background-color: #3232ff;

    }


""")

window = QWidget()
window.resize(800, 500)
mainline = QHBoxLayout()

baton1 = QPushButton('створити замітку')
baton2 = QPushButton('видалити замітку')
baton3 = QPushButton('зберегти замітку')
baton4 = QPushButton('додати до замітки')
baton5 = QPushButton('відкріпити від замітки')
baton6 = QPushButton('Скинути пошук')
text1 = QLabel('список заміток')
text2 = QLabel('список тегів')
pole1 = QTextEdit()
pole2 = QListWidget()
pole3 = QListWidget()
pole4 = QLineEdit()

linepole = QVBoxLayout()
linemenu = QVBoxLayout()
line1 = QHBoxLayout()
line2 = QHBoxLayout()

mainline.addLayout(linepole)
mainline.addLayout(linemenu)
linepole.addWidget(pole1)
linemenu.addWidget(text1)
linemenu.addWidget(pole2)
line1.addWidget(baton1)
line1.addWidget(baton2)
linemenu.addLayout(line1)
linemenu.addWidget(baton3)
linemenu.addWidget(text2)
linemenu.addWidget(pole3)
linemenu.addWidget(pole4)
line2.addWidget(baton4)
line2.addWidget(baton5)
linemenu.addLayout(line2)
linemenu.addWidget(baton6)


def add_note():
    note_name, ok = QInputDialog.getText(window, "Дотати заміну", "Назва замітки")
    if ok == True:
        notes[note_name] = {
            "текст": "",
            "теги": []
        }
        pole2.clear()
        pole2.addItems(notes)

        with open("notes_data.json", "w", encoding="utf-8") as file:
            json.dump(notes, file, ensure_ascii=False, indent=4)


def save_note():
    if pole2.selectedItems():
        key = pole2.selectedItems()[0].text()
        notes[key]["текст"] = pole1.toPlainText()
        with open("notes_data.json", "w", encoding="utf-8") as file:
            json.dump(notes, file, ensure_ascii=False, indent=4)
    else:
        print("Замітка для збереження не вибрана!")


def show_note():
    # отримуємо текст із замітки з виділеною назвою та відображаємо її в полі редагування
    key = pole2.selectedItems()[0].text()
    print(key)
    pole1.setText(notes[key]["текст"])
    pole3.clear()
    pole3.addItems(notes[key]["теги"])


def del_note():
    if pole2.selectedItems():
        key = pole2.selectedItems()[0].text()
        notes.pop(key)
        pole2.clear()
        pole3.clear()
        pole1.clear()
        pole2.addItems(notes)
        with open("notes_data.json", "w", encoding="utf-8") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False, indent=4)
        print(notes)
    else:
        print("Замітка для вилучення не обрана!")


def add_tag():  # кнопка добавити тег
    if pole2.selectedItems():
        key = pole2.selectedItems()[0].text()
        tag = pole4.text()
        if not tag in notes[key]["теги"]:
            notes[key]["теги"].append(tag)
            pole3.addItem(tag)
            pole4.clear()
        with open("notes_data.json", "w", encoding="utf-8") as file:
            json.dump(notes, file, ensure_ascii=False)
        print(notes)
    else:
        print("Замітка для додавання тега не обрана!")


def del_tag():  # кнопка видалити тег
    if pole3.selectedItems():
        key = pole2.selectedItems()[0].text()
        tag = pole3.selectedItems()[0].text()
        notes[key]["теги"].remove(tag)
        pole3.clear()
        pole3.addItems(notes[key]["теги"])
        with open("notes_data.json", "w", encoding="utf-8") as file:
            json.dump(notes, file, ensure_ascii=False)
    else:
        print("Тег для вилучення не обраний!")


def search_tag():  # кнопка "шукати замітку за тегом"
    button_text = baton6.text()
    tag = pole4.text()

    if button_text == "Шукати замітки за тегом":
        apply_tag_search(tag)
    elif button_text == "Скинути пошук":
        reset_search()
        pole2.clear()
        pole3.clear()
        pole1.clear()
        pole1.addItems(notes)

def apply_tag_search(tag):
    notes_filtered = {}
    for note, value in notes.items():
        if tag in value["теги"]:
            notes_filtered[note] = value

    baton6.setText("Скинути пошук")
    pole2.clear()
    pole3.clear()
    pole2.addItems(notes_filtered)


def reset_search():
    pole4.clear()
    pole2.clear()
    pole4.clear()
    pole2.addItems(notes)
    baton6.setText("Шукати замітки за тегом")

app.setStyleSheet("""
            QWidget {
                background: #9f2fad;
                }
            QPushButton
            {
            border-style: groove;
            border-width: 5px;
            border-color: brown;
            color: orange;
            }
            







                  """)


baton1.clicked.connect(add_note)
baton2.clicked.connect(del_note)
baton3.clicked.connect(save_note)
baton4.clicked.connect(add_tag)
baton5.clicked.connect(del_tag)
baton6.clicked.connect(search_tag)
pole2.itemClicked.connect(show_note)

window.setLayout(mainline)
window.show()

pole2.addItems(notes)

app.exec()