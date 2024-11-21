
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

headers = ["Name", "Birthdate", "Contribution"]
rows = [["Newton", "1643-01-04", "Classical mechanics"],
        ["Einstein", "1879-03-14", "Relativity"],
        ["Darwin", "1809-02-12", "Evolution"]]

class TableModel(QAbstractTableModel):
    def rowCount(self, parent):
        return len(rows)
    def columnCount(self, parent):
        return len(headers)
    def data(self, index, role):
        if role==Qt.ItemDataRole.DisplayRole or role==Qt.ItemDataRole.EditRole:
            value = rows[index.row()][index.column()]
            return str(value)
        else:
            return QVariant()
    def headerData(self, section, orientation, role):
        if role != Qt.ItemDataRole.DisplayRole or orientation != Qt.Orientation.Horizontal:
            return QVariant()
        return headers[section]
    
    def flags(self, index):
        return Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsEditable
    
    def setData(self, index, value, role):
        if role == Qt.ItemDataRole.EditRole:
            rows[index.row()][index.column()] = value
            return True
        return False

app = QApplication([])
model = TableModel()
view = QTableView()
view.setModel(model)
view.show()
app.exec()
