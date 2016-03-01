##################                                                                  ####################
##################                    I have included a commented                   ####################
##################                    out 'while loop' in order to                  ####################
##################                    facilitate testing.                           ####################
##################                                                                  ####################
##################                                                                  ####################

#get runner name for each of 3 runners
#get runner time for each of 3 runners
#compare and report finish order

def main():


#############################################################################################*#############
##########################################################################################################
##########################################################################################################
##########################################################################################################

        repeat = 'y'

        while repeat == ('y'):

##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################


#get runner names
#print a 'space' between input lines to let things breath


                print( )
                print( )
                print('*******************************************************************************')
                print( )
                print( )
                run_name_1 = input('What is the name of runner 1? ',)
                print( )
                run_name_2 = input('What is the name of runner 2? ',)
                print( )
                run_name_3 = input('What is the name of runner 3? ',)

                print( )
                print( )

#get race times
#print a 'space' between input lines to let things breath
                
                run_time_1 = float(input("What is runner one's race time in seconds? "))
                print( )
                run_time_2 = float(input("What is runner two's race time in seconds? "))
                print( )
                run_time_3 = float(input("What is runner three's race time in seconds? "))

                print( )
                print( )

####there are 13 unique orders in which runners 1, 2 and 3 can finish the race.
####they are defined below using boolean comparison and logical operators
####when a particular order is recognized by the decision structure, it will activate the print statements
####print a 'space' between output lines to let things breath
                
                if (run_time_1 < run_time_2) and (run_time_2 < run_time_3):
                    print('First place:', run_name_1)
                    print( )
                    print('Second place:',run_name_2)
                    print( )
                    print('Third place:', run_name_3)

                elif (run_time_1 < run_time_3) and (run_time_3 < run_time_2):
                    print('First place:', run_name_1)
                    print( )
                    print('Second place:',run_name_3)
                    print( )
                    print('Third place:', run_name_2)

                elif (run_time_2 < run_time_1) and (run_time_1 < run_time_3):
                    print('First place:', run_name_2)
                    print( )
                    print('Second place:',run_name_1)
                    print( )
                    print('Third place:', run_name_3)

                elif (run_time_2 < run_time_3) and (run_time_3 < run_time_1):
                    print('First place:', run_name_2)
                    print( )
                    print('Second place:',run_name_3)
                    print( )
                    print('Third place:', run_name_1)

                elif (run_time_3 < run_time_1) and (run_time_1 < run_time_2):
                    print('First place:', run_name_3)
                    print( )
                    print('Second place:',run_name_1)
                    print( )
                    print('Third place:', run_name_2)

                elif (run_time_3 < run_time_2) and (run_time_2 < run_time_1):
                    print('First place:', run_name_3)
                    print( )
                    print('Second place:',run_name_2)
                    print( )
                    print('Third place:', run_name_1)

                elif (run_time_1 == run_time_2) and (run_time_2 < run_time_3):
                    print(run_name_1,'and', run_name_2,'tie for first place. Second place goes to', run_name_3,'.')

                elif (run_time_3 < run_time_1) and (run_time_1 == run_time_2):
                    print(run_name_3,'takes first place.', run_name_1,'and', run_name_2,'tie for second place.')

                elif (run_time_1 == run_time_2) and (run_time_2 == run_time_3):
                    print(run_name_1,', ',run_name_2,' and ', run_name_3,' finish in a three way tie.',sep='')

                elif (run_time_1 == run_time_3) and (run_time_3 < run_time_2):
                    print(run_name_1,'and', run_name_3,'tie for first place. Second place goes to', run_name_2,'.')

                elif (run_time_2 < run_time_1) and (run_time_1 == run_time_3):
                    print(run_name_2,'takes first place.', run_name_1,'and', run_name_3,'tie for second place.')

                elif (run_time_1 < run_time_2) and (run_time_2 == run_time_3):
                    print(run_name_1,'takes first place.', run_name_2,'and', run_name_3,'tie for second place.')

                elif (run_time_2 == run_time_3) and (run_time_3 < run_time_1):
                    print(run_name_2,'and', run_name_3,'tie for first place. Second place goes to', run_name_1,'.')

##originally this else statement was used during testing to see if anything was falling all the way
##through the decision structure. Now it hangs around doing nothting.

                else:
                    print('Your results have fallen all the way through the decision structure.  They should not have.')

####provide more spacing and a visual seperation (if you choose to reactivate the while loop)    
                print( )
                print( )
                print('*******************************************************************************')

###############################################################################################*#############
############################################################################################################
############################################################################################################
############################################################################################################
####

        repeat = input('Do you wish to test this program for another set of values? (Enter y for yes): ', )
   
####
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################

  
##call the main function        
main()
