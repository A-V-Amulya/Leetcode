class Solution(object):
    def hammingDistance(Self, X, Y):
        return bin(X ^ Y).count("1")