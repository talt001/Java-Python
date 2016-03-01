#open and read a .txt file containing an unknown number of records
#spread across 3 fields
#process the data read
#output to another .txt file which the user will name
#in a column format the customer has specified

#define the main function
def main():

#open input file in read mode and asscoiate with file object emp_data
    emp_data = open('Input - A Level.txt', 'r')

#create output file in write mode and associate with file object emp_pay
    emp_pay = open(name_file(), 'w')

#priming read with readline method
    name = emp_data.readline()

#loop tests for empty strings to stop at the end of the input file
    while name != '':

        rate = emp_data.readline()

        hours = emp_data.readline()

        name, rate, hours = strip_newline(name, rate, hours)

        rate, hours = unstring(rate, hours)

        output_calc(emp_pay, name, rate, hours)

        name = emp_data.readline()

#close the input and output files
    emp_pay.close()
    emp_data.close()

    print('Your data has been written to your .txt file')
    
#Explain the program to the user and prompt for a name for the output file.
def name_file():
    print('This program will read records for employee name, pay rate')
    print('and hours worked.  It will output the employee\'s name')
    print('and gross pay for the week in a .txt file.')
    return (input('Choose a file name for employee gross pay data. ') + '.txt')


#strip the newline (\n) characters from the end of each field in the source .txt
#this is required to get output formatting right later
def strip_newline(employee, wage, time):

    employee = employee.rstrip('\n')
    wage = wage.rstrip('\n')
    time = time.rstrip('\n')

    return employee, wage, time

#convert numbers stored as strings back into numeric values so they can be
#used in calculations
def unstring(str_wage, str_time):

    num_wage = float(str_wage)
    num_time = int(str_time)

    return num_wage, num_time

#pass a value for a file object to the function
#carry out calculations and formating
#write to the file associated with the file object
def output_calc(output_object, employee, wage, time):
    output_object
    employee = employee.ljust(9, )  #corrects tabs for short names
    pay = wage*time
    str_pay = str('Gross Pay: $' + format(pay, ',.2f'))
    output_object.write(employee + '\t')    #\t for columns (see requirements)
    output_object.write(str_pay + '\n')

#call the main function
main()
