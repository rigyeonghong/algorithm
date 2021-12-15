class PriorityQueue:
    '''
    우선순위 큐를 힙으로 구현합니다
    '''
    
    # 왼쪽에는 현재 인덱스에 x2 오른쪽 x2 +1

    def __init__(self) :
        self.data = [0]

    def push(self, value) :
        '''
        우선순위 큐에 value를 삽입합니다.
        '''
        # 맨마지막에 값 추가
        self.data.append(value)
        # value 와 root 바꿔치기 위해 현재 마지막 번호 몇번인지 가져와
        index = len(self.data) -1
             
        # 마지막으로 삽입한 값이 root 노드가 되면 종료
        while index != 1:
            #  자신의 부모가 자신보다 크다면 : 이렇게 접근 가능한게 완전이진트리의 특성
            if self.data[index//2] > self.data[index] :
                temp = self.data[index]
                self.data[index] = self.data[index//2]
                self.data[index//2] = temp
                
                index = index // 2
            else:
                # 반복문 탈출
                break
        
    def pop(self) :
        '''
        우선순위가 가장 높은 원소를 제거합니다.
        '''
        if len(self.data) == 1:
            return
        # root노드와 마지막노드 바꿔치기 후 data에서 pop해서 버리도록
        # [1,2,3,4] -> [4,2,3]
        self.data[1] = self.data[-1]
        self.data.pop()
        
        index = 1
        
        # 깊이가 얼마인지 모르니까 무한 반복문
        while True:
            # priority : 왼쪽으로 갈지 오른쪽으로 갈지 결정해줌
            priority = -1 
            #1. 아무 자식 없는 경우
            if len(self.data) - 1 < index * 2 :
                break
            #2. 왼쪽 자식만 있는 경우
            elif len(self.data) -1 < index * 2 + 1 :
                priority = index * 2
            #3. 왼쪽 오른쪽 모두 자식 있는 경우
            else : 
                if self.data[index*2] < self.data[index*2 + 1] :
                    #priority를 왼쪽으로 옮겨줘
                    priority = index * 2
                else:
                    priority = index * 2 + 1
                    
            # 제거된 자료를 채우기위해 root 노드로 옮겨진 자료가 priority보다 크다면 자리 바꿔줘
            if self.data[index] > self.data[priority] :
                temp = self.data[index]
                self.data[index] = self.data[priority]
                self.data[priority] = temp
                
                index = priority
            else:
                break

    def top(self) :
        '''
        우선순위가 가장 높은 원소를 반환합니다. 만약 우선순위 큐가 비어있다면 -1을 반환합니다.
        '''

        if len(self.data) == 1:
            return -1
        else :
            return self.data[1]
            