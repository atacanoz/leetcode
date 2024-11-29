# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def insertAtEnd(self, new_data):
        new_node = Node(new_data)
        if self.head == None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end = " ")
            temp = temp.next
        print()

    def deleteFromBeginning(self):
        if self.head is None:
            return "The list is empty"
        self.head = self.head.next

    def ReverseList(self):
        node = None

        while self.head:
               temp = self.head.next
               self.head.next = node
               node = self.head
               self.head = temp
        return self.head




list = LinkedList()
list.insertAtBeginning(5)
list.insertAtBeginning(4)
list.insertAtBeginning(3)
list.insertAtBeginning(2)
list.insertAtBeginning(1)

list.printList()

list.ReverseList()

list.printList()
