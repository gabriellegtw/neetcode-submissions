class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return []

        hashmap = {}
        result = []
        for i in range(0, len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = 1
            else:
                hashmap[nums[i]] += 1

        hashmap = list(sorted(hashmap.items(), key=lambda item: item[1]))

        if len(hashmap) <= k:
            ref = hashmap[0][1]
        else:
            ref = hashmap[len(hashmap) - k][1]

        hashmap = dict(hashmap)

        for key, value in hashmap.items():
            if value >= ref and key not in result:
                result.append(key)

        return result

        