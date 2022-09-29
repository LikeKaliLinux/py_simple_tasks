#Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.

#Write a square function that takes 1 argument — the side of the square, and returns 3 values (using a tuple): the perimeter of the square, the area of the square and the diagonal of the square.

print("Function: \"squre\":")

s = int(input("""
Enter inportance of side squre
(inportance must be an integer, else ==> error).
:  """))
d = s * 1.414
P = 4 * s
S = s ** 2

d1 = [ "d", "в", "D", "В" ]
P1 = [ "p", "P", "з", "З" ]
S1 = [ "s", "S", "ы", "Ы" ]
all = ["all", "a", "everything", "все", "всё", "al"]

print("""d ==> find diagonal of the squre;
P ==> find perimetr of the squre;
S ==> find area of the squre;
all ==> find everything.""")

ch = input("Enter d ;  P ;  S  ;  all : ")
if ch in d1 :
    print("Diagonal of the squre =",d)
elif ch in P1:
    print("Perimetr of the squre =",P)
elif ch in S1:
    print("Area of the squre =",S)
elif ch in all:
    print("Diagonal =",d,";","Perimetr =",P,";",'Area =',S,".")
else:
    print("Incorrect inportance. Just pick: d ; P ; S ; or enter \"all\"")
