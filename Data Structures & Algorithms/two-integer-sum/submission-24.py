class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """ 
        ===== Sol 4 =====
        ===== Concept =====
        maintain a hashmap to storage seen num, can use O(1) to find pair(num, idx)
        ===== Complexity =====
        Time complexity: O(n)
        Space complexity: O(n)
        """
        seen_dict = {}
        for i, num in enumerate(nums):      
            complementary = target - num
            if complementary in seen_dict:
                return [seen_dict[complementary], i]
            seen_dict[num] = i
        return []