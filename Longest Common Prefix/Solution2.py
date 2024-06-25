class Solution2:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''

        strs = sorted(strs)
        
        first = strs[0]
        last = strs[-1]

        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return res
            res += first[i]

        return res