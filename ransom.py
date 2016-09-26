class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomeNote = list(ransomNote)
        magazine = list(magazine)
        for l in ransomeNote:
            if l in magazine:
                magazine.remove(l)
            else:
                return False
        return True
