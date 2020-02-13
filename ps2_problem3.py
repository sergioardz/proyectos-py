balance = 320000
annualInterestRate = 0.2

monthly_int_rate = annualInterestRate / 12

def lower_side(b):
    return b/12

def upper_side(b):
    return (b * (1 + monthly_int_rate) ** 12) / 12

aux = balance
min_monthly = lower_side(balance)
while aux >= 0.01:
    aux = balance
    for month in range(1, 13):
        aux -= min_monthly
        aux *= 1 + (annualInterestRate / 12)
    if aux >= 0:
        min_monthly = min_monthly + lower_side(abs(aux))
    else:
        min_monthly = min_monthly - upper_side(abs(aux))
        aux = abs(aux)

print("Lowest Payment: {}".format(round(min_monthly, 2)))