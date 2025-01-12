def check_symmetric(string: str):
    # To save opened symbols
    stack = []

    formated_list = list(string.strip().replace(" ", ""))

    # Iteration of symbols, write to the stack opened symbols, and delete if faced with it's closing
    for symbol in formated_list:
        if symbol == '(' or symbol == '{' or symbol == '[':
            stack.append(symbol)
        elif len(stack) == 0 and (symbol == ')' or symbol == '}' or symbol == ']'): #if stack is empty but have closing symbol, it's not symmetrical
            return f"{string} isn't symmetrical"
        elif symbol == ')' and stack[-1] == '(':
            stack.pop()
        elif symbol == '}' and stack[-1] == '{':
            stack.pop()
        elif symbol == ']' and stack[-1] == '[':
            stack.pop()
        else:
            continue

    if len(stack) == 0:
        return f"{string} is symmetrical"
    else:
        return f"{string} isn't symmetrical"


print(check_symmetric('( ) { [ ] ( ) ( ) { } } '))