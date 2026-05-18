class Solution(object):
    def reverseString(Self, Array):
        i, j = 0, len(Array) - 1
        while i < j:
            Array[i], Array[j] = Array[j], Array[i]
            i += 1
            j -= 1
        return Array