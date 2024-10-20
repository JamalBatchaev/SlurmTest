import os

from isvalid import is_valid
os.chdir('./Tasks_6')
with open('text.txt') as f:
    if is_valid(f.read()):
         print('Скобки расставлены валидно')
    else:
         print('Ошибка, скобки невалидны!')