import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = re.sub(r'[^a-zA-Z0-9]','' ,s).lower()
        i = 0
        j = len(cleaned) - 1
        while i<j:
            if cleaned[i] != cleaned[j]:
                return False
            i+=1
            j-=1
        return True