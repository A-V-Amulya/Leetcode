class Solution(object):
    def twoSum(Self, Array, Target):
        for i in range(len(Array) - 1):
            for j in range(i + 1, len(Array)):
                if Array[i] + Array[j] == Target:
                    return [i,j]
