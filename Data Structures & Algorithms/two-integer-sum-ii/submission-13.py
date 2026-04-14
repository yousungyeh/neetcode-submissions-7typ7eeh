class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = len(numbers)
        for i in range(l):
            if target - numbers[i] == numbers[i]:
                continue
            complementary_idx = self.binary_search(numbers, target-numbers[i])
            if complementary_idx != -1:
                return [i+1, complementary_idx+1]
        return -1

    def binary_search(self, array: List[int], target: int) -> int:
        if not array:
            return -1
        l = len(array)
        i = 0
        j = l - 1
        while i<=j:
            mid = (i+j)//2
            if array[mid] == target:
                return mid
            elif array[mid] > target:
                j = mid-1
            else:
                i = mid+1
        return -1
        