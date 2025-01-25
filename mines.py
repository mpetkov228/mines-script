floating_wager = float(input("Enter starting wager: "))
minimum_wager = floating_wager

total = 0
while True:
    result = input("1 for win | 0 for loss | end")
    if result == "end":
        break
    
    result = int(result)
    if result == 1:
        total += floating_wager * 1.47 - floating_wager
        floating_wager = minimum_wager
    
    