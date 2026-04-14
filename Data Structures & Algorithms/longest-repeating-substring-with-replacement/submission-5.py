class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_to_freq = defaultdict(int) # type: "char": freq in the sliding window
        set_of_appear_char = set([c for c in s])
        max_len = 0
        for appear_c in set_of_appear_char:
            target_c = appear_c # set the target for search/replace
            left = 0
            cnt_target = 0
            cnt_not_target = 0
            for right in range(len(s)):
                # put s[right] into sub_str
                if s[right] == target_c:
                    cnt_target += 1
                else:
                    cnt_not_target += 1
                # find it is invalid window, shrink from left
                if cnt_not_target > k:
                    while s[left] == target_c:
                        left += 1
                    left += 1
                    cnt_not_target -= 1
                max_len = max(max_len, right-left+1)
        return max_len

        