def checkPalindrome(inputString):
    is_palindrome = True
    length = len(inputString)
    for i in range(length // 2):
        if inputString[i] != inputString[-1 - i]:
            is_palindrome = False
            break
    return is_palindrome


