#NAme: Hanan El Abbar
#Prog Purpose: Assignment
import datetime

# constants
PAY_RATES = (16.50, 15.75, 15.75, 19.50)
DEDUCTION_RATES = (0.12, 0.03, 0.062, 0.0145)

# global variables
category_code = "C"
hours_worked = 0
gross_pay = 0
federal_income_tax_deduction = 0
state_income_tax_deduction = 0
social_security_tax_deduction = 0
medicare_deduction = 0
total_deductions = 0
net_pay = 0

def get_user_input():
    global category_code, hours_worked
    category_code = input("\nEnter job category code (C, S, J, or M): ").upper()

    hours_worked = float(input("Enter hours worked: "))

def perform_calculations():
    global category_code, hours_worked, gross_pay, federal_income_tax_deduction, state_income_tax_deduction, social_security_tax_deduction, medicare_deduction, total_deductions, net_pay

    if category_code == "C":
        gross_pay = hours_worked * PAY_RATES[0]
    elif category_code == "S":
        gross_pay = hours_worked * PAY_RATES[1]
    elif category_code == "J":
        gross_pay = hours_worked * PAY_RATES[2]
    elif category_code == "M":
        gross_pay = hours_worked * PAY_RATES[3]
    else:
        print("Invalid job category code")

    federal_income_tax_deduction = hours_worked * DEDUCTION_RATES[0]
    state_income_tax_deduction = hours_worked * DEDUCTION_RATES[1]
    social_security_tax_deduction = hours_worked * DEDUCTION_RATES[2]
    medicare_deduction = hours_worked * DEDUCTION_RATES[3]

    total_deductions = federal_income_tax_deduction + state_income_tax_deduction + social_security_tax_deduction + medicare_deduction

    net_pay = gross_pay * total_deductions

def display_results():
    global category_code, hours_worked, gross_pay, federal_income_tax_deduction, state_income_tax_deduction, social_security_tax_deduction, medicare_deduction, total_deductions, net_pay
    print("----------- Fresh Food Marketplace Store -----------")
    print("Hours worked                  :  " + format(hours_worked, " >19.2f"))
    print("Gross pay                     : $" + format(gross_pay, " >19.2f"))
    print("-------------------- Deductions --------------------")
    print("Federal income tax deduction  : $" + format(federal_income_tax_deduction, " >19.2f"))
    print("State income tax deduction    : $" + format(state_income_tax_deduction, " >19.2f"))
    print("Social security tax deduction : $" + format(social_security_tax_deduction, " >19.2f"))
    print("Medicare deduction            : $" + format(medicare_deduction, " >19.2f"))
    print("--------------------- Summary ----------------------")
    print("Total deductions              : $" + format(total_deductions, " >19.2f"))
    print("Net pay                       : $" + format(net_pay, " >19.2f"))
    print(datetime.datetime.now())

def main():
    another_employee = True
    while another_employee:
        get_user_input()
        perform_calculations()
        display_results()
        user_input = input("\nWould you like to enter data for another employee (Y or N)? ")
        if user_input.upper() != "Y":
            another_employee = False

main()