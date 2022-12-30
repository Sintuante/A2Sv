class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        max = 3**19
        return n>0 and max % n== 0
