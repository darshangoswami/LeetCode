class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        heapq.heapify(heap)
        for n in stones:
            heapq.heappush(heap, -n)

        while len(heap) > 1:
            x = -(heapq.heappop(heap))
            y = -(heapq.heappop(heap))
            res = x - y

            if res > 0:
                heapq.heappush(heap, -res)

        return -(heap[0]) if heap else 0