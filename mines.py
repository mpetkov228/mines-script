floating_wager = float(input("Enter starting wager: "))
minimum_wager = floating_wager
total = 0
while True:
    result = input("1 for win | 0 for loss | end")
    if result == "end":
        break