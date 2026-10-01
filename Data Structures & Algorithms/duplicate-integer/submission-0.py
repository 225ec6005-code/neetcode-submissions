class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset=set()
        for s in nums:
            if s in hashset:
                return True
            hashset.add(s)
        return False