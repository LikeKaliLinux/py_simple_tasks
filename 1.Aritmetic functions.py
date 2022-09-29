# url ----> https://pythonworld.ru/osnovy/tasks.html

# ----> RUS Простейшие арифметические операции (1)
#Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция, которая должна быть произведена над ними. Если третий аргумент +, сложить их; если —, то вычесть; * — умножить; / — разделить (первое на второе). В остальных случаях вернуть строку "Неизвестная операция".

# ----> ENG The simplest arithmetic operations (1)
#Write an arithmetic function that takes 3 arguments: the first 2 are numbers, the third is the operation that should be performed on them. If the third argument is +, add them; if —, then subtract; * — multiply; / — divide (the first by the second). In other cases, return the string "Unknown operation".


print("""This is my function of arithmetic on Python""")


op1 = int(input("Enter first integer operand: "))
op2 = int(input("Enter your second integer operand: "))

print(op1," ... ", op2, "= ...")

print("""Operation:
    + ==> addition;
    - ==> subtraction;
    * ==> multiplication;
    / ==> division.""")
    
operation = input("Enter operations: ")

if operation == "+":
    print(op1,"+", op2, "=", op1 + op2)
elif operation == "-":
    print(op1,"-", op2, "=", op1 - op2)
elif operation == "*":
    print(op1,"*", op2, "=", op1 * op2)
elif operation == "/":
    print(op1,"/", op2, "=", op1 / op2)
else:
    print("Unknown operations.")

