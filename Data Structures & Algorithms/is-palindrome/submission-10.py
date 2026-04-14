class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_clean = "".join([c.lower() for c in s if c.isalpha() or c.isalnum()])
        l = len(s_clean)
        half_l = l//2
        for i in range(half_l):
            if s_clean[i] != s_clean[l-i-1]:
                return False
        return True
        