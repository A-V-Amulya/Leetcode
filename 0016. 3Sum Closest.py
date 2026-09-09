class Solution(object):
    def threeSumClosest(self, Array, Target):
        Array.sort()
        Closest_Sum = Array[0] + Array[1] + Array[2]
        for i in range(len(Array) - 2):
            if i > 0 and Array[i] == Array[i - 1]:
                continue
            j, k = i + 1, len(Array) - 1
            while j < k:
                Current_Sum = Array[i] + Array[j] + Array[k]
                if Current_Sum == Target:
                    return Current_Sum
                if abs(Target - Current_Sum) < abs(Target - Closest_Sum):
                    Closest_Sum = Current_Sum
                if Current_Sum < Target:
                    j += 1
                else:
                    k -= 1
        return Closest_Sum