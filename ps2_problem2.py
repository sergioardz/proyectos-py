balance = 3329
annualInterestRate = 0.2

aux = balance
min_monthly = 0
while aux >= 0:
    aux = balance
    min_monthly += 10
    for month in range(1, 13):
        aux -= min_monthly
        aux *= 1 + (annualInterestRate / 12)

print("Lowest Payment: {}".format(min_monthly))