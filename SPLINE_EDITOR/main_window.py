from PyQt5.QtWidgets import  QMainWindow, QWidget
from spline_view import SplineWiev


class MainWindow(QMainWindow):
    def __init__(self, parent= None):
        super().__init__(parent)
        menubar=self.menuBar()
        file_menu=menubar.addMenu('File')
        close_action=file_menu.addAction('Close')
        close_action.triggered.connect(self.close)
        spline_view=SplineWiev()
        self.setCentralWidget(spline_view)