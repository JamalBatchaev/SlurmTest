from PyQt5.QtWidgets import  QWidget, QHBoxLayout, QSpinBox, QDoubleSpinBox, QComboBox
from PyQt5.QtCore import QPointF, pyqtSignal
from knot import Knot


class ControlPanel(QWidget):
    state_changed=pyqtSignal(Knot)
    def __init__(self, width:int, height:int, parent=None):
        super().__init__(parent)

        self.state=Knot(QPointF(0, 0))
        self.line_types = ['Kochanek–Bartels', 'Polyline']
        self.current_line='Kochanek–Bartels'

        layout=QHBoxLayout()
        self.x_spinbox=QSpinBox()
        self.x_spinbox.setMaximum(width)
        self.x_spinbox.setPrefix('X = ')
        self.x_spinbox.valueChanged.connect(self.set_x)
        self.x_spinbox.setSingleStep(10)


        self.y_spinbox=QSpinBox()
        self.y_spinbox.setMaximum(height)
        self.y_spinbox.setPrefix('Y = ')
        self.y_spinbox.valueChanged.connect(self.set_y)
        self.y_spinbox.setSingleStep(10)

        layout.addWidget(self.x_spinbox)
        layout.addWidget(self.y_spinbox)

        def create_spinbox(prefix:str, min:float, max:float, slot)->QDoubleSpinBox:
            spin=QDoubleSpinBox()
            spin.setPrefix(prefix)
            spin.setMinimum(min)
            spin.setMaximum(max)
            spin.setSingleStep(0.1)
            spin.valueChanged.connect(slot)
            layout.addWidget(spin)
            return spin
        
        self.t_spinbox=create_spinbox('T = ', -1000, 1000, self.set_tension)
        self.b_spinbox=create_spinbox('B = ', -1000, 1000, self.set_bias)
        self.c_spinbox=create_spinbox('C = ', -1000, 1000, self.set_continuity)
        
        #Добавление выбора типа линии
        self.combobox = QComboBox()
        for line_type in self.line_types:
            self.combobox.addItem(line_type)
        self.combobox.activated.connect(self.on_activated)
        layout.addWidget(self.combobox)
 
        self.setLayout(layout)


    def set_x (self, value:float):
        if value==self.state.pos.x():
            return
        self.state.pos.setX(value)
        self.state_changed.emit(self.state)

    def set_y (self, value:float):
        if value==self.state.pos.y():
            return
        self.state.pos.setY(value)
        self.state_changed.emit(self.state)
    
    def set_tension (self, value:float):
        if value==self.state.tension:
            return
        self.state.tension=value
        self.state_changed.emit(self.state)
    
    def set_bias (self, value:float):
        if value==self.state.bias:
            return
        self.state.bias=value
        self.state_changed.emit(self.state)

    def set_continuity (self, value:float):
        if value==self.state.continuity:
            return
        self.state.continuity=value
        self.state_changed.emit(self.state)
    
    def set_state (self, value:Knot):
        self.state=value
        self.x_spinbox.setValue(round(value.pos.x()))
        self.y_spinbox.setValue(round(value.pos.y()))
        self.t_spinbox.setValue(value.tension)
        self.b_spinbox.setValue(value.bias)
        self.c_spinbox.setValue(value.continuity)

    def on_activated (self, idx):
        self.current_line=self.line_types[idx]
        print ( self.current_line)
    