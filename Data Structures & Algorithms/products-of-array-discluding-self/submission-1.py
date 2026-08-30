class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # This is the naive method
        # res = []
        # for i in range(0, len(nums)):
        #     num = 1
        #     for j in range(0, len(nums)):
        #         if i == j:
        #             continue
        #         num *= nums[j]
        #     res.append(num)

        # return res

        pre = [1] * len(nums)
        post = [1] * len(nums)

        pre[0] = 1
        post[len(nums) - 1] = 1

        for i in range(1, len(nums)):
            pre[i] = nums[i - 1] * pre[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            post[i] = nums[i + 1] * post[i + 1]

        res = []

        for i in range(0, len(nums)):
            res.append(pre[i] * post[i])

        return res




                

        