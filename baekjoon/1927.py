# 연산 개수
# 0이면 가장 작은 값 출력 / 배열에서 제거
# 아니면 추가 

import sys
import heapq


class PriorityQueue:
    def __init__(self):
        self.data = []

    def push(self, value):
        heapq.heappush(self.data, value)

    def pop(self):
        if len(self.data) == 0:
            return 0
        elif len(self.data) > 0:
            tmp = self.data[0]
            heapq.heappop(self.data)
            return tmp
            


def main():
    myPQ = PriorityQueue()

    n = int(sys.stdin.readline())
    for _ in range(n):
        x = [int(v) for v in sys.stdin.readline().split()]
        if x[0] == 0:
            print(myPQ.pop()) # 가장작은 값 출력하고 배열에서 제거
        else: 
            #배열에 추가
            myPQ.push(x[0])
    
if __name__ == "__main__":
    main()