class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class LinkedList:
    def __init__(self):
        self.head=None
    
    def print_list(self):
        curNode=self.head
        while curNode:
            print(f'{curNode.data}',end=' ')
            curNode=curNode.next
        print()
    
    def append(self,data):
        #2 cases -> LL empty, LL non-empty
        newNode=Node(data)
        if self.head is None:
            self.head=newNode
            return
        lastNode=self.head
        while lastNode.next:
            lastNode=lastNode.next
        lastNode.next=newNode
    
    def prepend(self,data):
        newNode=Node(data)
        newNode.next=self.head
        self.head=newNode
        
        # curNode=self.head
        # not required
        # if curNode is None:
        #     self.head=newNode
        #     return

    def insert_after_node(self,prev_node,data):
        if prev_node is None:
            print('prev node does not exist.')
            return
        newNode=Node(data)
        newNode.next=prev_node.next
        prev_node.next=newNode
            
    def delete_node_by_val(self,key):
        cur_node=self.head
        #2 cases: Node to be deleted is head, not head
        if cur_node and cur_node.data == key:
            self.head=self.head.next
            cur_node=None
            return
        
        prev=None
        while cur_node and cur_node.data != key:
            prev=cur_node
            cur_node=cur_node.next    
        if cur_node is None:
            print(f'ele to delete not found in LL')
            return
        prev.next=cur_node.next
        cur_node=None
        
    def delete_node_at_pos(self, pos):
        #2 cases: Node to be deleted is head, not head
        if self.head:
            cur_node=self.head
            if pos==0:
                self.head=cur_node.next
                cur_node=None
                return
            
            prev=None
            count=0
            while cur_node and count!=pos:
                prev=cur_node
                cur_node=cur_node.next
                count+=1
            if cur_node is None:
                print(f'position provided is greater than length of LL')
                return
            prev.next=cur_node.next
            cur_node=None
    
    def len_iterative(self):
        count = 0
        cur_node = self.head
        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count
    
    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)
    
    def swap_nodes(self, key1, key2):
        if key1 == key2:
            return
        
        prev1=None
        curr1=self.head
        while curr1 and curr1.data!=key1:
            prev1=curr1
            curr1=curr1.next
        
        prev2=None
        curr2=self.head
        while curr2 and curr2.data!=key2:
            prev2=curr2
            curr2=curr2.next
            
        if not curr1 or not curr2:
            return
        
        if prev1:
            prev1.next=curr2
        else:
            self.head=curr2
        
        if prev2:
            prev2.next=curr1
        else:
            self.head=prev1
            
        curr1.next,curr2.next=curr2.next,curr1.next
        
    def reverse_iterative(self):
        prev=None
        curr=self.head
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        self.head=prev
        
    def reverse_recursive(self):
        def _reverse_recursive(curr, prev):
            if not curr:
                return prev
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
            return _reverse_recursive(curr,prev)
        
        self.head=_reverse_recursive(curr=self.head,prev=None)
        
    def merge_sorted(self, llist):
        p=self.head
        q=llist.head
        s=None
        #If current LL is empty, return other LL
        if not p:
            return q
        if not q:
            return p
        if p and q:
            if p.data<=q.data:
                s=p
                p=s.next
            else:
                s=q
                q=s.next
            new_head=s    
        while p and q:
            if p.data<=q.data:
                s.next=p
                s=p
                p=s.next
            else:
                s.next=q
                s=q
                q=s.next
        if not p:
            s.next=q
        if not q:
            s.next=p
        return new_head
    
    def remove_duplicates(self):
        dup_values=dict()
        prev=None
        curr=self.head
        while curr:
            if curr.data in dup_values:
                prev.next=curr.next
                curr=None
            else:
                dup_values[curr.data]=1
                prev=curr
            curr=prev.next
            
    def print_nth_from_last(self, n, method):
        if method == 1:
            #Method 1:
            total_len = self.len_iterative()
            cur = self.head
            while cur:
                if total_len == n:
                    #print(cur.data)
                    return cur.data
                total_len -= 1
                cur = cur.next
            if cur is None:
                return
        elif method == 2:
            # Method 2:
            p = self.head
            q = self.head
            count = 0
            while q:
                count += 1
                if(count>=n):
                    break
                q = q.next
            if not q:
                print(str(n) + " is greater than the number of nodes in list.")
                return
            while p and q.next:
                p = p.next
                q = q.next
            return p.data
        
    def count_occurences_iterative(self, data):
        count = 0
        cur = self.head
        while cur:
            if cur.data == data:
                count += 1
            cur = cur.next
        return count
    
    def count_occurences_recursive(self, node, data):
        if not node:
            return 0
        if node.data == data:
            return 1 + self.count_occurences_recursive(node.next, data)
        else:
            return self.count_occurences_recursive(node.next, data)
    
    def rotate(self, k):
        #Constraints: k>0
        #perform right shift k times
        if self.head and self.head.next:
            p = self.head
            q = self.head
            prev = None
            count = 0
            while p and count < k:
                prev = p
                p = p.next
                q = q.next
                count += 1
            p = prev
            while q:
                prev = q
                q = q.next
            q = prev
            
            q.next = self.head
            self.head = p.next
            p.next = None

    def is_palindrome_1(self):
        # Solution 1:
        s = ""
        p = self.head
        while p:
            s += p.data
            p = p.next
        return s == s[::-1]
    def is_palindrome_2(self):
        # Solution 2:
        p = self.head
        s = []
        while p:
            s.append(p.data)
            p = p.next
        p = self.head
        while p:
            data = s.pop()
            if p.data != data:
                return False
            p = p.next
        return True
    def is_palindrome_3(self):
        if self.head:
            p = self.head
            q = self.head
            prev = []
            i=0
            while q:
                prev.append(q)
                q = q.next
                i += 1
            
            count = 1
            while count <= i//2 + 1:
                if prev[-count].data != p.data:
                    return False
                p = p.next
                count += 1
            return True
        else:
            return True
    def is_palindrome(self,method):
        if method == 1:
            return self.is_palindrome_1()
        elif method == 2:
            return self.is_palindrome_2()
        elif method == 3:
            return self.is_palindrome_3()
    
    def move_tail_to_head(self):
        if self.head and self.head.next:
            last = self.head
            second_to_last = None
            while last.next:
                second_to_last = last
                last = last.next
            last.next = self.head
            second_to_last.next = None
            self.head = last
            
    def sum_two_lists(self, llist):
        p = self.head
        q = llist.head
        sum_llist = LinkedList()
        carry = 0
        while p or q:
            if not p:
                i =0
            else:
                i = p.data
            if not q:
                j =0
            else:
                j = q.data
            s = i + j + carry
            if s >= 10:
                carry = 1
                remainder = s % 10
                sum_llist.append(remainder)
            else:
                carry = 0
                sum_llist.append(s)
            if p:
                p = p.next
            if q:
                q = q.next
        sum_llist.print_list()

    def is_circular_linked_list(self, input_list):
        cur = input_list.head
        while cur.next:
            cur = cur.next
            if cur.next == input_list.head:
                return True
        return False
    
