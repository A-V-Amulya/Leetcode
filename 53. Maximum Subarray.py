class Solution(object):
    def maxSubArray(Self, Array):
        Sum = 0
        Max = float('-inf')
        for i in Array:
            Sum += i
            if Sum > Max:
                Max = Sum
            if Sum < 0:
                Sum = 0 
        return Max 
