# Name: Hanan El Abbar
# Prog Purpose: This program computes the cost of a Palermo Pizza purchase.


from datetime import date
import datetime
today = date.today()
print("Today's date:", today)

# Pizza Costs
pizzas = [
"Small", = 9.99
"Medium" = 12.99
"Large" = 14.99
"Extra Large" = 17.99
]

# define global variables
totalowed = 0
balance = 0
subtotal = 0
num_pizzas=0
SALES_TAX_RATE = .055
PR_SMALL = 9.99
PR_MEDIUM = 12.99
PR_LARGE = 14.99
PR_EXTRA_LARGE = 17.99

def main():
    another_order = True
    get_user_data()
    perform_calculations()
    display_results()
        yesno = input("\nWould you like to place another order? (Y/N): ")
        if yesno.upper() != "Y":
           another_order = False

def get_user_data():
    global num_pizzas
    num_pizzas = int(input("Desired pizza sizes: "))
    size= input("\nWhat pizza size do you want?(S/M/L/X):")
    if size.upper() != "S":
        print("output")

def perform_calculations ():
    global subtotal, sales_tax, total
    subtotal =num_ * PR_
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax

def display_results():
    print('------------------------------')
    print('**** Palermo Pizza ****')
    print('Pizza.pys')
    print('------------------------------')
    print('Pizzas      $ ' + format(subtotal, '8,.2f'))
    print('Sales Tax    $ ' + format(sales_tax,'8,.2f' ))
    print('Total        $ ' + format(total, '8,.2f'))
    print('------------------------------')
    print(str(datetime.datetime.now()))

    ########### call on pain program to execute ############
main()