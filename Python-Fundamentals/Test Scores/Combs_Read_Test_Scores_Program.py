#read an unknown number of test scores from a txt file
#report them as they are read
#average them
#determin highest and lowest scores
#mimic example output format


#define the main function
def main():

#open input txt and associate file object with it in read mode
    score_obj = open('Input - B Level.txt', 'r')

#start an accumulator for the average calculation
    total = 0.0

#start a counter for reporting and to determine the divisor for
#the average calculation
    count = 0

#a priming value for comparison
    highest = 0.0

#a priming value for comparison
    lowest = 100.0

#read the lines in the input txt using a for loop    
    for line in score_obj:

#covert string to numeric value
        score = float(line)

#add to the accumulator each iteration (read line)
        total += score

#add to the count each itereration (read line)
        count += 1

#formating 
        list_num = 'Score #' + str(count)
#formating
        list_num = list_num.ljust(9, ) #left justified method

#formating, printing first portion of results
        print(list_num, ' : ', format(score, '5.2f'))

#use a function to run through a new loop with a file
#object associated with the innput txt for comparison
#to determine highest score
        if higher(score) > highest:

            highest = higher(score)

#use a function to run through a new loop with a file
#object associated with the innput txt for comparison
#to determine lowest score
        if lower(score) < lowest:

            lowest = lower(score)

#determine average score using the accumulator and counter
#required since the number of scores will not be known ahead
#of time.
    avg = total / count

#print second portion of results
    print('Highest Score:', format(highest, '.2f'))

    print('Lowest Score :', format(lowest, '.2f'))

    print('Average Score:', format(avg, '.2f'))

#pass the current value for score for each iteration of the
#initial loop into this function to compare to each other value
#in the file and pass the results back up
def higher(score_):

    compare_obj = open('Input - B Level.txt', 'r')

    for line in compare_obj:

        grade = float(line)

        if score_ > grade:

            return score_

        else:

            return grade

#pass the current value for score for each iteration of the
#initial loop into this function to compare to each other value
#in the file and pass the results back up
def lower(score_):

    compare_obj = open('Input - B Level.txt', 'r')

    for line in compare_obj:

        grade = float(line)

        if score_ < grade:

            return score_

        else:

            return grade
                
#call the main function
main()
