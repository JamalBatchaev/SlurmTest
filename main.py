splines=list() 
current_spline=0
index=-1

def add_spline_view(spline:int):
    splines.append(spline)
    global index
    global    current_spline
    index = index +1
    current_spline=splines[-1]
    if splines.__len__()>30:
        splines.pop(0)
        index=29
    
def undo_spline():
    global index
    global    current_spline
    if index>0:
        index=index-1
        current_spline=splines[index]
    
def redo_spline():
    global index
    global    current_spline
    if  index<splines.__len__()-1:
        index=index+1
        current_spline=splines[index]

add_spline_view(1)
add_spline_view(2)
add_spline_view(3)
add_spline_view(4)
add_spline_view(5)
add_spline_view(6)
add_spline_view(7)
print(splines)
print(current_spline)
print(index)

undo_spline()
undo_spline()
undo_spline()
undo_spline()
print(splines)
print(current_spline)
print(index)

redo_spline()
print(splines)
print(current_spline)
print(index)
