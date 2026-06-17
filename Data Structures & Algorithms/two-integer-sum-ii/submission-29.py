class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp = {}
        for i, num in enumerate(numbers):
            tmp = target - num
            if tmp in mp:
                return [mp[tmp], i + 1]
            mp[num] = i + 1
        return []