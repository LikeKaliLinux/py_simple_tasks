#Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).

#Write a season function that takes 1 argument — the number of the month (from 1 to 12), and returns the time of the year to which this month belongs (winter, spring, summer or autumn).

#Option 1:
print("Function \"Seasons\".\n")

month = int(input(""" Enter integer number of month from 1 to 12.
Your number must be integer and from 1 to 12, else the program will output an error.
: """))

if month > 0 and month <= 2 or month ==12:
    print("Now Winter.\n")
elif month > 2 and month <= 5:
    print("Now Spring.\n")
elif month > 5 and month <= 8:
    print("Now Summer.\n")
elif month > 8 and month <= 11:
    print("Now Fall.\n")
else:
    print("Entered incorrect importance. You need enter integer from 1 to 12.\n")

#Option 1.1. if m == or m ==.

month1 = int(input("""Enter integer number of month from 1 to 12.
Your number must be integer and from 1 to 12, else the program will output an error.
: """))

if month1 == 12 or month1 == 1 or month1 == 2:
    print('Now Winter.\n')
elif month1 == 3 or month1 == 4 or month1 == 5:
    print('Now Spring.\n')
elif month1 == 6 or month1 == 7 or month1 == 8:
    print('Now Summer.\n')
elif month1 == 9 or month1 == 10 or month1 == 11:
    print('Now Fall.\n')
else:
    print("Entered incorrect importance. You need enter integer from 1 to 12.\n")

#Option 2. Lists:

month2 = int(input("""Enter integer number of month from 1 to 12.
Your number must be integer and from 1 to 12, else the program will output an error.
: """))

Winter = [ 12, 1, 2 ]
Spring = [ 3, 4, 5 ]
Summer = [ 6, 7, 8 ]
Fall = [ 9, 10, 11 ]

if month2 in Winter:
    print("Now Winter.")
elif month2 in Spring:
    print('Now Spring.')
elif month2 in Summer:
    print('Now Summer.')
elif month2 in Fall:
    print('Now Fall.')
else:
    print("Entered incorrect importance. You need enter integer from 1 to 12.")
