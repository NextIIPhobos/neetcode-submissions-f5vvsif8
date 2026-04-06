class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []
        

    def addNum(self, num: int) -> None:
        #print(self.small,self.large, num)
        if len(self.small) == 0:
            self.small.append(-num)
            return
        if abs(len(self.small) - len(self.large)) >= 1:
            if len(self.small)>len(self.large):
                if -num < self.small[0]:
                    heapq.heappush(self.large,num)
                else:
                    mover = heapq.heappop(self.small)
                    heapq.heappush(self.large,-mover)
                    heapq.heappush(self.small,-num)
            else:
                if num < self.large[0]:
                    heapq.heappush(self.small,-num)
                else:
                    mover = heapq.heappop(self.large)
                    heapq.heappush(self.small,-mover)
                    heapq.heappush(self.large,num)
        else:
            if -num < self.small[0]:
                    heapq.heappush(self.large,num)
            else:
                heapq.heappush(self.small,-num)
        

        

    def findMedian(self) -> float:
        #print(self.small,self.large)
        if len(self.small) == len(self.large):
            return (self.large[0]-self.small[0])/2
        elif len(self.small)>len(self.large):
            return -self.small[0]
        else:
            return self.large[0]

        

        
        