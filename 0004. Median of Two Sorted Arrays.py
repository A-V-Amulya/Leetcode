class Solution(object):
    def findMedianSortedArrays(Self, Array1, Array2):
        Merged_Array = []
        i = j = 0
        while i < len(Array1) and j < len(Array2):
            if Array1[i] < Array2[j]:
                Merged_Array.append(Array1[i])
                i += 1
            else:
                Merged_Array.append(Array2[j])
                j += 1
        while i < len(Array1):
            Merged_Array.append(Array1[i])
            i += 1
        while j < len(Array2):
            Merged_Array.append(Array2[j])
            j += 1
        N = len(Merged_Array)
        if N % 2 == 0:
            Median = (Merged_Array[N // 2 - 1] + Merged_Array[N // 2]) / 2.0
        else:
            Median = Merged_Array[N // 2]
        return Median