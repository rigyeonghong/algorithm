#ref
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        head_list = []
        while head:
            head_list.append(head.val)
            head = head.next
        return head_list == head_list[::-1]