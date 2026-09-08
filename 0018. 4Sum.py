class Solution(object):
    def fourSum(self, Array, Target):
        Final_Array = []
        Array.sort()
        for i in range(len(Array) - 3):
            if i > 0 and Array[i] == Array[i - 1]:
                continue
            for j in range(i + 1, len(Array) - 2):
                if j > i + 1 and Array[j] == Array[j - 1]:
                    continue
                k, l = j + 1, len(Array) - 1
                while k < l:
                    if Array[i] + Array[j] + Array[k] + Array[l] == Target:
                        Final_Array.append([Array[i], Array[j], Array[k], Array[l]])
                        k += 1
                        l -= 1
                        while k < l and Array[k] == Array[k - 1]:
                            k += 1
                        while k < l and Array[l] == Array[l + 1]:
                            l -= 1
                    elif Array[i] + Array[j] + Array[k] + Array[l] < Target:
                        k += 1
                    else:
                        l -= 1
        return Final_Array