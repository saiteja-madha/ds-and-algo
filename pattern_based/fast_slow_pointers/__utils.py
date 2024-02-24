# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_linked_list(lst):
    head = ListNode(lst[0])
    cur = head
    for i in range(1, len(lst)):
        cur.next = ListNode(lst[i])
        cur = cur.next
    return head


def linked_list_to_list(head):
    lst = []
    while head is not None:
        lst.append(head.val)
        head = head.next
    return lst
