class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ords = sum(ord(c) for c in s)
        ordt = sum(ord(c) for c in t)
        return chr(ordt - ords)
