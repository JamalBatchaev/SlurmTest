from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtSql import *
from sqlalchemy.orm import Session
from initdb import engine, YaProject

projects=[]
with engine.connect() as conn:
    session=Session(bind=engine)
    projects=list(session.query(YaProject).order_by(YaProject.id).all())

schema={0:'id', 1:'col1', 2:'col2', 3:'col3', 4:'col4', 5:'col5'}

class TableModel(QAbstractTableModel):
    def flags(self, index):
        return Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsEditable
    
    def setData(self, index, value, role):
        if role == Qt.ItemDataRole.EditRole:
            setattr(self.values[index.row()], schema[index.column()], value )
            # Обновление соответствующего поля
            #row_to_update = self.values[index.row()]
            #session.add(row_to_update)
           # session.commit()
            return True 
            
    
    def setCustomData(self, data:list):
        self.headers=list(schema.values())
        self.values=data
    
    def rowCount(self, parent):
        return len(self.values)
    
    def columnCount(self, parent):
        return len(self.headers)
    

    def data(self, index, role):
        if role==Qt.ItemDataRole.DisplayRole:
            value = getattr(self.values[index.row()], schema[index.column()] )
            return str(value)
        else:
            return QVariant()
        
    def headerData(self, section, orientation, role):
        if role != Qt.ItemDataRole.DisplayRole or orientation != Qt.Orientation.Horizontal:
            return QVariant()
        return self.headers[section]  
    def commit(self):
        session.commit() 


app = QApplication([])
window = QWidget()  # Создаем основное окно
layout = QVBoxLayout() 

model = TableModel()
model.setCustomData(projects)
view = QTableView()
view.setModel(model)


commit_button = QPushButton('Commit')
commit_button.clicked.connect(model.commit)  # Подключаем кнопку к методу commit

# Добавляем представление и кнопку в layout
layout.addWidget(view)
layout.addWidget(commit_button)

# Устанавливаем layout в основное окно
window.setLayout(layout)
window.setWindowTitle('Table')
window.show()
app.exec()
    

    


