class Solution(object):
    def isAnagram(Self, String1, String2):
        if len(String1) != len(String2):
            return False
        String1_dict = {}
        String2_dict = {}
        for i in String1:
            if i in String1_dict:
                String1_dict[i] += 1
            else:
                String1_dict[i] = 1
        for i in String2:
            if i in String2_dict:
                String2_dict[i] += 1
            else:
                String2_dict[i] = 1
        return String1_dict == String2_dict