def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def divide(num1,num2):
    return num1/num2
def modulo(num1,num2):
    return num1%num2
num1 = int(input("enter a number"))
num2 = int(input("enter a number"))
operation = input('plz enter (*,-,+,/,%)')
result = 0
if operation == '+':
    result = add(num1,num2)
elif operation == "-":
    result = subtract(num1,num2)
elif operation == "*":
    result = multiply(num1,num2)
elif operation == "/":
    reult = divide(num1,num2)
elif operation == "%":
    result = modulo(num1,num2)
else:
    print("write something")

print(num1,operation,num2,"=",result)    


    
