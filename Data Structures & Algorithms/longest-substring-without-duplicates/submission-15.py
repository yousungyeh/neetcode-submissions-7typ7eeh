class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        using set and two pointer for sliding window
        BUT add jump! memory the last seen_idx for each characters
        """
        map_last_seen_idx = {} # "char": last_seen_idx
        start_ptr = 0 # sub_str start pointer
        max_len = 0
        for i in range(len(s)):
            if s[i] in map_last_seen_idx:
                # jump start_ptr to 
                start_ptr = max(map_last_seen_idx[s[i]]+1, start_ptr)
            map_last_seen_idx[s[i]] = i
            max_len = max(max_len, i-start_ptr+1)
        return max_len

        