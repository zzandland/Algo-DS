# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        output = before = after_node = None
        node = head
        complete = False
        
        while complete is False:
            if self.check_remainder_len(node, k) is True:
                after_node = self.traverse_k_nodes(node, k)
                after = self.reverse_interval(node, k)
                if before is not None:
                    before[1].next = after[0]
                before = after    
                if output is None:
                    output = before[0]
                node = after_node    
            else:     
                if before is None:
                    return node
                before[1].next = node
                complete = True    
        return output         
      
      
    def check_remainder_len(self, node: ListNode, k: int) -> bool:
        while k > 0:
            if node is None:
                return False
            node = node.next
            k -= 1  
        return True
      
    
    def traverse_k_nodes(self, node: ListNode, k: int) -> ListNode:
        while k > 0:
            node = node.next
            k -= 1
        return node
      

    def reverse_interval(self, node: ListNode, k: int) -> List[ListNode]:
        tail = curr = node
        runner = curr.next
        prev = None
        while k > 0:
            curr.next = prev
            prev = curr
            curr = runner
            if curr is not None:
                runner = curr.next
            k -= 1    
        return [prev, tail]