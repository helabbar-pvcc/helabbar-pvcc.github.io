# Name: my name
# Prog Purpose: This program computes college tuition & fees based on number of credits
#   PVCC Fee Rates are from: https://www.pvcc.edu/tuition-and-fees
#   NOTE: All fees are PER CREDIT
#       In-state tuition: $155, Out-of-state tution: $331.60
#       Capital fee: $23.50 (out-of-state students only)
#       Instituion fee: $1.75
#       Activity fee: $2.90
import datetime
# define tution & fee rates
RATE_TUITION_IN = 155
RATE_TUTION_OUT = 331.60
RATE_CAPITAL = 23.5
RATE_INSTUTION = 1.75
RATE_ACTIVTY = 2.90

# define global variables
inout = 1 # 1 means in-state, 2 means out-of-state
numcredits = 0
scholarshipamt = 0
tuitionfee = 0
capitalfee = 0
institutionfee = 0
activityfee = 0
totalowed = 0
balance = 0

############ define program functions ############
def main():
    another_student = True
    while another_student:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("\nWould you like to calculate tuition & fees for another student? (Y/N): ")
        if yesno.upper() != "Y":
            another_student = False

def get_user_data():
    global inout, numcredits, scholarshipamt
    inout = int(input('Enter 1 for IN-STATE: enter a 2 for OUT-OF-STATE: '))
    numcredits = int(input('Number of credits registered for: '))
    scholarshipamt = float(input('Scholarship amount received: '))

def perform_calculations():
    global tuitionfee, capitalfee, institutionfee, activityfee, totalowed, balance
    if inout == 1:
        tuitionfee = numcredits * RATE_TUITION_IN
        capitalfee = 0
    else:
        tuitionfee = numcredits * RATE_TUTION_OUT
        capitalfee = numcredits * RATE_CAPITAL

    institutionfee = numcredits * RATE_INSTUTION
    activityfee = numcredits * RATE_ACTIVTY
    totalowed = tuitionfee + capitalfee + institutionfee + activityfee
    balance = totalowed - scholarshipamt    

def display_results():
    print('\n---------------------------------------')
    print('Number of credits : ' + str(numcredits))
    print('---------------------------------------')
    print('Tuition           $ ' + format(tuitionfee, '10,.2f'))
    print('Capital Fee       $ ' + format(capitalfee, '10,.2f'))
    print('Institution Fee   $ ' + format(institutionfee, '10,.2f'))
    print('Activity fee      $ ' + format(activityfee, '10,.2f'))
    print('Total             $ ' + format(totalowed, '10,.2f'))
    print('Scholarship       $ ' + format(scholarshipamt, '10,.2f'))
    print('---------------------------------------')
    print('Balance Owed      $ ' + format(balance, '10,.2f'))
    print('---------------------------------------')
    print(str(datetime.datetime.now()))
    print("NOTE: PVCC Fee Rates: https://www.pvcc.edu/tuition-and-fees")

########### call on pain program to execute ############
main()