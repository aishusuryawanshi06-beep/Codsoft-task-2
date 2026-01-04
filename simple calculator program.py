#Simple Calculator program 

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

op = input("Enter operation (+, -, *, /): ")

if op == '+':
    result = a + b
    
elif op == '-':
    result = a - b
    
elif op == '*':
    result = a * b
    
elif op == '/':
    if b != 0:
        result = a / b
    else:
        result = "Error: Division by zero is not allowed"   
        
else:
    result = "Invalid operation"
    
print("Result:",result)