class Solution:

    def encode(self, strs: List[str]) -> str:
        separators = "#" # package format: len(str) + "#" + str
        package = ""
        for s in strs:
            l = len(s)
            package += str(l) + separators + s
        return package
        # return "".join(str(len(s)) + "#" + s for s in strs) 

    def decode(self, s: str) -> List[str]:
        package_len = len(s)
        i = 0 # ptr for packed_s start position
        ans = []
        while i < package_len:
            j = i # ptr for separator "#" position
            while s[j] != "#":
                j += 1
            packed_len = int(s[i:j])
            packed_s_start = j+1
            packed_s_end = j+1+packed_len
            packed_s = s[packed_s_start:packed_s_end]
            ans.append(packed_s)
            i = packed_s_end
        return ans

            