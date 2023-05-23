import random

ans='yes'
while ans=='yes':
    print()
    print('Basic Math problems')
    num=random.randint(0,20)
    num2=random.randint(0,20)
    x=int(input('Enter 1 to add, 2 to subtract,' \
                '3 to multiply, 4 to divide, 0 for random:'))
    print('')
    Continue=True
    
    if x==0:
        x=random.randint(1,4)
        
    if x==1:
        while Continue==True:
            print(num,'+',num2,'=')
            print('')
            ans=int(input('Enter your answer to the problem:'))
            print('')
            if num+num2==ans:
                print('correct')
                print()
                Continue=False
            else:
                print('incorrect')
                print()
                Quit=input('Would you like to give up?')
                if Quit=='Yes' or Quit=='yes':
                    Continue=False
                else:
                    Contine=True
    elif x==2:
        while Continue==True:
            print(num,'-',num2,'=')
            print('')
            ans=int(input('Enter your answer to the problem:'))
            print('')
            if num-num2==ans:
                print('correct')
                print()
                Continue=False
            else:
                print('incorrect')
                print()
                Quit=input('Would you like to give up?')
                if Quit=='Yes' or Quit=='yes':
                    Continue=False
                else:
                    Contine=True
        
    elif x==3:
        while Continue==True:
            print(num,'*',num2,'=')
            print('')
            ans=int(input('Enter your answer to the problem:'))
            print('')
            if num*num2==ans:
                print('correct')
                print()
                Continue=False
            else:
                print('incorrect')
                print()
                Quit=input('Would you like to give up?')
                if Quit=='Yes' or Quit=='yes':
                    Continue=False
                else:
                    Contine=True
        
    elif x==4:
        while Continue==True:
            print(num,'/',num2,'=')
            print('')
            ans=float(input('Enter your answer to the problem:'))
            print('')
            if num/num2==ans:
                print('correct')
                print()
                Continue=False
            else:
                print('incorrect')
                print()
                Quit=input('Would you like to give up?')
                if Quit=='Yes' or Quit=='yes':
                    Continue=False
                else:
                    Contine=True
        
    else:
        print('error')
        
    print('')
    ans=input('Would you like to try another problem (yes or no)?')
    
while ans=='no':
    print('')
    print('See you soon!')
    break



