from PyQt5.QtWidgets import  QMainWindow, QWidget, QMessageBox
from spline_view import SplineWiev
from control_panel import ControlPanel
from dialogs import Dialog
from PyQt5.QtGui import QPalette, QKeySequence



class MainWindow(QMainWindow):
    
    def __init__(self, parent= None):
        super().__init__(parent)
        menubar=self.menuBar()
        menubar.setFocus()
        file_menu=menubar.addMenu('&File')
        close_action=file_menu.addAction('Close')
        close_action.triggered.connect(self.close)


        #пункт меню About
        about_menu=menubar.addMenu('&About')
        about_menu.aboutToShow.connect(self.on_about_clicked)
        


        spline_view=SplineWiev()
        #пункт меню edit->undo
        edit_menu=menubar.addMenu('&Edit')
        undo_action=edit_menu.addAction('Undo')
        undo_action.setShortcut(QKeySequence("Ctrl+Z"))
        undo_action.triggered.connect(spline_view.undo_spline_click)

        #пункт меню edit->redo
        redo_action=edit_menu.addAction('Redo')
        redo_action.setShortcut(QKeySequence("Shift+Ctrl+Z"))
        redo_action.triggered.connect(spline_view.redo_spline_click)

        self.setCentralWidget(spline_view)
        control_panel=ControlPanel(spline_view.maximumWidth(), spline_view.maximumHeight())
        self.statusBar().addWidget(control_panel)
        control_panel.state_changed.connect(spline_view.set_current_knot)
        spline_view.current_knot_changed.connect(control_panel.set_state)





    #вызов окна About
    def on_about_clicked(self):
        about = QMessageBox()
        about.setStyleSheet(self.styleSheet())
        about.setWindowTitle('About')
        about.setText('Spline Editor v1.0 Author: Dzhamal Batchaev')
        about.exec()


        

