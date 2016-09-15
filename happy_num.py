class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        tried = set()
        tried.add(n)
        digits = n
        sum = n
        while not sum == 1:
            sum = 0
            for d in str(digits):
                sum += int(d) ** 2
            if sum in tried:
                return False
            tried.add(sum)
            digits = sum
        return True
