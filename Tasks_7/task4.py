from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

headers = ["Scientist name", "Birthdate", "Contribution"]
rows = [("Newton", "1643-01-04", "Classical mechanics"),
        ("Einstein", "1879-03-14", "Relativity"),
        ("Darwin", "1809-02-12", "Evolution")]

data = {
   "Name": ["Newton", "Einstein", "Darwin"],
   "Birthdate": ["1643-01-04", "1879-03-14", "1809-02-12"],
   "Contribution": ["Classical mechanics", "Relativity", "Evolution"]
}


class TableModel(QAbstractTableModel):
    def flags(self, index):
        return Qt.ItemIsSelectable|Qt.ItemIsEnabled|Qt.ItemIsEditable

    def setData(self, index, value, role):
        if role == Qt.EditRole:
            self.values[index.column()][index.row()] = value
            return True

    def setCustomData(self, data: dict):
        self.headers = list(data.keys())
        self.values = list(data.values())

    def rowCount(self, parent):
        return len(max(self.values))

    def columnCount(self, parent):
        return len(self.headers)

    def data(self, index, role):
        if role != Qt.ItemDataRole.DisplayRole:
            return QVariant()
        return self.values[index.column()][index.row()]

    def headerData(self, section, orientation, role):
        if role != Qt.ItemDataRole.DisplayRole or orientation != Qt.Orientation.Horizontal:
            return QVariant()        
        return self.headers[section]

app = QApplication([])
model = TableModel()
model.setCustomData(data)
view = QTableView()
view.setModel(model)
view.show()
app.exec()