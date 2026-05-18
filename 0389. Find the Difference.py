class Solution(object):
    def findTheDifference(Self, String1, String2):
        Dict1 = {}
        Dict2 = {}
        for i in String1:
            if i in Dict1:
                Dict1[i] += 1
            else:
                Dict1[i] = 1
        for i in String2:
            if i in Dict2:
                Dict2[i] += 1
            else:
                Dict2[i] = 1
        for i in Dict2:
            if i not in Dict1 or Dict2[i] != Dict1[i]:
                return i