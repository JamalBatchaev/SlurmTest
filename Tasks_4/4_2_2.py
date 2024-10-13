
def matrix (a:int=1, b:int=25)->str:
    
    res_str=''
    i=a
    while i <=b:
        if i%5==0:
            res_str=res_str+str(i)+'\n'
            
        else:
            res_str=res_str+str(i)+' '
        
        i+=1
        
    return res_str
print('Построение матрицы 5 x n')
print('Введите начало матрицы:')
a=int(input())
print('Введите конец матрицы:')
b=int(input())
print (matrix(a,b))



