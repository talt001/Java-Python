##################                                                                  ####################
##################                    I have included a loop for                    ####################
##################                    testing.                                      ####################
##################                                                                  ####################
##################                                                                  ####################
##################                                                                  ####################



def main():

##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
####
    repeat = 'y'

    while repeat == ('y'):
####
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################

        print( )
        print( )
        print('******************************************************************************')
        print( )
        print( )
        print('Mix 2 of the 3 primary colors; red, blue and yellow.')
        print( )
        print( )
        
    ##establish 2 global variables through user input

        color1 = input('Enter the first color you want to mix: ', )
        print( )
        color2 = input('Enter the second color you want to mix: ', )
        print( )
        print( )

    ##establish flags defined by boolean statements regarding the variables
        
        f_red = ((color1 == 'red') and (color2 == 'red'))
        f_blue = ((color1 == 'blue') and (color2 == 'blue'))
        f_yellow = ((color1 == 'yellow') and (color2 == 'yellow'))
        f_purple = (((color1 == 'red') or (color1 == 'blue')) \
                    and ((color2 == 'red') or (color2 == 'blue')))
        f_orange = (((color1 == 'red') or (color1 == 'yellow')) \
                    and ((color2 == 'red') or (color2 == 'yellow')))
        f_green = (((color1 == 'yellow') or (color1 == 'blue')) \
                   and ((color2 == 'yellow')  or (color2 == 'blue')))
                                    
    ##use an if, elif, else statement to determine which of the flags is true
    ##define the color3 variable based on the evaluation of the flags
        
        if f_red:
            color3 = 'red'
        elif f_blue:
            color3 = 'blue'
        elif f_yellow:
            color3 = 'yellow'
        elif f_purple:
            color3 = 'purple'
        elif f_orange:
            color3 = 'orange'
        elif f_green:
            color3 = 'green'
        else:
            color3 = 'invalid colors'

    ##display the result of the if, elif, else statement
            
        print('You have mixed ',color3,'.', sep = '')
        print( )
        print( )
        print('******************************************************************************')


############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
####
####
        repeat = input('Do you wish to test this program for another set of values? (Enter y for yes): ', )
####   
####
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################

  
main()
