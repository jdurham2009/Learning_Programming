#Get details of loan
money_owed = float(input("How much money do you owe, in dollars?\n")) #$50,000 example value
apr = float(input("What is the APR of the loan\n")) #3% example value
payment = float(input("How much will you pay off each month, in dollars\n")) #$1,000 example value
months = int(input("How many months do you want to see the results for?\n")) #24

monthly_rate = apr/100/10

# Calculate interest to pay
interest_paid = money_owed*monthly_rate

# Add interest
money_owed = money_owed + interest_paid

# Make payment
money_owed = money_owed - payment

print("Paid", payment , "of which", interest_paid, "was interest", end=" ")
print("Now I owe", money_owed)