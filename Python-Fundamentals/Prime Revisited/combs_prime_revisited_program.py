#Write a modularized program to gather user input to determine the prime
#numbers within a user supplied range of integers

#Step 1     Ask the user for a range of integers to check for prime
#numbers.

#Step 2     Write a function for the main line logic to iterate the range
#of numbers through, in order to check each number for "primeness".


#lay down the main line logic (in the main function)
#that will call the functions necessary to complete steps 1 and 2
#print empty lines with print() to provide white space in the output.

def main():

    start, end = input_range()

    for number in range(start, end + 1):

        is_prime, integer = check(number)
        
        if is_prime:
        
            print(integer, 'is a prime number.')

            
#define a function to inform the user of the purpose
#of the program and get user input for a range of integers
#to check for prime numbers


def input_range():

    print('Welcome to the Wiz-bang prime number finder thingy.')
    print('Enter a range of positive integers to search for prime numbers.')
    print('Since 2 is the first prime number, any starting point')
    print('less than 2 will be changed to 2.')
    print()

    start = int(input('Where should the range begin? '))
    print()

    if start < 2:
        start = 2
        print('Error, your starting point is invalid.  It has been set at 2')
        print()

    end = int(input('Where should the range end? '))
    print()
    
    return start, end


#define a function to check an integer in order to
#determine if is a prime number.
#it must iterate through modulus division
#and return a boolean value and the integer being
#checked.

def check(num):

    is_prime = True

    for digit in range(2, num):

        assess = num % digit
    
        if assess == 0:

            is_prime = False

    return is_prime, num


#call the main function
main()



##2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 
##
##
##73 79 83 89 97 101 103 107 109 113 127 131 137 139 149 151 157 163 167 173 
##
##
##179 181 191 193 197 199 211 223 227 229 233 239 241 251 257 263 269 271 277 281 
##
##
##283 293 307 311 313 317 331 337 347 349 353 359 367 373 379 383 389 397 401 409 
##
##
##419 421 431 433 439 443 449 457 461 463 


