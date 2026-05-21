print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").lower()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
extra_cheese = input("Do you want extra cheese? Y or N: ").lower()

bill = 0
if size == "s":
    if pepperoni == "y":
        bill += 17
    else:
        bill += 15
elif size == "m":
    if pepperoni == "y":
        bill += 23
    else:
        bill += 20
elif size == "l":
    if pepperoni == "y":
        bill += 28
    else:
        bill += 25


if extra_cheese == "y":
    bill += 1

print(f"Your final bill is: ${bill}.")

