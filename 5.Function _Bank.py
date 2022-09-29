#Пользователь делает вклад в размере a рублей сроком на years лет под 10% годовых (каждый год размер его вклада увеличивается на 10%. Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты).

#Написать функцию bank, принимающая аргументы a и years, и возвращающую сумму, которая будет на счету пользователя.

#The user makes a contribution in the amount of a rubles for a period of years at 10% per annum (every year the amount of his contribution increases by 10%. This money is added to the amount of the deposit, and there will also be interest on it next year).

#Write a bank function that accepts the arguments a and years, and returns the amount that will be on the user's account.

print('Function \"Bank\":')

sum = int(input('''Enter deposit amount,
deposit amount must be a integer and not must be less 0.
: '''))

print('\n')

period = int(input('''Enter period in years,
period in years must be a integer and not must be less 0.
: '''))

profit1 = sum * 10 // 100
profit2 = ( profit1 * period ) + sum

print('''\nYour deposit amount =''',sum,'''

Your period in years =''',period,'''

Calculation your profit...
.......
...........
Your profit =''',profit1,'''for 1 year.''','''

You will be paid total: ''',profit2,'''
Thanks for your waiting and attention.
Good day for you :) .''')

