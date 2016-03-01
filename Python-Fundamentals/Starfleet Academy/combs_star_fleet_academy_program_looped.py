##################                                                                  ####################
##################                    I have included a loop for testing.           ####################
##################                                                                  ####################
##################                                                                  ####################
##################                                                                  ####################
##################                                                                  ####################


#Star Fleet Academy Entrance Evaluaton

#First name
#Age
#GPA
#SAT
#Race

#GPA >= 2.0
#SAT >= 800
#Age >= 17
#except Vulcans >= 16
#race(not(race == romulan))



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
        print('***************************************************************************')
        print( )
        print( )
        print('Welcome to the Star Fleet Academy Online Application!')
        print( )
        print('Tell us about yourself.')
        print( )
        print( )


        First_name = input('Applicant name:  ',)
        print( )
        Age = int(input('Age:  ',))
        print( )
        GPA = float(input('GPA:  ',))
        print( )
        SAT = int(input('SAT:  ',))
        print( )
        Race = input('Race:  Human, Vulcan, Klingon, Romulan or Other? ',)
        print( )
        print( )

        
        f_admittance_1 = ((GPA >= 2.0) and (SAT >= 800) and ((Age >= 17)\
                        or (Age >= 16 and (Race == 'Vulcan')))\
                        and not(Race == 'Romulan'))

        f_admittance_2 = ((GPA >= 3.5) and ((Age >= 17) or (Age >= 16\
                        and (Race == 'Vulcan'))) and not(Race == 'Romulan'))

        f_admittance_3 = ((SAT >= 1100) and ((Age >= 17)\
                        or (Age >= 16 and (Race == 'Vulcan')))\
                        and not(Race == 'Romulan'))

        f_admittance_4 = ((SAT >= 1500) and not(Race == 'Romulan'))

        if f_admittance_4:
            qualification = 1

        elif f_admittance_3:
            qualification = 1

        elif f_admittance_2:
            qualification = 1

        elif f_admittance_1:
            qualification = 1

        else:
            qualification = 0

        print('You have entered the following:')
        print( )
        print('Name:', First_name)
        print( )
        print('Age: ', Age)
        print( )
        print('GPA: ', GPA)
        print( )
        print('SAT: ', SAT)
        print( )
        print('Race: ', Race)
        print( )
        print( )

        if qualification == 1:
            print('You are accepted into Starfleet Academy. \
Welcome to the fleet.')
            print( )
            print( )

        else:
            print('Sorry, but you do not meet the minimum requirements.')
            print( )
            print( )

        if Race == 'Romulan':
            print('Starfleet Officers are being dispatched to \
assist you in returning to the')
            print('Neutral Zone.')
            print( )
            print( )
            print('***************************************************************************')
            print( )
            print( )

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


