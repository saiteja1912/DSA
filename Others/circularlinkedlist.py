class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        curr=self.head
        while curr:
            print(curr.data,end=' ')
            curr=curr.next
            if curr==self.head:
                break
        print()

    def append(self, data):
        new_node=Node(data)
        #2 cases: CLL is empty or not
        if not self.head:
            self.head=new_node
            self.head.next=self.head
            return
        last_node=self.head
        while last_node.next!=self.head:
            last_node=last_node.next
        last_node.next=new_node
        new_node.next=self.head
    
    def prepend(self, data):
        #Solution 1
        new_node = Node(data)
        cur = self.head
        new_node.next = self.head
        if not self.head:
            new_node.next = new_node
        else:
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
        self.head = new_node
        
        # # Solution 2
        # new_node=Node(data)
        # # 2 cases: CLL is empty or not
        # if not self.head:
        #     self.head=new_node
        #     self.head.next=self.head
        #     return
        # last_node=self.head
        # while last_node.next!=self.head:
        #     last_node=last_node.next
        # last_node.next=new_node
        # new_node.next=self.head
        # #below line is the only extra line
        # self.head=new_node
    def __len__(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
            if cur == self.head:
                break
        return count

    def remove(self, key):
        #Assumption: The occurrences of nodes will be unique(remove only 1st occ)
        if self.head:
            if self.head.data == key:
                cur = self.head
                while cur.next != self.head:
                    cur = cur.next
                if self.head == self.head.next:
                    self.head = None
                else:
                    cur.next = self.head.next
                    self.head = self.head.next
            else:
                cur = self.head
                prev = None
                while cur.next != self.head:
                    prev = cur
                    cur = cur.next
                    if cur.data == key:
                        prev.next = cur.next
                        cur = cur.next

    def split_list(self):
        size = len(self)
        if size == 0:
            return None
        if size == 1:
            return self.head
        mid = size//2
        count = 0
        prev = None
        cur = self.head
        while cur and count < mid:
            count += 1
            prev = cur
            cur = cur.next
        prev.next = self.head
        split_cllist = CircularLinkedList()
        while cur.next != self.head:
            split_cllist.append(cur.data)
            cur = cur.next
        split_cllist.append(cur.data)
        self.print_list()
        print("\n")
        split_cllist.print_list()

    def is_circular_linked_list(self, input_list):
        cur = input_list.head
        while cur.next:
            cur = cur.next
            if cur.next == input_list.head:
                return True
        return False

cll=CircularLinkedList()
# cll.append(1)
# cll.append(2)
cll.prepend('A')
cll.prepend('B')
cll.append('C')
cll.prepend('D')
cll.remove('A')
cll.print_list()
cll.split_list()
cll.print_list()
cll_test=CircularLinkedList()
cll_test.print_list()
print(cll.is_circular_linked_list(cll_test))