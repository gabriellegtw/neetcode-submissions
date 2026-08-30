class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for i in range(0, len(nums)):
            if (nums[i] not in hashmap.keys()):
                hashmap[nums[i]] = 1
            else:
                hashmap[nums[i]] += 1

        for key, value in hashmap.items():
            if value > 1:
                return True

        return False

         