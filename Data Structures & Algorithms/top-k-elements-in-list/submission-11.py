class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums) # cnt = {"num": freq, "num": freq, ...}
        f = []
        for i in range(len(nums)+1):
            f.append([])
        for num, freq in cnt.items():
            f[freq].append(num)

        ans = []
        for i in range(len(f)-1, 0, -1):
            for num in f[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans

