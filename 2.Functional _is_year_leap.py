#Високосный год (2)
#Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе.

#Leap year (2)
#Write a function is_year_leap that takes 1 argument — year, and returns True if the year is a leap year, and False otherwise.


print("Function: \"is_year_leap\":")

year = int(input('''Enter year
(number must be an integer, else ==> error).
:  '''))

i_y_l = year % 4
if i_y_l > 0:
    print('Folse')
elif i_y_l == 0:
    print('True')
else:
    print('Incorect year')
    