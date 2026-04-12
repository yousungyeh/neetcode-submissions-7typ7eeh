class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        l = list(cnt.items())
        l.sort(key=lambda x: x[1], reverse=True)
        return [l[i][0] for i in range(k)]
        