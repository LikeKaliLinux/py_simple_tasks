#Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True, если оно простое, и False - иначе.

#Write an is_prime function that takes 1 argument — a number from 0 to 1000, and returns True if it is simple, and False otherwise.



is_prime = int(input("Enter integer from 0 to 1000: "))

if is_prime < 0 or is_prime > 1000:
    print("Error. Need enter integer from 0 to 1000.")
    
a = is_prime % 2
b = is_prime % 3
    
if a == 0 or b == 0:
    print(is_prime,"is not prime number.")
elif a > 0 or b > 0:
    print(is_prime,"is prime number.")
else:
    print("Error. Need integer number from 0 to 1000.")

