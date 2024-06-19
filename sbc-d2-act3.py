from random import randint

print("Lottery House")

# place your bet number
bet1 = int(input("Enter 1st number (0-9): "))
bet2 = int(input("Enter 2nd number (0-9): "))
bet3 = int(input("Enter 3rd number (0-9): "))


print("Bet numbers are; ", bet1, bet2, bet3)

# random winning numbers
r1 = randint(0,9)
r2 = randint(0,9)
r3 = randint(0,9)


print("winning numbers are; ", r1, r2, r3)
      
# the result
if bet1 == r1 and bet2 == r2 and bet3 == r3:
    print("YOU WIN!!")
elif (bet1 == r1 and bet2 == r3 and bet3 == r2) or \
     (bet1 == r2 and bet2 == r1 and bet3 == r3) or \
     (bet1 == r2 and bet2 == r3 and bet3 == r1) or \
     (bet1 == r3 and bet2 == r1 and bet3 == r2) or \
     (bet1 == r3 and bet2 == r2 and bet3 == r1):
    print("Almost got your LLUCK!")
else:
    print("THANK YOU!!")
