class Solution(object):
    def maxProduct(self, Array):
        Prefix_Product = Suffix_Product = 1
        Max = float('-inf')
        for i in range(len(Array)):
            if Prefix_Product == 0:
                Prefix_Product = 1
            if Suffix_Product == 0:
                Suffix_Product = 1
            Prefix_Product *= Array[i]
            Suffix_Product *= Array[len(Array) - i - 1]
            Max = max(Max, max(Prefix_Product, Suffix_Product))
        return Max