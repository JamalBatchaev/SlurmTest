
def is_valid(value: str)->str:
    if value.count('(')==value.count(')') and value.count('{')==value.count('}') and value.count('[')==value.count(']'):
        return 'assert is valid '+value
    else:
        return 'assert is not valid '+value
    

print(is_valid("('()')"))
print(is_valid("('{}')"))
print(is_valid("('[]')"))
print(is_valid("({[]}"))
print(is_valid("({]}"))
