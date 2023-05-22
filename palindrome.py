#global variable
another = 'yes'

# function to reverse the string or list given and return it
def reversePal(palindrome):
    return palindrome[::-1]


# function that returns true or false if given input is palindrome
def checkPal(palindrome):
    rPal = reversePal(palindrome)
    if (palindrome == rPal):
        return True
    return False


def main(another):
    while another == 'yes':
        # Enters list of numbers or string as a string
        palindrome = input('Enter a list of numbers or a string to check palindrome:')
        #runs functions above to return true or false
        ans = checkPal(palindrome)
        if ans:      # if check pal returns true then the input is a palindrome
            print("Yes")
        else:
            print("No")
        another = input('Would you like to try another(yes or no):')
        print("")
    else:
        exit
    

main(another)

