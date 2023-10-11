loan_principal = 'Loan principal: 1000'
final_output = 'The loan has been repaid!'
first_month = 'Month 1: repaid 250'
second_month = 'Month 2: repaid 250'
third_month = 'Month 3: repaid 500'

# write your code here
loan_principal = int(input("Enter your loan principal"))
choice = input(
    'What do you want to calculate? \n type "m" - for number of monthly payments, \n type "p" - for the monthly payment:')
if choice == 'm':
    monthly_payment = int(input("Enter the monthly payment:"))
    months = round((loan_principal) / (monthly_payment))
    print("It will take ", months, " months to repay the loan")
elif choice == 'p':
    nummonths = int(input("Enter the number of months:"))
    monthlypayment = -(-(loan_principal) // nummonths)
    if loan_principal % nummonths != 0:
        lastpayment = loan_principal - monthlypayment * (nummonths - 1)
        print("Your monthly payment = ", monthlypayment, " and the last payment = ", lastpayment, ".")
    else:
        print("Your monthly payment = ", monthlypayment)

print(loan_principal)
print(first_month)
print(second_month)
print(third_month)
print(final_output)