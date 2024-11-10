from PyQt5.QtCore import Qt, pyqtSignal, QEvent,QPointF
from PyQt5.QtWidgets import  QWidget
from PyQt5.QtGui import QMouseEvent, QPainter,  QPalette, QPen, QBrush
from spline import Spline
from knot import Knot
from spline_history import SplineHistory

class SplineView(QWidget):

    current_knot_changed=pyqtSignal(Knot)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.spline=Spline()
        self.cur_knot_index=0
        self.spline_hist=SplineHistory()
        self.spline_index=None
        self.mouse_clicked=False
        self.shift_clicked=False

        
    def paintEvent(self, event) -> None:
        bg_color=self.palette().color(QPalette.Base)
        curve_color=self.palette().color(QPalette.Foreground)
        painter=QPainter(self)
        painter.fillRect(self.rect(), bg_color)
        painter.setPen(QPen(curve_color, 3, Qt.SolidLine))
        painter.setRenderHints(QPainter.HighQualityAntialiasing)
        painter.drawPolyline(self.spline.get_curve())

        painter.setBrush(QBrush(curve_color, Qt.SolidPattern))
        for index, knot in enumerate(self.spline.get_knots()):
            radius=6 if self.cur_knot_index==index else 4
            painter.drawEllipse(knot.pos, radius, radius)
        


        return super().paintEvent(event)
    
    def mousePressEvent(self, event:QMouseEvent):
        index=self.spline.get_knot_by_pos(event.pos())
        #Удаление узла при нажатии правой кнопки мыши
        if event.button()==Qt.RightButton:
            if index:
                self.spline.delete_knot(index)
                self.spline_hist.add_spline_view(self.spline)
        #Добавление/выбор узла при нажатии левой кнопки мыши
        elif event.button()==Qt.LeftButton:
            self.mouse_clicked=True
            #выбор узла
            if index is not None:
                self.cur_knot_index=index
            #добавление нового узла после выбранного 
            else:
                if  self.cur_knot_index<len(self.spline.get_knots())-1:
                    self.spline.insert_knot(self.cur_knot_index+1, event.pos())
                else:
                    self.spline.add_knot(event.pos())
                    self.cur_knot_index=len(self.spline.get_knots())-1
                #Добавление записи в Spline History
                self.spline_hist.add_spline_view(self.spline)
            
        
            self.current_knot_changed.emit(self.spline.get_knots()[self.cur_knot_index])
            
        self.update()
        return super().mousePressEvent(event)
    
    #отработка удерживания левой кнопки мыши для перетаскивания узлов
    def mouseMoveEvent(self, event:QMouseEvent):
        if self.mouse_clicked and self.shift_clicked:
            index=self.spline.get_knot_by_pos(event.pos())
            if index:
                self.spline.knots[index].pos=event.pos()
                self.spline._interpolate()
             
        self.update()
        return super().mouseMoveEvent(event)
    
    #отработка отжатия левой кнопки мыши
    def mouseReleaseEvent(self, event:QMouseEvent):
        if event.button()==Qt.LeftButton:
            self.mouse_clicked=False
        self.update()
        return super().mouseReleaseEvent(event)
    
    def set_current_knot(self,  value: Knot):
        self.spline.set_current_knot(self.cur_knot_index, value)
        self.update()

    #Отработка нажатия Undo
    def undo_spline_click(self):
        self.spline_hist.undo_spline()
        self.spline_index=self.spline_hist.index
        self.spline=self.spline_hist.splines[self.spline_index]
        self.update()

    #Отработка нажатия Redo
    def redo_spline_click(self):
        self.spline_hist.redo_spline()
        self.spline_index=self.spline_hist.index
        self.spline=self.spline_hist.splines[self.spline_index]
        self.update()