def invest(amount, rate, time):
    counter = 0
    year = 1
    print("principle amount: ${}".format(amount))
    print("annual rate of return {}\n".format(rate))
    for n in range(1, time + 1):
        increase = amount * rate
        amount += increase
        print("year {}: ${}".format(year, amount))
        year += 1
    print()
    print()
    return amount


x = invest(59956, .08, 25)

y = invest(85982, .08, 25)

z = invest(133662, .08, 25)

print("Total in 25 years = {}".format(x + y + z))
