#Constant Global variables
RATE_OF_INFLATION=float(input('Rate of inflation in percent:'))
FR_RATE_OF_INFLATION=RATE_OF_INFLATION/100
START=0

#Using function to start while loop
def main():
    COST_OF_ITEM=float(input('Cost of item:'))
    YEARS_TILL_PURCHASE=int(input('Years until purchase:'))
#Return function back to start with minus 1 to
#year value to discontinue after alloted years
    while(START<YEARS_TILL_PURCHASE):
        COST_OF_ITEM=(COST_OF_ITEM*FR_RATE_OF_INFLATION)+COST_OF_ITEM
        YEARS_TILL_PURCHASE=YEARS_TILL_PURCHASE-1
#When years becomes 0, print cost and break loops
        while(YEARS_TILL_PURCHASE==0):
            print('Price after inflation:',format(COST_OF_ITEM, '.2f'))
            break
    return 0

#call main function
main()


