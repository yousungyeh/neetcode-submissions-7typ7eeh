class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        items = sorted(cnt.items(), key=lambda x: x[1], reverse=True)
        return [num for num, freq in items[:k]]