class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        r = lambda x2,y2: (x2)**2 + (y2)**2

        heap = [(-r(point[0],point[1]),point) for point in points]     
        heapq.heapify(heap)
        while len(heap) > k:
            heapq.heappop(heap)
        

        return [h[1] for h in heap]
