class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = {} # {"char": freq}
        cnt = Counter(s1)
        len_s1 = len(s1)
        left = 0
        for right in range(len(s2)):
            freq[s2[right]] = freq.get(s2[right], 0) + 1
            len_window = right - left + 1
            if len_window == len_s1:
                # check the char in window, whether match cnt or not
                if cnt == freq:
                    return True
                # move window, and pop the char out
                freq[s2[left]] -= 1
                if freq[s2[left]] == 0: # remove key
                    del freq[s2[left]]
                left += 1
        return False