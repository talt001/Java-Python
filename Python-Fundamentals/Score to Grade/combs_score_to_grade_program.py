#Write a function to convert a numerical grade to a letter grade
#Main() has been provided
#define scoretograde(numerical) so that when it is called in main()
#the correct output will be displayed

def main():

    score = int(input('Enter the numeric score (-1 to quit): '))

    while (score >= 0):
        print(score, 'get\'s a grade of', scoretograde(score))
        score = int(input('Enter the numeric score (-1 to quit): '))
    print()
    print('Thank\'s for playing!')


#definition of the missing function that allows the above code to work properly
def scoretograde(numerical):
    if numerical >= 90:
        return 'A'
    elif numerical >= 80:
        return 'B'
    elif numerical >= 70:
        return 'C'
    elif numerical >= 60:
        return 'D'
    else:
        return 'F'

main()
    
