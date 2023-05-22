import sys

print("Numeric Converter")
print("Choose your input number system.")
numSys = input("Enter 1 for decimal, 2 for binary, 3 for hexidecimal:")
print('')
print("Choose your input number system that you want to convert to.")
numCon= input("Enter 1 for decimal, 2 for binary, 3 for hexidecimal:")

if numSys == numCon:
    print('')
    print('Same number, Restart program.')
    sys.exit('End program')
else:
    print('')
    
con = True

while con == True:
    if numSys == '1' and numCon == '2':
        print('Decimal to Binary')
        num=int(input("Enter a number in Decimal:"))
        Bin=''                              # set string value for Binary (Bin)
        if (num > 0):                       
            while (num>=1):                 # continue loop until num<1
                if (num%2==0):              # remainder of number is equal to 0
                    Bin=Bin+"0"
                    num=num/2
                else:                       # remainder is not equal to 0
                    Bin=Bin+"1"
                    num=(num-1)/2           # -1 from num to remove remainder.
        else:
            Bin="0"
        for x in reversed(Bin):             # reverse to correct binary order
            print(x, end="")  
        con = False
        
    elif numSys == '1' and numCon == '3':
        print('Decimal to Hexidecimal')
        num=int(input("Enter a number in Decimal:"))
        ans = num
        Hex = ''
        while ans > 0:
            rem = ans % 16
            ans = int(ans / 16)
            if (rem < 10):
                Hex += str(rem)
                del rem
            elif (rem == 10):
                Hex += 'A'
                del rem
            elif (rem == 11):
                Hex += 'B'
                del rem
            elif (rem == 12):
                Hex += 'C'
                del rem
            elif (rem == 13):
                Hex += 'D'
                del rem
            elif (rem == 14):
                Hex += 'E'
                del rem
            elif (rem == 15):
                Hex += 'F'
                del rem
                
        for x in reversed(Hex):    
            print(x, end="")
            
        con = False
        
    elif numSys == '2' and numCon == '1':
        print('Binary to Decimal')
        Bin=int(input("Enter a number in Binary:")) # Bin = Binary
        dec = 0                                     # Set Decimal to 0
        count = 0                                   # Set count for loop
        while Bin != 0:
            rem = Bin % 10                          # Find remainder
            dec = dec + rem * (2 ** count)          
            Bin = Bin // 10
            count+=1
        print(dec)
        con = False

        
    elif numSys == '2' and numCon == '3':
        print('Binary to Hexidecimal')
        Bin=int(input("Enter a number in Binary:")) # Bin = Binary
        dec = 0                                     # Set Decimal to 0
        count = 0                                   # Set count for loop
        while Bin != 0:
            rem = Bin % 10                          # Find remainder
            dec = dec + rem * (2 ** count)          
            Bin = Bin // 10
            count+=1

        num=dec
        ans = num
        Hex = ''
        while ans > 0:
            rem = ans % 16
            ans = int(ans / 16)
            if (rem < 10):
                Hex += str(rem)
                del rem
            elif (rem == 10):
                Hex += 'A'
                del rem
            elif (rem == 11):
                Hex += 'B'
                del rem
            elif (rem == 12):
                Hex += 'C'
                del rem
            elif (rem == 13):
                Hex += 'D'
                del rem
            elif (rem == 14):
                Hex += 'E'
                del rem
            elif (rem == 15):
                Hex += 'F'
                del rem
                
        for x in reversed(Hex):    
            print(x, end="")
            
        con = False

        
    elif numSys == '3' and numCon == '1':
        print('Hexidecimal to Decimal')
        num=input("Enter a number in Hexidecimal:")
        exp = len(num) - 1
        total = 0
        for char in num:
            if char == 'A':
                value = 10
            elif char == 'B':
                value = 11
            elif char == 'C':
                value = 12
            elif char == 'D':
                value = 13
            elif char == 'E':
                value = 14
            elif char == 'F':
                value = 15
            else:
                value = int(char)
            dec = (value)*(16**exp)
            exp -= 1
            total += dec
        print(total)
            
        con = False                                 
    
        
    elif numSys == '3' and numCon == '2':
        print('Hexidecimal to Binary')
        Hex=input("Enter a number in Hexidecimal:")
        exp = len(Hex) - 1
        total = 0
        for char in Hex:
            if char == 'A':
                value = 10
            elif char == 'B':
                value = 11
            elif char == 'C':
                value = 12
            elif char == 'D':
                value = 13
            elif char == 'E':
                value = 14
            elif char == 'F':
                value = 15
            else:
                value = int(char)
            dec = (value)*(16**exp)
            exp -= 1
            total += dec
        num = total
        Bin=''                              
        if (num > 0):                       
            while (num>=1):                 
                if (num%2==0):              
                    Bin=Bin+"0"
                    num=num/2
                else:                       
                    Bin=Bin+"1"
                    num=(num-1)/2           
        else:
            Bin="0"
        for x in reversed(Bin):          
            print(x, end="")  
        con = False

        
    else:
        print('Try again.')
        print('')
        numSys = input("Enter 1 for decimal, 2 for binary, 3 for hexidecimal:")
        print('')
        numCon= input("Enter 1 for decimal, 2 for binary, 3 for hexidecimal:")
        con = True
