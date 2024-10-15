def is_substring(string: str, sub_string: str) -> bool:
    if string.find(sub_string)==-1:
        return False
    else:
        return True

print(is_substring('Sassy', 'y'))
    