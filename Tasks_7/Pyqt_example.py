import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
 
def window():
   # Создаем Qt приложение
   app = QApplication(sys.argv)
   # Создаем пустой виджет
   widget = QWidget()
   # Создаем дочерний (указываем ему родителя в конструкторе) к раннее созданному виджет типа QLabel
   textLabel = QLabel(widget)
   # Лейблы способны отображать текст. Устанавливаем текст
   textLabel.setText("Hello World!")
   # Двигаем лейбл на координаты, рассчитываемые от угла родительского виджета
   textLabel.move(110,85)
   # Задаем родительскому виджету геометрию (размеры и положение)
   widget.setGeometry(500,500,320,200)
   # Ставим подпись на окне
   widget.setWindowTitle("PyQt5 Example")
   # По умолчанию все виджеты невидимые, пока их не покажет родитель или явно не вызвать соответствующий метод
   widget.show()
   # Ожидаем завершения Qt приложения чтобы выйти из скрипта
   sys.exit(app.exec_())
 
if __name__ == '__main__':
   window()