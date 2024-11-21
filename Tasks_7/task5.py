from os.path import exists
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *

import sys

if not exists("projects.db"):
    print("File projects.db does not exist. Please run initdb.py.")
    sys.exit()

app = QApplication([])
db = QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName("projects.db")
db.open()

def show_table(db, table):    
    model = QSqlTableModel(None, db)
    model.setTable(table)
    model.select()
    view = QTableView()
    view.setModel(model)
    view.setWindowTitle(table)
    view.show()
    return view

view1 = show_table(db, "projects")
view2 = show_table(db, "YA_projects")
app.exec()