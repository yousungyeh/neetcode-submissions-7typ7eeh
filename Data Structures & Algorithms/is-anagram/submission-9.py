class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt_s = [0]*26
        cnt_t = [0]*26
        if len(s)!=len(t):
            return False
        for c in s:
            num = ord(c)-ord('a')
            cnt_s[num]+=1
        for c in t:
            num = ord(c)-ord('a')
            cnt_t[num]+=1
        return cnt_s == cnt_t
        