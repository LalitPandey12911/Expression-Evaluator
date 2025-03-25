# utils/evaluation.py

def evaluate_postfix(expression):
    stack = []
    
    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        else:
            if len(stack) < 2:
                return "Invalid Expression"
            op1 = stack.pop()
            op2 = stack.pop()
            if char == '+':
                stack.append(op2 + op1)
            elif char == '-':
                stack.append(op2 - op1)
            elif char == '*':
                stack.append(op2 * op1)
            elif char == '/':
                stack.append(op2 / op1)

    return stack[0] if len(stack) == 1 else "Invalid Expression"

def evaluate_prefix(expression):
    stack = []
    
    for char in reversed(expression):
        if char.isdigit():
            stack.append(int(char))
        else:
            if len(stack) < 2:
                return "Invalid Expression"
            op1 = stack.pop()
            op2 = stack.pop()
            if char == '+':
                stack.append(op1 + op2)
            elif char == '-':
                stack.append(op1 - op2)
            elif char == '*':
                stack.append(op1 * op2)
            elif char == '/':
                stack.append(op1 / op2)

    return stack[0] if len(stack) == 1 else "Invalid Expression"

def evaluate_infix(expression):
    try:
        return eval(expression)
    except Exception:
        return "Invalid Expression"
