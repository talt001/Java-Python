#Algorithm
#Step 1 - Input
#Step 2 - Sequence
#Step 3 - Generate Pairings: subtask 1: divide list into two equal halves
#Step 4 - Generate Pairings: subtask 2: create the pairings
#Step 5 - Display Pairings

#define the main function
def main():

    #Input
    player_list = input()

    #Sequence
    sorted_players = Sequence(player_list)

    #Generate Pairings subtask 1: divide list into two equal halves
    group1, group2 = divide(sorted_players)
    
    #Generate Pairings subtask 2: create the pairings
    pairings = generate_pairings(group1, group2)

    #A little banter to let the user know what is going on
    print('Welcome to the ACC All Valley Chess Championship')
    print()
    print('Sweep the king!')
    print()
    print('Round 1: Fight!')
    print()

    #Display Pairings
    display_pairings(group1, pairings)


#Input
#read a .txt file to create a list of players
def input():
    
    chess_players = open('Input - chess.txt', 'r')

    player_list = chess_players.readlines()

    chess_players.close()

    index = 0

    while index < len(player_list):

        player_list[index] = player_list[index].rstrip('\n')

        index += 1

    return player_list

#Sequence
#sort the list of players into decending order (highest ranked first)
def Sequence(players):
    
    players.sort()

    players.reverse()

    return players

#Generate Pairings subtask 1: divide list into two equal halves
#create two empty lists and use iterative logic to fill them
def divide(player_pool):
    
    pool1 = []
    pool2 = []
    
    index = 0
    
    while index < len(player_pool):
        
        if index < len(player_pool)//2:
            pool1.append(player_pool[index])
        else:
            pool2.append(player_pool[index])
        index += 1

    return pool1, pool2
    
#Generate Pairings subtask 2: create the pairings
#make a two dimensional list from our two lists
#each sublist or 'row' will contain a pairing consisting of
#1 player from group1 and 1 player from group2
def generate_pairings(pool1, pool2):

    matches = [['',''],
               ['',''],
               ['',''],
               ['',''],
               ['','']]
                

    for r in range(len(pool1)):
        for c in range(2):
            matches[r][0] = pool1[r]
            matches[r][1] = pool2[r]

    return matches

#Display Pairings
#use a count controled loop (range to be determined by the length of either list) to
#generate the display of the pairings by referencing the two dimensional list
def display_pairings(pool1, matches):
    
    for r in range(len(pool1)):
        print('In ring', r + 1, ', on board', r + 1, ': ', matches[r][0], ' VS. ', matches[r][1])
        print()

#call the main function
main()
