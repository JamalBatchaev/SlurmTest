#4_3_8
def my_range(stop: float, start: float = 0.0, step: float =1.0) -> list[float]:
    retlist=[]
    while start <= stop:
        retlist.append(start)
        start += step
    return retlist

#print(my_range(10.0))