llist_1=LinkedList()
print('one')
llist_1.print_list()
llist_1.append(1)
print('two')
llist_1.print_list()
llist_1.prepend(2)
print('three')
llist_1.print_list()
llist_1.insert_after_node(llist_1.head.next,3)
print('four')
llist_1.print_list()
llist_1.delete_node_by_val(3)
print('five')
llist_1.print_list()
print('six')
llist_1.delete_node_at_pos(0)
llist_1.print_list()
print(llist_1.len_iterative())
print(llist_1.len_recursive(llist_1.head))
print('seven')
llist_1.append(9)
llist_1.append(7)
llist_1.append(5)
llist_1.append(10)
print('before swap')
llist_1.print_list()
llist_1.swap_nodes(9,5)
print('after swap')
llist_1.print_list()
llist_1.reverse_recursive()
llist_1.print_list()
llist_1.reverse_recursive()
llist_1.print_list()

llist_2=LinkedList()
llist_2.append(2)
llist_2.append(3)
llist_2.append(4)
llist_2.append(6)
llist_2.append(8)
llist_1.merge_sorted(llist_2)
llist_1.print_list()
print("Linked List Before Removing Duplicates")
llist_1.append(2)
llist_1.append(3)
llist_1.print_list()
print("Linked List After Removing Duplicates")
llist_1.remove_duplicates()
llist_1.print_list()
print(llist_1.print_nth_from_last(4,1))
print(llist_1.print_nth_from_last(4,2))
print(llist_1.count_occurences_iterative(1))
print(llist_1.count_occurences_recursive(llist_1.head, 1))

llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
llist.append(5)
llist.append(6)
llist.rotate(4)
llist.print_list()

llist_2 = LinkedList()
llist_2.append("A")
llist_2.append("B")
llist_2.append("A")
print(llist_2.is_palindrome(1))
print(llist_2.is_palindrome(2))
print(llist_2.is_palindrome(3))
llist_2.print_list()
llist_2.move_tail_to_head()
llist_2.print_list()
print(f'cll: {llist_2.is_circular_linked_list(llist_2)}')


# 3 6 5
#   4 2 
# ------
#
llist1 = LinkedList()
llist1.append(5)
llist1.append(6)
llist1.append(3)
llist2 = LinkedList()
llist2.append(2)
llist2.append(4)
print(365 + 42)
llist1.sum_two_lists(llist2)