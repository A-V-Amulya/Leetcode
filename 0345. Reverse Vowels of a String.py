class Solution(object):
    def reverseVowels(Self, String):
        Array = list(String)
        Vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
        i, j = 0, len(Array) - 1
        while i < j:
            while i < j and Array[j] not in Vowels:
                j -= 1
            while i < j and Array[i] not in Vowels:
                i += 1
            Array[i], Array[j] = Array[j], Array[i]
            i += 1
            j -= 1
        return "".join(Array)   