#ref
class Solution:
    # node는 popleft하듯 줄어들고 다 없어질 때까지!
    # prev는 None에서 시작해서 -> node.next에 prev=None=Node를 넣는데, 1부터 계속 채워짐
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        
        while node:
            # node.next를 이전 prev 리스트로 계속 연결하면서 끝날 때까지 반복
            next, node.next = node.next, prev
            prev, node = node, next

        return prev