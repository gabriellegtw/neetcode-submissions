import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        result = 0

        k = len(nums) - k

        while k >= 0:
            result = heapq.heappop(nums)
            k -= 1

        return result
        