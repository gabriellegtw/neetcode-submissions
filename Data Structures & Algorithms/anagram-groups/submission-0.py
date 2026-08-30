class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        hashmap = {}

        for i in range(0, len(strs)):
            s = ''.join(sorted(strs[i]))

            if s not in hashmap:
                hashmap[s] = len(result)
                result.append([])

            result[hashmap[s]].append(strs[i])

        return result
        