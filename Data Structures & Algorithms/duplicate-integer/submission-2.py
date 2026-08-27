class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashs = set()
        for i in nums :
            if i in hashs :
                return True
            else :
                hashs.add(i)
        return False

        