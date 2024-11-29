# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

class Node:
    def __init__(self, data):
        self.val = data
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
