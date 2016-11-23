# -*- coding: utf-8 -*-
# The above allows for the '£' sign

# Mortgage/Loan Calculator
# Calculate the repayments on a mortgage or loan
# Calculate the overall cost and total interest paid

# Ask the user the amount they wish to borrow
# Created a loop to only accept an integer
# any other "data type" will fail and the user will be asked to retry.
while True:
    try:
        loanAmount = float(raw_input("Please enter how much you would like to borrow: £ "))
    except ValueError:
        print "You did not enter the correct format, please enter a number"
        continue
    else:
        break

# Ask user to input how many years the mortgage/loan will be borrowed over
while True:
    try:
        years = int(raw_input("Please enter mortgage/loan term (in years): "))
    except ValueError:
        print "You did not enter the correct format, please enter a number"
        continue
    else:
        break

# Translate the years into months for loan calculation
months = years * 12

# Ask the user to input the interest rate of the mortgage/loan
while True:
    try:
        interestRate = float(raw_input("Please enter interest rate: "))
    except ValueError:
        print "You did not enter the correct format, please enter a number"
        continue
    else:
        break

# Mortgage/Loan calculation
# Calculation of the monthly interest rate
# e.g. interestRate = 5%
# step 1: 5 / 100 = 0.05  |  This is to work out percentage in decimal value
# step 2: 0.05 / 12 =  0.00417  |  This is wotk out percentage each month
monthlyInterest = interestRate / 100 / 12

# Calculation of the monthly payments
# e.g. carry on with example above, months = 60 and loanAmount = 10000
# Step 1: Work out 1 + monthlyInterest
# Step 2: Work out negative exponent of the above value by number of months
# 1 + 0.00417 = 1.00417 ** -60 = 0.779
# Step 3: 1 - the above amount and then divide monthlyInterest by this new amount
# 1 - 0.779 = 0.221
# 0.00417 / 0.221 = 0.0189
# Step 4:  Times the above by the loanAmount
# 0.0189 * 10000 = 189
# 189 is the  monthlyPayment (However results below will be to 2 decimal places)
monthlyPayment = (monthlyInterest / (1 - (1 + monthlyInterest)**(-months))) * loanAmount

# Calculation of totalCost is simply the monthlyPayment * the number of months
totalCost = monthlyPayment * months

# To calculate to overall interest charged it will be the overall amount to pay minus the amount borrowed.
totalInterestCharged = totalCost - loanAmount

# Print results to screen to a value of 2 decimal places for all £'s
print "For a mortgage/loan of value - £%.2f" % (loanAmount)
print "At a rate of - %.2f%%" % (interestRate)
print "Over %d years" % (years)
print "Will cost £%.2f per month" % (monthlyPayment)
print "This is a total cost of £%.2f" % (totalCost)
print "Total interest charge of £%.2f" % (totalInterestCharged)
