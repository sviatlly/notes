from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout,QRadioButton,QHBoxLayout,QGroupBox, QButtonGroup,QTextEdit,QListWidget,QLineEdit,QInputDialog
import json

#data = {'Про солнце':'солнце- хорошее','Про луну':'луна тоже нормальная'}
#with open('f.json','w',encoding='utf-8')as file:
#    json.dump(data,file,ensure_ascii=False)

def add_tag():
    try:
        key = names_notes.selectedItems()[0].text()
    except:
        return[0]
    new_tag = tag_input.text()
    data[key] ['теги'].append(new_tag)
    with open('f1.json','w',encoding='utf-8')as file:
        json.dump(data,file,ensure_ascii=False)      
    names_tags.clear()
    names_tags.addItems(data[key]['теги'])
    tag_input.setText('')

def delete_tag():
    try:
        key = names_notes.selectedItems()[0].text()
        del_tag = names_tags.selectedItems()[0].text()
    except:
        return[0]
    data[key] ['теги'].remove(del_tag)
    with open('f1.json','w',encoding='utf-8')as file:
        json.dump(data,file,ensure_ascii=False)
    names_tags.clear()
    tag_input.setText('')
    names_tags.addItems(data[key]['теги'])

def find_tag():
    tag = tag_input.text()
    if buton_find.text() == 'Искать' and tag:
        notes_filted = {}
        for note in data:
            if tag in data[note]['теги']:
                notes_filted[note]=data[note]
        #print (notes_filted)
        buton_find.setText('Сброс тега')
        names_notes.clear()
        names_tags.clear()
        names_notes.addItems(notes_filted)
    elif buton_find.text() == 'Сброс тега':
        tag_input.clear()
        names_notes.clear()
        names_tags.clear()
        names_notes.addItems(data)
        buton_find.setText('Искать')

def show_note():
    key = names_notes.selectedItems()[0].text()
    note_edit.setText(data[key]['текст'])
    names_tags.clear()
    names_tags.addItems(data[key]['теги'])

def save_text():
    new_text = note_edit.toPlainText()
    key = names_notes.selectedItems()[0].text()
    data[key] = {'текст':new_text,'теги':[]}
    with open('f1.json','w',encoding='utf-8')as file:
        json.dump(data,file,ensure_ascii=False)

def shiwa():
    key = names_notes.selectedItems()[0].text()
    del data[key]
    with open('f1.json','w',encoding='utf-8')as file:
        json.dump(data,file,ensure_ascii=False)
    names_notes.clear()
    note_edit.setText('')
    names_notes.addItems(data)
    
def brahma():
    key,result = QInputDialog.getText(winrar,'Добавить заметку','Название заметки')
    if result:
        new_text = note_edit.toPlainText()
        data[key] = {'текст':new_text,'теги':[]}
        with open('f1.json','w',encoding='utf-8')as file:
            json.dump(data,file,ensure_ascii=False)      
        names_notes.clear()
        names_notes.addItems(data)

with open('f1.json','r',encoding='utf-8')as file:
    data = json.load(file)
    print(data)

appppp =QApplication([])
winrar = QWidget()
winrar.show()
winrar.setWindowTitle('Умные заметки')
buton_create = QPushButton('Создать') 
buton_create.clicked.connect(brahma)
buton_save = QPushButton('Сохранить') 
buton_save.clicked.connect(save_text)
buton_delete = QPushButton('Удалить') 
buton_delete.clicked.connect(shiwa)
note_edit = QTextEdit('')
names_notes = QListWidget()
tag_input = QLineEdit()
tag_input.setPlaceholderText('Введите тег...')
names_notes.addItems(data)
names_notes.itemClicked.connect(show_note)

linel = QHBoxLayout()
liner = QVBoxLayout()
linel.addWidget(note_edit)
linel.addLayout(liner)
liner.addWidget(QLabel('Список заметок'))
liner.addWidget(names_notes)
liner.addWidget(buton_create)
liner.addWidget(buton_save)
liner.addWidget(buton_delete)

buton_add = QPushButton('Добавить') 
buton_unpin = QPushButton('Открепить') 
buton_find = QPushButton('Искать') 
names_tags = QListWidget()
buton_add.clicked.connect(add_tag)
buton_unpin.clicked.connect(delete_tag)
buton_find.clicked.connect(find_tag)
liner.addWidget(QLabel('Список тегов'))
liner.addWidget(names_tags)
liner.addWidget(buton_add)
liner.addWidget(buton_unpin)
liner.addWidget(buton_find)
liner.addWidget(tag_input)

winrar.move(60,100)
winrar.setLayout(linel)
winrar.resize(750,500)
winrar.setStyleSheet('''font-size:20px''')  
winrar.show()
appppp.exec() 