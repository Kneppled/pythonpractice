#Global variables
PERCENT_INTEREST_MONTH=1.5
INTEREST_MONTH=PERCENT_INTEREST_MONTH/100
MONTHLY_PAYMENT=50

#create starting price of STEREO_COST
#Use count in loop to count number of loops for months until paid off
#Use TOTAL_INTEREST to add the prices of each loops INTEREST for total value of interest paid
def main():
    STEREO_COST=1000
    COUNT=0
    TOTAL_INTEREST=0
#while stereo cost is above 0 there is still credit to be paid
    while(STEREO_COST>0):
        INTEREST=STEREO_COST*INTEREST_MONTH
        STEREO_COST=(STEREO_COST-MONTHLY_PAYMENT)+(INTEREST)
        COUNT=COUNT+1
        TOTAL_INTEREST=TOTAL_INTEREST+INTEREST
#while stereo is equal or below 0 there is no money left to be paid and break to end
        while(STEREO_COST<=0):
            print('Months until paid off:',COUNT,'Total interest paid',format(TOTAL_INTEREST, '.2f'))
            break
#return function to start back at first while loop
    return 0
#call main function
main()
