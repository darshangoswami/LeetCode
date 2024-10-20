class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)

        for word in strs:
            key = str(sorted(word))
            hm[key].append(word)

        return list(hm.values())