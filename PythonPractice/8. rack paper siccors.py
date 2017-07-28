


p1 = str(input("1,2,3 shoot:"))
p2 = str(input("1,2,3 shoot:"))

if p1 == p2:
    print("draw")

if p1 == "rock":
    if p2 == "paper":
        print("p2 wins")
    if p2 == "scissors":
        print("p1 wins")

if p1 == "paper":
    if p2 == "rock":
        print("p1 wins")
    if p2 == "scissors":
        print("p2 wins")

if p1 == "scissors":
    if p2 == "paper":
        print("p1 wins")
    if p2 == "rock":
        print("p2 wins")


