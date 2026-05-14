class Solution(object):
    def containsDuplicate(Self, Array):
        Dict = {}
        for i in Array:
            if i in Dict:
                return True
                break
            else:
                Dict[i] = 1
        return False