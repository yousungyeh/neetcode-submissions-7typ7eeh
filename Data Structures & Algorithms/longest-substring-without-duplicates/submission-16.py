class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        using set and two pointer for sliding window
        once we meet the repeated char, we need to remove all char before that index.
        BUT add jump! memory the last seen_idx for each characters, so we can jump through seen_idx+1
        """
        map_last_seen_idx = {} # "char": last_seen_idx
        start_ptr = 0 # sub_str start pointer
        max_len = 0
        for i in range(len(s)):
            if s[i] in map_last_seen_idx:
                # jump start_ptr to, that is, we need to start substr at least from last_seen_idx["c"]+1
                # that is, if last_seen_idx is inside the sub_str, we need to remove that char, 
                # while if last_seen_idx is not in the sub_str(already jump through it), we dont update.
                start_ptr = max(map_last_seen_idx[s[i]]+1, start_ptr)
            map_last_seen_idx[s[i]] = i
            max_len = max(max_len, i-start_ptr+1)
        return max_len

        