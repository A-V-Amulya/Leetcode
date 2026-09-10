class Solution(object):
    def removeElement(self, Array, Value):
        i, j = 0, len(Array) - 1
        while i <= j:
            while i <= j and Array[i] != Value:
                i += 1
            while i <= j and Array[j] == Value:
                j -= 1
            if i <= j:
                Array[i], Array[j] = Array[j], Array[i]
        return i