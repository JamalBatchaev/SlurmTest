def hypot(a:float, b:float)->float:
    return (a*a+b*b)**0.5

print('Введите длину катета 1:')
a=int(input())
print('Введите длину катета 2:')
b=int(input())
print (f'Гипотенуза равна {hypot(a, b)}')
