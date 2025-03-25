from collections import deque

def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    output = []
    steps = []

    for symbol in expression:
        if symbol.isalnum():  # Operand
            output.append(symbol)
        elif symbol == '(':
            stack.append(symbol)
        elif symbol == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Remove '('
        else:
            while stack and stack[-1] != '(' and precedence.get(stack[-1], 0) >= precedence.get(symbol, 0):
                output.append(stack.pop())
            stack.append(symbol)
        
        # Save step
        steps.append({
            "symbol": symbol,
            "stack": list(stack),
            "output": list(output)
        })

    while stack:
        output.append(stack.pop())
        steps.append({
            "symbol": "Pop",
            "stack": list(stack),
            "output": list(output)
        })

    return {"result": "".join(output), "steps": steps}


def infix_to_prefix(expression):
    expression = expression[::-1]  
    expression = expression.replace('(', 'temp').replace(')', '(').replace('temp', ')')
    
    postfix_result = infix_to_postfix(expression)
    prefix_result = postfix_result["result"][::-1]  
    postfix_result["result"] = prefix_result  

    return postfix_result  

def postfix_to_infix(expression):
    stack = []
    steps = []

    for symbol in expression:
        if symbol.isalnum():
            stack.append(symbol)
        else:
            if len(stack) < 2:
                return {"result": "Error: Invalid Postfix Expression", "steps": steps}

            b = stack.pop()
            a = stack.pop()
            result = f"({a}{symbol}{b})"
            stack.append(result)

        steps.append({
            "symbol": symbol,
            "stack": list(stack)
        })

    if len(stack) == 1:
        return {"result": stack[0], "steps": steps}
    else:
        return {"result": "Error: Invalid Postfix Expression", "steps": []}


def prefix_to_infix(expression):
    stack = []
    steps = []
    
    for symbol in reversed(expression):  
        if symbol.isalnum():  # Operand (A, B, C, etc.)
            stack.append(symbol)
        else:  # Operator (+, -, *, /, etc.)
            if len(stack) < 2:
                return {"result": "Error: Invalid Prefix Expression", "steps": []}
            
            a = stack.pop()
            b = stack.pop()
            result = f"({a}{symbol}{b})"
            
            stack.append(result)
        
        # Save step for debugging
        steps.append({
            "symbol": symbol,
            "stack": list(stack)
        })

    if len(stack) == 1:
        return {"result": stack[0], "steps": steps}
    else:
        return {"result": "Error: Invalid Prefix Expression", "steps": []}


import re

def evaluate_postfix(expression):
    stack = []
    steps = []  

    expression = re.sub(r'(\d)([+\-*/])', r'\1 \2', expression) 
    tokens = re.findall(r'\d+|\S', expression) 

    for symbol in tokens:
        if symbol.isdigit():
            stack.append(int(symbol))
        else:
            if len(stack) < 2:
                return {"result": "Error: Invalid Postfix Expression", "steps": steps}
            
            b = stack.pop()
            a = stack.pop()
            
            if symbol == "+":
                result = a + b
            elif symbol == "-":
                result = a - b
            elif symbol == "*":
                result = a * b
            elif symbol == "/":
                if b == 0:
                    return {"result": "Error: Division by Zero", "steps": steps}
                result = a / b 
            else:
                return {"result": "Error: Invalid Operator", "steps": steps}
            
            stack.append(result)

        steps.append({
            "symbol": symbol,
            "stack": list(stack)  
        })

    if len(stack) == 1:
        return {"result": stack[0], "steps": steps}
    else:
        return {"result": "Error: Invalid Postfix Expression", "steps": steps}



def evaluate_prefix(expression):
    stack = []
    steps = []  

    for symbol in reversed(expression):
        if symbol.isdigit():
            stack.append(int(symbol))
        else:
            if len(stack) < 2:
                return {"result": "Error: Invalid Prefix Expression", "steps": steps}

            a = stack.pop()
            b = stack.pop()

            if symbol == "+":
                result = a + b
            elif symbol == "-":
                result = a - b
            elif symbol == "*":
                result = a * b
            elif symbol == "/":
                result = a / b  
            else:
                return {"result": "Error: Invalid Operator", "steps": steps}
            
            stack.append(result)


        steps.append({
            "symbol": symbol,
            "stack": list(stack)  
        })

    if len(stack) == 1:
        return {"result": stack[0], "steps": steps}
    else:
        return {"result": "Error: Invalid Prefix Expression", "steps": steps}


def evaluate_infix(expression):
    try:
        result = eval(expression)
        return {"result": result, "steps": []}
    except Exception:
        return {"result": "Error: Invalid Infix Expression", "steps": []}
