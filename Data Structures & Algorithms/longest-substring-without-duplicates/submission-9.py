class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        using set
        and two pointer for sliding window
        """
        char_set = set()
        start_ptr = 0
        end_ptr = 0
        max_len = 0
        for c in s:
            if c in char_set:
                max_len = max(max_len, end_ptr - start_ptr)
                # remove until c exit.
                while c in char_set:
                    char_set.remove(s[start_ptr])
                    start_ptr += 1
            # move sliding window
            char_set.add(c)
            end_ptr += 1
        
        max_len = max(max_len, end_ptr - start_ptr)
        return max_len

        