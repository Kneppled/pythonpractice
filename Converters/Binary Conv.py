def main():
    num=int(input("Enter a number:"))   #user input
    Bin=''                              #set string value for Bin
    if (num!=0):                        #if number is not 0 it will start loop.
        while (num>=1):                 #continue loop until num<1
            if (num%2==0):              #remainder of number is equal to 0
                Bin=Bin+"0"
                num=num/2
            else:                       #remainder is not equal to 0
                Bin=Bin+"1"
                num=(num-1)/2           #-1 from num to remove remainder.
    else:
        Bin="0"
    numPrint(Bin)
    
def numPrint(Bin):
    for x in reversed(Bin):             #reversed each number to correct order
        print(x, end="")                #end is used to not make a new line.

main()                                  #run function
