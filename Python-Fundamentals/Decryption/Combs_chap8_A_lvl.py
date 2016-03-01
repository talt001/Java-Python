#Algorithm
#Write a program to decrypt and display the EncryptedList
#method used to encrypt the list
    #find a characters index in Key1 and substitute the character
    #in that same index in Key2
#decrypting will be the reverse
    #find a characters index in Key2 and substitue the character
    #in that same index in Key1
#Step 1 decrypt
#Step 2 display
#Step 3 sleep


#set these three lists as global tuples for saftey, purity, and speed
#we are being extra careful AND demonstrating use of the tuple function
Key1 = ['A','B','C','D','E','F','G','H','I', \
        'J','K','L','M','N','O','P','Q','R', \
        'S','T','U','V','W','X','Y','Z',' ']

Key1 = tuple(Key1)

Key2 = ['M','Q','X','H','N','U','V','B','O', \
        'K','A','C','Y','P','E','L',' ','J', \
        'W','S','R','T','I','F','D','Z','G']

Key2 = tuple(Key2)

EncryptedList = ['Q','N','M','Y','G','Y','N','G','R','L',
                 'G','W','X','E','S','S','D','G','G','S',
                 'B','N','J','N','W','G','P','E','G','O',
                 'P','S','N','C','C','O','V','N','P','S',
                 'G','C','O','U','N','G','B','N','J','N']

EncryptedList = tuple(EncryptedList)


#an encrypted list I made using the encryption protocol in
#the Algorithm
my_message = ['W', 'E', 'G', 'C', 'E', 'P', 'V', 'G',
              'M', 'P', 'H', 'G', 'S', 'B', 'M', 'P',
              'A', 'W', 'G', 'U', 'E', 'J', 'G', 'M',
              'C', 'C', 'G', 'S', 'B', 'N', 'G', 'U',
              'O', 'W', 'B']

my_message = tuple(my_message)

#define main function
def main():

    decrypt()

    #my first easter egg
    #uncomment the line below this one (message for hoopy froods only)
    #my_message_decrypt()

def decrypt():
    # provide value for logical comparison in while clause
    cryptlist_range = len(EncryptedList)

    # initiate a variable to hold rolling count for index in Encrypted list
    position = 0

    # establish logical conditions for interation through the loop
    while position < cryptlist_range:

        #returns the Key2 index of the letter found in EncryptedList[position]
        placeK2 = Key2.index(EncryptedList[position])

        #prints the letter in Key1 index corresponding to the Key2 index above
        #use of end = '' prints everything on one line to show the message
        print(Key1[placeK2], end ='')

        #moves the rolling count forward one position each iteration
        position += 1


def my_message_decrypt():

    #separate the messages
    print()
    print()
    
    # provide value for logical comparison in while clause
    my_message_range = len(my_message)

    # initiate a variable to hold rolling count for index in my_message list
    position = 0

    # establish logical conditions for interation through the loop
    while position < my_message_range:

        #returns the Key2 index of the letter found in my_message[position]
        placeK2 = Key2.index(my_message[position])

        #prints the letter in Key1 index corresponding to the Key2 index above
        #use of end = '' prints everything on one line to show the message
        print(Key1[placeK2], end ='')

        #moves the rolling count forward one position each iteration
        position += 1


#call the main function
main()


