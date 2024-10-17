def is_valid(value: str) -> bool:
    acc = []
    for ch in value:        
        if ch == '(':
            acc.append('(')
        elif ch == '[':
            acc.append('[')
        elif ch == '{':
            acc.append('{')
        elif ch == ')':
            if not acc or acc[-1] != '(':
                return False
            acc.pop()
        elif ch == ']':
            if not acc or acc[-1] != '[':
                return False
            acc.pop()
        elif ch == '}':
            if not acc or acc[-1] != '{':
                return False  
            acc.pop()
        
    return len(acc) == 0
    

