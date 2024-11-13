class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        inserted = False

        for interval in intervals:
            if newInterval[0] < interval[0] and not inserted:
                result.append(newInterval)
                inserted = True
            result.append(interval)

        if not inserted:
            result.append(newInterval)

        merged = []

        for interval in result:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] =  max(merged[-1][1], interval[1])

        return merged