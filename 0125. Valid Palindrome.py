class Solution(object):
    def isPalindrome(Self, String):
        String = String.lower()
        Result = ""
        for i in String:
            if i.isalnum():
                Result += i
        return Result == Result[::-1]