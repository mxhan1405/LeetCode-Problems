class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Start with a pointer at the head
        curr = head
        
        # Traverse the list until we reach the end
        while curr and curr.next:
            # If the current value is the same as the next value, skip the next node
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                # Only move the pointer forward if no duplicate was found
                curr = curr.next
                
        return head

