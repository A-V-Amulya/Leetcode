class Solution(object):
    def majorityElement(Self, Array):
        Dict = {}
        for i in Array:
            if i not in Dict:
                Dict[i] = 1
            else:
                Dict[i] += 1
        for Key, Value in Dict.items():
            if Value > len(Array) / 2:
                return Key  