import time         # to pause program for a period of time
import sys          # to end program if user fails to answer correctly

print('Good morning, Welcome to The Inn!')
print('My name is Dan and I will be your server today.')
print('')
price=0             # set hidden price for meal
tryAgain = 'yes'
while tryAgain == 'yes':
    print("Today's available drinks are: pepsi, coffee, and water.")
    drink = input('What drink can I start you off with today?')
    print('')
    if drink == 'pepsi':
        print('I will be back with your drink very soon, thank you.')
        time.sleep(3)
        print('Here is your pepsi.')
        price=price+1
        tryAgain = 'no'
    elif drink == 'coffee':
        print('I will be back with your drink very soon, thank you.')
        time.sleep(5)
        print('Here is your coffee.')
        price=price+1.5
        tryAgain = 'no'
    elif drink == 'water':
        print('I will be back with your drink very soon, thank you.')
        time.sleep(3)
        print('Here is your water.')
        tryAgain = 'no'
    else:
        print('That is not a valid drink option from our menu.')
        tryAgain = 'yes'        # to allow customers to keep ordering /
                                # if they get the drink name wrong

print('')
time.sleep(2)              
wait = 'yes'
while wait != 'no':
    print("Today's menu consists of steak, lobster, scallops, or lamb")
    wait=input('Would you like more time before ordering?')
    print('')
    time.sleep(3)

    
validFood = 'no'                # in case of invalid food order
while validFood == 'no':        # customer can keep ordering
    food = input('Okay, what will you be having today?')
    if food == 'steak':
        time.sleep(3)
        print('Here is your steak.')
        price=price+19.25
        validFood='yes'
    elif food == 'lobster':
        time.sleep(3)
        print('Here is your lobster.')
        price=price+24.95
        validFood = 'yes'
    elif food == 'scallops':
        time.sleep(3)
        print('Here is your scallops.')
        price=price+16
        validFood = 'yes'
    elif food == 'lamb':
        time.sleep(3)
        print('Here is your lamb.')
        price=price+12
        validFood = 'yes'
    else:
        print('This is not a valid food option')
        validFood = 'no'

print('')
time.sleep(5)
print('It looks like you are finished.')
print('Here is the bill for the meal, the total comes out to $',price)
print('')
time.sleep(5) 
print('Okay, I will take this to the back and return with your receipt.')
print('')
time.sleep(5)
print('Here is your receipt.')
time.sleep(1)
print('Thank you for eating at The Inn!')
