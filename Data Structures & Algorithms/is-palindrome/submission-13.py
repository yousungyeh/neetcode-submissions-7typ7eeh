class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Two pointer
        """
        l = len(s)
        first_ptr = 0
        second_ptr = l-1
        while first_ptr < second_ptr:
            while first_ptr < second_ptr and not s[first_ptr].isalnum():
                first_ptr += 1
            while first_ptr < second_ptr and not s[second_ptr].isalnum():
                second_ptr -= 1
            if s[first_ptr].lower() != s[second_ptr].lower():
                return False
            first_ptr += 1
            second_ptr -= 1
        return True
        