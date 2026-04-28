class Solution(object):
    def merge(Self, Array1, M, Array2, N):
        i, j, k = M + N - 1, M - 1, N - 1
        while j >= 0 and k >= 0:
            if Array1[j] > Array2[k]:
                Array1[i] = Array1[j]
                j -= 1
            else:
                Array1[i] = Array2[k]
                k -= 1
            i -= 1
        while k >= 0:
            Array1[i] = Array2[k]
            k -= 1
            i-= 1
        return Array1 
