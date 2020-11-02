class LinkedList:
    def __init__(self, data):
        self.value  = data
        self.next = None

    def append(self, head, data):
            if head is None:
                head = LinkedList(data)
            temp = head
            while temp.next is not None:
                temp = temp.next
            new_node = LinkedList(data)
            new_node.next = None
            temp.next = new_node

    def merge(self, head1, head2):
        fake = LinkedList(-1)
        last = fake
        while head1 is not None and head2 is not None:
            if head1.value < head2.value:
                last.next = head1
                last = head1
                head1 = head1.next
            else:
                last.next = head2
                last = head2
                head2 = head2.next
        if head1 is None:
            last.next = head2
        if head2 is  None:
            last.next = head1
        return fake.next


    def print_list(self, head):
        if head is None:
            return
        temp = head
        while temp is not None:
            print(temp.value, end=' ')
            temp = temp.next


head1 = LinkedList(6)
head1.append(head1, 8)
head1.append(head1, 10)
head2 = LinkedList(1)
head2.append(head2, 7)
head2.append(head2, 9)
head2.append(head2, 11)
head2.append(head2, 13)
ref = head2.merge(head1, head2)
head1.print_list(ref)