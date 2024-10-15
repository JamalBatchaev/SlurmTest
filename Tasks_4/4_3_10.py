def my_range(stop: float, start = 0.0, step = 1.0) -> Generator[float]:
    
        i=start
        while(i<=stop):
            yield i
            i+=step
    
print(my_range(10))