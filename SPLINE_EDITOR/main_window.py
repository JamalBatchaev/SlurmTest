from PyQt5.QtWidgets import  QMainWindow, QWidget, QMessageBox, QFileDialog
from spline_view import SplineWiev
from control_panel import ControlPanel
from dialogs import Dialog
from PyQt5.QtGui import QPalette, QKeySequence
import pickle


class MainWindow(QMainWindow):
    
    def __init__(self, parent= None):
        super().__init__(parent)
        menubar=self.menuBar()
        menubar.setFocus()

        #раздел меню File
        file_menu=menubar.addMenu('&File')

        #пункт меню file->close
        close_action=file_menu.addAction('Close')
        close_action.triggered.connect(self.close)

        #пункт меню file->save
        save_action=file_menu.addAction('Save')
        save_action.setShortcut(QKeySequence("Ctrl+S"))
        save_action.triggered.connect(self.dialog_save) 

        #пункт меню file->open
        open_action=file_menu.addAction('Open')
        open_action.setShortcut(QKeySequence("Ctrl+O"))
        open_action.triggered.connect(self.dialog_open)

        #раздел меню About
        about_menu=menubar.addMenu('&About')
        about_menu.aboutToShow.connect(self.on_about_clicked)
        
        #объявление сплайна
        self.spline_view=SplineWiev()

        #раздел меню Edit
        edit_menu=menubar.addMenu('&Edit')

        #пункт меню edit->undo
        undo_action=edit_menu.addAction('Undo')
        undo_action.setShortcut(QKeySequence("Ctrl+Z"))
        undo_action.triggered.connect(self.spline_view.undo_spline_click)

        #пункт меню edit->redo
        redo_action=edit_menu.addAction('Redo')
        redo_action.setShortcut(QKeySequence("Shift+Ctrl+Z"))
        redo_action.triggered.connect(self.spline_view.redo_spline_click)

        #отображение сплайна
        self.setCentralWidget(self.spline_view)
        control_panel=ControlPanel(self.spline_view.maximumWidth(), self.spline_view.maximumHeight())
        self.statusBar().addWidget(control_panel)
        control_panel.state_changed.connect(self.spline_view.set_current_knot)
        self.spline_view.current_knot_changed.connect(control_panel.set_state)





    #вызов окна About
    def on_about_clicked(self):
        about = QMessageBox()
        about.setStyleSheet(self.styleSheet())
        about.setWindowTitle('About')
        about.setText('Spline Editor v1.0 Author: Dzhamal Batchaev')
        about.exec()

    #сохранение сплайна в файл
    def dialog_save(self):
        save_dialog=QFileDialog()
        save_dialog.setStyleSheet(self.styleSheet())
        fname = save_dialog.getSaveFileName(self, "Save current knots of spline", 'data', "Pickle files (*.pkl)")[0]
        f=open(fname, 'wb')
        with f:  
            pickle.dump(self.spline_view.spline.knots, f)

    #открытие файла со сплайном
    def dialog_open(self):
        open_dialog=QFileDialog()
        open_dialog.setStyleSheet(self.styleSheet())
        fname = open_dialog.getOpenFileName(self, "Open file with knots", 'data', "Pickle files (*.pkl)")[0]
        f = open(fname, 'rb')

        with f:
            self.spline_view.spline.knots = pickle.load(f)
            #повторная прорисовка сплайна по загруженным точкам
            self.spline_view.spline._interpolate()


