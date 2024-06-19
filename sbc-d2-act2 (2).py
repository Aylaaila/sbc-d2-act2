from random import randint

p1 = input("kulob to hayang: ")
c2 = randint(1,7)
c3 = randint(1,7)

hayang = 1
kulob = 7

if p1 == kulob:
    print("P1:kulob")
elif p1 == hayang:
    print("P1:hayang")
if c2 == 7:
    print("C2:kulob")
elif c2 == 1:
    print("C2:hayang")
if c3 == 7:
    print("C3:kulob")
elif c3 == 1:
    print("C3:hayang")
    


if p1 == hayang and c2 == 7 and c3 == 7 or p1 == kulob and c2 == 1 and c3 == 1 :
    print("you win")
elif p1 == 1 and c2 == 7 and c3 == 1 or p1 == 7 and c2 == 1 and c3 == 7:
    print("c2 win")
elif p1 == 1 and c2 == 1 and c3 == 7 or p1 == 7 and c2 == 7 and c3 == 1:
    print("c3 win")
else:
    print("hahay")