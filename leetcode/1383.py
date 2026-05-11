class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:

        performance = sorted(zip(efficiency, speed), reverse=True)
        heap, sSum, p = [], 0, 0

        for e, s in performance:
            if len(heap) > k-1:
                sSum -= heappop(heap)

            heappush(heap, s)

            sSum += s
            p = max(p, sSum*e)

        return p % (1000000007)
