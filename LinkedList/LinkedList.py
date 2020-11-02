class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def append(head, data):
    if head is None:
        head = LinkedList(data)
    else:
        temp = head
        new_node = LinkedList(data)
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

def insert_beg(head, data):
    if head is None:
        head = LinkedList(data)
    else:
        new_node = LinkedList(data)
        new_node.next = head
    return new_node

def insert_after(head, prev_node, data):
    if head is None or prev_node is None:
        print("previous node cant be none")
        return
    else:
        temp = head
        while temp is not None and temp.value != prev_node:
            temp = temp.next
        new_node = LinkedList(data)
        new_node.next = temp.next
        temp.next = new_node

def delete(head, data):
    if head is None:
        print("list is empty")
        return
    elif head.value == data:
        temp = head.next
        head = temp
        return head

    else:
        temp = head
        prev_node = None
        while temp is not None and temp.value != data:
            prev_node = temp
            temp = temp.next
        if temp is None:
            print("value does not exist")
            return
        prev_node.next = temp.next
        temp.next = None
        return head

def insert_mid(head, data):
    if head is None:
        print( "list is empty")
        return
    else:
        length = 0
        temp = head
        while temp is not None:
            length+=1
            temp = temp.next
        new_node = LinkedList(data)
        spare = head
        prev_node = None
        for i in range((length+1)//2):
            prev_node = spare
            spare = spare.next
        prev_node.next = new_node
        new_node.next = spare

def index_of(head, data):
    if head is None:
        print('list is empty')
        return
    elif head.value == data:
        print(0)
    else:
        index = 0
        temp = head
        while temp is not None and temp.value!= data:
            index+= 1
            temp = temp.next
        if temp is None:
            print("element not in list")
            return
        else:
            print(index)


def reverse(head):
    current = head
    prev = None
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    head = prev
    return head

def print_list(head):
    if head is None:
        return
    temp = head
    while temp is not None:
        if temp.next is None:
            print(temp.value, end='.')
        else:
            print(temp.value,end=' -> ')
        temp = temp.next



head = LinkedList(10)
head.next = LinkedList(8)
head = insert_beg(head, 12)
append(head, 6)
append(head, 4)
append(head, 2)
insert_mid(head, 100)
insert_after(head, 10, 22)
head = delete(head, 12)
print_list(head)
print()
index_of(head, 4)
head = reverse(head)
print_list(head)
print()
index_of(head, 4)
