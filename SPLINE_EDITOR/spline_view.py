from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import  QWidget
from PyQt5.QtGui import QMouseEvent, QPainter,  QPalette, QPen
from spline import Spline

class SplineWiev(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.spline=Spline()
    
    def paintEvent(self, event) -> None:
        bg_color=self.palette().color(QPalette.Base)
        curve_color=self.palette().color(QPalette.Foreground)
        painter=QPainter(self)
        painter.fillRect(self.rect(), bg_color)
        painter.setPen(QPen(curve_color, 2, Qt.SolidLine))
        painter.setRenderHints(QPainter.HighQualityAntialiasing)
        painter.drawPolyline(self.spline.get_curve())
        return super().paintEvent(event)
    
    def mousePressEvent(self, event):
        self.spline.add_knot(event.pos())
        self.update()
        return super().mousePressEvent(event)