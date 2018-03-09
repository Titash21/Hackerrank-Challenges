def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    print("String is", s,end=" ")
    s = s.strip(" ")
    lists = s.split(" ")
    print("Length of last word is",len(lists[len(lists) - 1]))

lengthOfLastWord("a b c")
lengthOfLastWord("abc d  ")
lengthOfLastWord("Hello World")
lengthOfLastWord("Hello Titash   ")