class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:

            count = []
            for c in s:
                count.append(c)
            sorts = tuple(sorted(s))
            res[sorts].append(s)

        return list(res.values())