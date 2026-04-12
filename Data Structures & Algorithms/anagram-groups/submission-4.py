class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        order_save = defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s))
            order_save[sorted_s].append(s)
        print(order_save.values())
        return list(order_save.values())
        