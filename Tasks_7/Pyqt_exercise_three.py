from PyQt5.QtWidgets import *

app = QApplication([])
button = QPushButton('Click')
button_two = QPushButton('Выключено')
button_two.isChecked=0
button_three = QPushButton(f'Click count=0')
label_one = QLabel('')
clicks=0

def on_button_clicked():
    alert = QMessageBox()
    alert.setText('You clicked the button!')
    alert.exec()

def on_button_two_clicked():
    if button_two.isChecked==0:
        button_two.setText('Включено')
        button_two.isChecked=1
        label_one.setText('Checked')
    else:
        button_two.setText('Выключено')
        button_two.isChecked=0
        label_one.setText(' ')

def on_button_three_clicked():
    global clicks
    clicks=clicks+1
    button_three.setText(f'Click count={clicks}')
        
    

button.clicked.connect(on_button_clicked)
button_two.clicked.connect(on_button_two_clicked)
button_three.clicked.connect(on_button_three_clicked)



window = QWidget()
layout = QVBoxLayout()
layout.addWidget(button)
layout.addWidget(button_two)
layout.addWidget(button_three)
layout.addWidget(label_one)
window.setLayout(layout)
window.show()
app.exec()
