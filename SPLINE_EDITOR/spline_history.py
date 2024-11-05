from spline import Spline
import copy
import pickle


class SplineHistory():
    splines=[]
    index=-1

    def add_spline_view(self,spline:Spline):
        self.index=self.index+1
        self.splines.append(copy.deepcopy(spline)) 
        if self.splines.__len__()>30:
            self.splines.pop(0)
            self.index=29
    
    def undo_spline(self):
        if self.index>0:
            self.index=self.index-1

    def redo_spline(self):
        if self.splines.__len__()-1>self.index:
            self.index=self.index+1



    
