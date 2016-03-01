##complete programming exercise # 7 in Chapter 7, P. 293:
##
##"Write a program that writes a series of random numbers to a disk file.  Each
##random number should be in the range of 1 through 100.  The program should let
##the user specify how many random numbers the file will hold."
##
##See section 6.1 for info on generating random numbers.


#import the random module
import random

#define the main function
def main():

    #open random.txt in write mode and associate it with the file object random_file
    random_file = open('random.txt', 'w')

    #ask the user how many random numbers they want to print to the output file
    print('This program will generate random numbers in the range 1 through 100 and')
    print('output them to a .txt file named random.txt.')
    n = int(input('How many random numbers do you want to write to the output file? '))

    #initiate a for loop to count through the amount of random numbers the user wants to print
    for count in range(1, n + 1):

        #pass the randint(range 1-100) function through the str() function and use the result as an argument
        #for the write method on the file object
        #don't forget to add a newline character so the numbers don't all run together
        random_file.write(str(random.randint(1, 100)) + '\n')

    #close the output file with the close method of the file object
    random_file.close()

    #tell the user their numbers have printed, and what the file name is.
    print('Your numbers have printed to the file random.txt.')

#call the main function
main()

    
