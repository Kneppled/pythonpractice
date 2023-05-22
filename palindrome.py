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

#test prints
print(checkPal('race car'))
print(checkPal('Abba'))
print(checkPal([123, 321]))
print(checkPal([121, 121]))
print(checkPal([121, 121, 121]))
print(checkPal([[121, 121], [121, 121]]))
print(checkPal([[123, 123], [123, 123]]))
print(checkPal(["abc", "abc"]))
