def longestPalindrome(string):
    # If string is a single character or the string is a palindrome, return the string itself
    if (len(string) == 1 or (string == string[::-1])):
        return string

    else:
        palindrome = ""
        for i in range(len(string)):
            if (string[i] in string[i + 1:]):
                character = string[i]
                temp = string[i + 1:]
                indexFound = temp.rfind(character)
                newString = string[i] + temp[:indexFound + 1]
                print(newString)
                if (newString == newString[::-1]):
                    if (len(palindrome) < len(newString)):

                        palindrome = newString

        if (len(palindrome) > 0):
            return palindrome
        else:
            return (string[0])

print(longestPalindrome('aaabaaaa'))