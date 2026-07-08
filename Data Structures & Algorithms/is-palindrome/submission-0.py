class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(i for i in s if i.isalnum()) # O(n)
        i = 0
        j = len(s) - 1
        while i<=j:
            if s[i].lower()==s[j].lower():
                i+=1
                j-=1
            else:
                return False
        return True