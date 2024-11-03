from PyQt5.QtWidgets import  QMainWindow, QWidget, QMessageBox
from spline_view import SplineWiev
from control_panel import ControlPanel
from dialogs import Dialog
from PyQt5.QtGui import QPalette

class MainWindow(QMainWindow):
    def __init__(self, parent= None):
        super().__init__(parent)
        menubar=self.menuBar()
        file_menu=menubar.addMenu('File')
        close_action=file_menu.addAction('Close')
        close_action.triggered.connect(self.close)

        #About
        about_menu=menubar.addMenu('About')
        about_menu.aboutToShow.connect(self.on_about_clicked)
        


        spline_view=SplineWiev()
        self.setCentralWidget(spline_view)
        control_panel=ControlPanel(spline_view.maximumWidth(), spline_view.maximumHeight())
        self.statusBar().addWidget(control_panel)
        control_panel.state_changed.connect(spline_view.set_current_knot)
        spline_view.current_knot_changed.connect(control_panel.set_state)
    
    def on_about_clicked(self):
        alert = QMessageBox()
        alert.setStyleSheet("color: #d1fa78; background-color: #1e1d23")
        alert.setText('Spline Editor v1.0 Author: Dzhamal Batchaev')
        alert.exec()