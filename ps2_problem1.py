balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

for month in range(1, 13):
    min_monthly = monthlyPaymentRate * balance
    balance -= min_monthly
    balance *= 1 + (annualInterestRate / 12)
    
print("Remaining balance: {}".format(round(balance, 2)))