#enter the provided numbers into a list of "charge account" numbers
#prompt the user to enter a charge account number
#check the list for the charge account number
#if it is there tell the user the account number is valid
#if it is not there tell the user the account number is invalid
#give the user the option of entering another number or exiting

#define the main function
def main():

    print('Welcom To The Charge Number Validation Thing-a-majig')

    #enter the provided numbers into a list of "charge account" numbers
    charge_accounts = [5658845, 4520125, 7895122, 8777541, 8451277, 1302850, 8080152, 4562555, 5552012, 5050552, 7825877, 1250255, 1005231, 6545231, 3852085, 7576651, 7881200, 4581002]

    #prompt the user to enter a charge account number
    input_num = int(input('Enter a charge account number (or enter 0 to exit): '))  #give the user the option of entering another number or exiting

    #give the user the option of entering another number or exiting
    while input_num != 0:

        #check the list for the charge account number
        valid = find_number(input_num, charge_accounts)

        #if it is there tell the user the account number is valid
        if valid:
            print('That is a valid charge account number.')

        #if it is not there tell the user the account number is invalid
        else:
            print('That is NOT a valid charge number.')

        input_num = int(input('Enter a charge account number (or enter 0 to exit): '))


def find_number(input, list):
    validity = input in list    #check the list for the charge account number
    return validity

#call the main function
main()



