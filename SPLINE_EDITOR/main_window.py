from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import  QMainWindow,  QMessageBox, QFileDialog
from spline_view import SplineView
from control_panel import ControlPanel
from PyQt5.QtGui import  QKeySequence
import pickle


class MainWindow(QMainWindow):
    
    def __init__(self, parent= None):
        super().__init__(parent)
        self.menubar=self.menuBar()
        self.menubar.setFocus()
        
        #объявление сплайна
        self.spline_view=SplineView()
        self.style_sheet_file=open('light.qss', 'r', encoding='utf-8')
        #раздел меню File
        file_menu=self.menubar.addMenu('&File')

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

        #раздел меню Edit
        edit_menu=self.menubar.addMenu('&Edit')

        #пункт меню edit->undo
        undo_action=edit_menu.addAction('Undo')
        undo_action.setShortcut(QKeySequence("Ctrl+Z"))
        undo_action.triggered.connect(self.spline_view.undo_spline_click)

        #пункт меню edit->redo
        redo_action=edit_menu.addAction('Redo')
        redo_action.setShortcut(QKeySequence("Shift+Ctrl+Z"))
        redo_action.triggered.connect(self.spline_view.redo_spline_click)

        #раздел меню About
        about_menu=self.menubar.addMenu('&About')
        about_menu.aboutToShow.connect(self.on_about_clicked)

        #отображение сплайна
        self.setCentralWidget(self.spline_view)
        control_panel=ControlPanel(self.spline_view.maximumWidth(), self.spline_view.maximumHeight())
        control_panel.setFocusPolicy(Qt.NoFocus)
        self.statusBar().addWidget(control_panel)
        control_panel.state_changed.connect(self.spline_view.set_current_knot)
        control_panel.state_changed.connect(self.set_focus)
        #передача сигнала об изменении типа линии
        control_panel.line_changed.connect(self.spline_view.redraw_changed_line)
        self.spline_view.current_knot_changed.connect(control_panel.set_state)
        

    
    def set_focus(self):
        self.menubar.setFocus()

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
            self.spline_view.spline.interpolate()
    
    #отработка нажатия Shift для перетаскивания узлов сплайна
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Shift:
            self.spline_view.shift_clicked=True
        return super().keyPressEvent(event)
    
    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_Shift:
            self.spline_view.shift_clicked=False
        return super().keyReleaseEvent(event)
    
