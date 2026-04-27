class Solution(object):
    def containsDuplicate(Self, Array):
        return len(Array) != len(set(Array))
