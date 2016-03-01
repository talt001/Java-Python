#Step 1 write a python function that will calculate monthly payments on
# a loan.

#Step 2 pass the following to your function
#Principle of $20,000, with an APR of 4% to be paid in
#   1.) 36 months
#   2.) 48 months
#   3.) 60 months
#   4.) 72 months

#Step 3 include code for user supplied loan terms and comment out

#define the main function
def main():

#set some global constants for loan terms
    Principle = 20000.00
    APR = 0.04
    rate = APR / 12

    print('On a $20,000.00 loan, with 4% APR:')
    print()

#iterate through 3, 4, 5, and 6 'years' and multiply by twelve to provide the argument 'n' in
#the proper terms - months
    
    for years in range(3, 7):

        n = years * 12 

#assign the function to a variable for formatting in the print statements to follow
#calling the function directly within print() produces an error        
        payment = Calculate_monthly_payment(Principle, n, rate)
        
        print('Your monthly payments will be $', format(payment, ',.2f'), ' when you borrow for ', n,' months.', sep = '')
        print()


# code for user provided loan terms
#    x, y, z = Get_loan_terms()
#    payment = Calculate_monthly_payment(x, y, z)
#    print('Your monthly payment will be $', format(payment, ',.2f'), sep = '')


# code for user provided loan terms
##def Get_loan_terms():
##    Principle = float(input('Enter the loan amount: '))
##    n = int(input('Enter duration of loan in months: '))
##    APR = float(input('Enter the APR: '))
##    rate = APR / 12
##    return Principle, n, rate


#define the function to calculate monthly payments by writing a math expression
#return the value to mainn()
def Calculate_monthly_payment(Principle, n, rate):

    monthly = Principle*((rate*(1+rate)**n))/((1+rate)**n - 1)

    return monthly

#call the main function
main()
    
    
