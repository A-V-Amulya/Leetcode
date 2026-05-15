class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(Self, x):
        Num, Sum = x, 0
        while Num > 0:
            Sum += Num % 10
            Num = Num // 10
        if x % Sum == 0:
            return Sum
        return -1 