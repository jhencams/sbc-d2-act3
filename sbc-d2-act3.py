from random import randint

print("lottery")
N1 = int(input("N1 (0-9): "))
N2 = int(input("N2 (0-9): "))
N3 = int(input("N3 (0-9): "))

print("Bet numbers are; ", N1, N2, N3)

r1 = randint(0,9)
r2 = randint(0,9)
r3 = randint(0,9)

print("winning numbers are; ", r1, r2, r3)    

if N1 == r1 and N2 == r2 and N3 == r3:
    print("YOU WIN!!")
elif (N1 == r1 and N2 == r3 and N3 == r2) or \
     (N1 == r2 and N2 == r1 and N3 == r3) or \
     (N1 == r2 and N2 == r3 and N3 == r1) or \
     (N1 == r3 and N2 == r1 and N3 == r2) or \
     (N1 == r3 and N2 == r2 and N3 == r1):
    print("Almost got your LUCK!")
else:
    print("BETTER LUCK NEXT TIME!!")
