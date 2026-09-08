class Solution(object):
    def threeSum(self, Array):
        Final_Array = []
        Array.sort()
        for i in range(len(Array) - 2):
            if i > 0 and Array[i] == Array[i - 1]:
                continue
            j, k = i + 1, len(Array) - 1
            while j < k:
                if Array[i] + Array[j] + Array[k] == 0:
                    Final_Array.append([Array[i], Array[j], Array[k]])
                    j += 1
                    k -= 1
                    while j < k and Array[j] == Array[j - 1]:
                        j += 1
                    while j < k and Array[k] == Array[k + 1]:
                        k -= 1
                elif Array[i] + Array[j] + Array[k] < 0:
                    j += 1
                else:
                    k -= 1
        return Final_Array