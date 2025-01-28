starting_balance = float(input("Enter starting balance: "))
floating_wager = float(input("Enter starting wager: "))
minimum_wager = floating_wager

total = 0
while True:
    result = input("1 for win | 0 for loss | end ")
    if result == "end":
        break
    
    if result == "1":
        profit = floating_wager * 1.47 - floating_wager
        total += profit
        print("Profit:", profit)
        floating_wager = minimum_wager
    elif result == "0":
        total -= floating_wager
        print("Loss:", floating_wager)
        floating_wager = floating_wager * 3.33 + floating_wager
    else:
        print("Invalid input! Try again!")
        continue
    

print("End total:", total)    