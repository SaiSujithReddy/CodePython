def show_balances(daily_balances):
    # do not include -1 because that slice will only have 1 balance, yesterday
    len_array = len(daily_balances)
    for day in range(len_array,1,-1):
        balance_slice = daily_balances[day-2: day]

        # use positive number for printing
        print("slice starting %d days ago: %s" % (abs(day), balance_slice))


daily_balances = [107.92, 108.67, 109.86, 110.15]
show_balances(daily_balances)