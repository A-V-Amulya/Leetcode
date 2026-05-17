class Solution(object):
    def fizzBuzz(self, n):
        Array = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                Array.append("FizzBuzz")
            elif i % 3 == 0:
                Array.append("Fizz")
            elif i % 5 == 0:
                Array.append("Buzz")
            else:
                Array.append(str(i))
        return Array