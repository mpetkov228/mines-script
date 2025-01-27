floating_wager = float(input("Enter starting wager: "))
minimum_wager = floating_wager

total = 0
while True:
    result = input("1 for win | 0 for loss | end ")
    if result == "end":
        break
    
    if result == "1":
        total += floating_wager * 1.47 - floating_wager
        floating_wager = minimum_wager
    elif result == "0":
        total -= floating_wager
        floating_wager *= 3.33
    else:
        print("Invalid input! Try again!")
        continue
    

print("End total:", total)    