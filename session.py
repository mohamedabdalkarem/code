operators = ['+', '-', '*', '/']
expression = input("Enter an expression ") 
for operator in operators:
    if operator in expression:
        num1, num2 = expression.split(operator)
        num1, num2 = float(num1), float(num2)
        
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2
        
        print(f"Result: {result}")
        break
