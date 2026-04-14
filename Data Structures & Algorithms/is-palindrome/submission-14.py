class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Two pointer (Non built-in func.)
        """
        l = len(s)
        first_ptr = 0
        second_ptr = l-1
        while first_ptr < second_ptr:
            while first_ptr < second_ptr and not self.alphaNum(s[first_ptr]):
                first_ptr += 1
            while first_ptr < second_ptr and not self.alphaNum(s[second_ptr]):
                second_ptr -= 1
            if s[first_ptr].lower() != s[second_ptr].lower():
                return False
            first_ptr += 1
            second_ptr -= 1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
        