class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums) # cnt = {"num": freq, "num": freq, ...}
        items = list(cnt.items()) # items = [(num. freq), (num. freq), ...]
        items.sort(key=lambda x: x[1], reverse=True)
        return [num for num, freq in items[:k]]