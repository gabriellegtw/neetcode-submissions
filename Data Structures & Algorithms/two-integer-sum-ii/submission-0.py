class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        results = []

        while l < r:
            sum1 = numbers[l] + numbers[r]
            if sum1 == target:
                results.append(l + 1)
                results.append(r + 1)
                return results

            if sum1 < target:
                l += 1

            if sum1 > target:
                r -= 1
        