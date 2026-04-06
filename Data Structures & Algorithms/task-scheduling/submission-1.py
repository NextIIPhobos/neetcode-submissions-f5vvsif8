class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        heap = [-c for c in counts.values()]
        heapq.heapify(heap)

        time = 0

        deq = deque()
        
        while heap or deq:
            time+=1
            if heap:
                cnt = heapq.heappop(heap) + 1
                if cnt:
                    deq.append((cnt,time+n))
            if deq and deq[0][1] == time:
                cnt = deq.popleft()[0]
                heapq.heappush(heap, cnt)
        
        return time


