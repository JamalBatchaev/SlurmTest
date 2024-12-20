from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import  QWidget
from PyQt5.QtGui import QMouseEvent, QPainter,  QPalette, QPen, QBrush, QTransform, QColor
from spline import Spline
from knot import Knot
from spline_history import SplineHistory

class SplineView(QWidget):

    current_knot_changed=pyqtSignal(Knot)
    scale_changed=pyqtSignal(float)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.spline=Spline()
        self.cur_knot_index=0
        self.spline_hist=SplineHistory()
        self.spline_index=None
        self.mouse_clicked=False
        self.shift_clicked=False
        self.current_line_type='Kochanek–Bartels'
        self.scale_factor = 1.0  #масштаб
        
    def paintEvent(self, event) -> None:
        bg_color=self.palette().color(QPalette.Base)
        curve_color=self.palette().color(QPalette.Foreground)
        painter=QPainter(self)
        painter.fillRect(self.rect(), bg_color)
        painter.setPen(QPen(curve_color, 3/self.scale_factor, Qt.SolidLine))
        painter.setRenderHints(QPainter.HighQualityAntialiasing)
        #изменение масштаба
        transform = QTransform()
        transform.scale(self.scale_factor, self.scale_factor)
        painter.setTransform(transform)
        #отрисовка изменения типа линии
        if self.current_line_type=='Kochanek–Bartels':
            painter.drawPolyline(self.spline.get_curve())
        elif self.current_line_type=='Polyline':
            painter.drawPolyline(self.spline.get_curve_polyline())

        painter.setBrush(QBrush(curve_color, Qt.SolidPattern))
        for index, knot in enumerate(self.spline.get_knots()):
            radius=6/self.scale_factor if self.cur_knot_index==index else 4/self.scale_factor
            painter.drawEllipse(knot.pos, radius, radius)

        #отрисовка сетки
        painter.setPen(QPen(QColor(curve_color), 0.3/self.scale_factor, Qt.DotLine)) 
        cell_size = 50
        cell_heught=int(self.height()/self.scale_factor)
        cell_width=int(self.width()/self.scale_factor)
        for x in range(0, cell_width, cell_size):
            painter.drawLine(x, 0, x, cell_heught)
        for y in range(0, cell_heught, cell_size):
            painter.drawLine(0, y, cell_width, y)

        return super().paintEvent(event)
    
    def mousePressEvent(self, event:QMouseEvent):
        #учет изменения масштаба
        scaled_pos = event.pos() / self.scale_factor

        index = self.spline.get_knot_by_pos(scaled_pos, self.scale_factor)
        #Удаление узла при нажатии правой кнопки мыши
        if event.button()==Qt.RightButton:
            if index:
                self.spline.delete_knot(index)
                self.spline_hist.add_spline_view(self.spline)
                self.cur_knot_index=index-1
                self.set_current_knot(self.spline.get_knots()[self.cur_knot_index])
                self.current_knot_changed.emit(self.spline.knots[index-1])
        #Добавление/выбор узла при нажатии левой кнопки мыши
        elif event.button()==Qt.LeftButton:
            self.mouse_clicked=True
            #выбор узла
            if index is not None:
                self.cur_knot_index=index
            #добавление нового узла после выбранного 
            else:
                if  self.cur_knot_index<len(self.spline.get_knots())-1:
                    self.spline.insert_knot(self.cur_knot_index+1, scaled_pos)
                    self.cur_knot_index+=1
                else:
                    self.spline.add_knot(scaled_pos)
                    self.cur_knot_index=len(self.spline.get_knots())-1        
            
            
        self.update()
        return super().mousePressEvent(event)
    
    #отработка удерживания левой кнопки мыши для перетаскивания узлов
    def mouseMoveEvent(self, event:QMouseEvent):
        #учет изменения масштаба
        scaled_pos = event.pos() / self.scale_factor

        if self.mouse_clicked and self.shift_clicked:
            index=self.spline.get_knot_by_pos(scaled_pos, self.scale_factor)
            if index:
                self.spline.knots[index].pos=scaled_pos
                self.spline.interpolate()
        self.update()
        return super().mouseMoveEvent(event)
    
    #отработка отжатия левой кнопки мыши
    def mouseReleaseEvent(self, event:QMouseEvent):
        if event.button()==Qt.LeftButton:
            self.mouse_clicked=False
            self.set_current_knot(self.spline.get_knots()[self.cur_knot_index])
            self.update()
        return super().mouseReleaseEvent(event)
    #установка текущего узла
    def set_current_knot(self,  value: Knot):
        self.spline.set_current_knot(self.cur_knot_index, value)
        self.spline_hist.add_spline_view(self.spline)
        self.spline_index=self.spline_hist.index
        self.current_knot_changed.emit(self.spline.get_knots()[self.cur_knot_index])
        self.update()

    #Отработка нажатия Undo
    def undo_spline_click(self):
        self.spline_hist.undo_spline()
        self.spline_index=self.spline_hist.index
        self.spline=self.spline_hist.splines[self.spline_index]
        self.cur_knot_index=self.spline_index
        if self.cur_knot_index>len(self.spline.get_knots())-1:
            self.cur_knot_index=len(self.spline.get_knots())-1
        self.current_knot_changed.emit(self.spline.knots[-1])
        self.update()

    #Отработка нажатия Redo
    def redo_spline_click(self):
        self.spline_hist.redo_spline()
        self.spline_index=self.spline_hist.index
        self.spline=self.spline_hist.splines[self.spline_index]
        self.cur_knot_index=self.spline_index
        if self.cur_knot_index>len(self.spline.get_knots())-1:
            self.cur_knot_index=len(self.spline.get_knots())-1
        self.current_knot_changed.emit(self.spline.knots[-1])
        self.update()
    #обработка изменения типа линии
    def redraw_changed_line(self, value: str):
        self.current_line_type=value
        self.paintEvent
        self.update()

    # Изменение масштаба при прокрутке колесика мыши
    def wheelEvent(self, event):
        if self.scale_factor < 0.2:
            self.scale_factor = 0.2
        elif self.scale_factor > 5.0:
            self.scale_factor = 5.0
        else:
            if event.angleDelta().y() > 0:
                self.scale_factor *= 1.1  
            else:
                self.scale_factor /= 1.1 
        
        self.scale_changed.emit(self.scale_factor)
        self.update()