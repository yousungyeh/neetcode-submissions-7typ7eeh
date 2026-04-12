class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """ 
        ===== Sol 4 =====
        ===== Concept =====
        maintain a hashmap to find num to idx
        ===== Complexity =====
        Time complexity: O(n)
        Space complexity: O(n)
        """
        nums_to_idx = {}
        for i, num in enumerate(nums):      
            complementary = target - num
            if complementary in nums_to_idx:
                return [nums_to_idx[complementary], i]
            nums_to_idx[num] = i
        return []