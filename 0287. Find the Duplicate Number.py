class Solution(object):
    def findDuplicate(Self, Array):
        Fast, Slow = Array[0], Array[0]
        while True:
            Slow = Array[Slow]
            Fast = Array[Array[Fast]]
            if Slow == Fast:
                break
        Fast = Array[0]
        while Slow != Fast:
            Slow = Array[Slow]
            Fast = Array[Fast]
        return Fast