#Написать функцию date, принимающую 3 аргумента — день, месяц и год. Вернуть True, если такая дата есть в нашем календаре, и False иначе.

#Write a date function that takes 3 arguments — day, month and year. Return True if there is such a date in our calendar, and False otherwise.

print("Function \"Date\":")
print(""" All inputs must be integer and more than 0 but not equal to 0,
else function will lead error.
Exemple of input date: 1.2.2021;

""")

#_________________________________________
months = list(range(1,13))
evenMonths = list(range(1,31))
oddMonths = list(range(1,32))

Jan = ["01", "1"]
Jan1 = list(range(1,32))

Feb = [ 2 ]
Feb1 = list(range(1,29))

Mar = ["03", "3"]
Mar1 = list(range(1,32))

Ap = ["04","4"]
Ap1 = list(range(1,31))

May = ["05",'5']
May1 = list(range(1,32))

June = ["06", "6"]
June1 = list(range(1,31))

Jule = ["07", "7"]
July1 = list(range(1,32))

Aug = ["08", "8"]
Aug1 = list(range(1,32))

Sep = [ "09", "9"]
Sep1 = list(range(1,31))

Oct = "10"
Oct1 = list(range(1,32))

Nov = "11"
Nov1 = list(range(1,31))

Dec = "12"
Dec1 = list(range(1,32))

#__________________________________________
while True:
    day = int(input('''Enter day;
    Not more 31;
    : '''))

    if day <= 0 or day > 31:
        print("""Wrong day. 
        """)
    else:
        break

while True:
    month = int(input('''Enter month;
    Not more 12;
    : '''))

    if month > 12 or month <= 0:
        print('''Wrong month.
        ''')
    else:
        break

while True:
    year = int(input('''Enter year
    : '''))

    if year <= 0:
        ptint('''Wrong year.
        ''')
    else:
        break
    
i_y_l = year % 4
if i_y_l == 0:
    Feb1.append(29)

if day <= 0 or month <= 0 or year <= 0:
    print("All inputs must be more than 0.")
elif year == i_y_l and month in Feb and day in Feb1:
    print("Wrong date.\n")
elif year != i_y_l and month in Feb and day in Feb1:
    print("Wrong date.\n")
else:
    print("Correct date.")
    

   
