from random import randint

choices0 = "Kulob"
choices1 = "hayang"
ran = randint(0,1)
dan = randint(0,1)

user = input("Kulob or hayang >")
if user.capitalize() == "Kulob":
    p1 = "Kulob"
    print("P1 = ", user)
else:
    p1 = "hayang"
    print("P1 = hayang")

c2 = ran
if c2 == 1:
    com1 = "Kulob"
    print("C2 = Kulob")
else:
    com1 = "hayang"
    print("C2 = hayang")

com2 = dan
if com2 == 1:
    com2 = "Kulob"
    print("C3 = Kulob")
else:
    com2 = "hayang"
    print("C3 = hayang")


if (p1 == "Kulob" and com1 == "hayang" and com2 == "hayang") or (p1 == "hayang" and com1 == "Kulob" and com2 == "Kulob"):
    print("P1 Win!!!!")


elif (p1 == "hayang" and com1 == "Kulob" and com2 == "hayang") or (p1 == "Kulob" and com1 == "hayang" and com2 == "Kulob"):
    print("C2 Win!!!!")


elif (p1 == "hayang" and com1 == "hayang" and com2 == "Kulob") or (p1 == "Kulob" and com1 == "Kulob" and com2 == "hayang"):
    print("C3 Win!!!!")


else:
    print("naahh")
