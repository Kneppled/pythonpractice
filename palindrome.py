# function to reverse the string or list given and return it
def reversePal(palindrome):
    return palindrome[::-1]


# function that returns true or false if given input is palindrome
def checkPal(palindrome):
    rPal = reversePal(palindrome)
    if (palindrome == rPal):
        return True
    return False


# Enters list of numbers or string as a string
palindrome = input('Enter a list of numbers or a string to check palindrome:')

ans = checkPal(palindrome)

if ans:      # if check pal returns true then the input is a palindrome
    print("Yes")
else:
    print("No")

print(checkPal('race car'))
print(checkPal('Abba'))
print(checkPal([123, 321]))
print(checkPal([121, 121]))
print(checkPal([121, 121, 121]))
print(checkPal([[121, 121], [121, 121]]))
print(checkPal([[123, 123], [123, 123]]))
print(checkPal(["abc", "abc"]))

# Take a look at the test cases and their results.  Code runs and checks for
# the most basic of palindromes but does come up with some questionable results
# Use blame in GitHub to find other changes I made to this file.
