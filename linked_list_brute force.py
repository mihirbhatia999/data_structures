class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertNode(self, nodeName):
        if self.head is None:
            self.head = nodeName

        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                else:
                    lastNode = lastNode.next
            lastNode.next = nodeName

    def printNodes(self):
        currentNode = self.head
        if currentNode is None:
            print("linked list is empty")
        else:
            while True:
                if currentNode is None:
                    break
                else:
                    print(currentNode.data)
                currentNode = currentNode.next

                
    def search_data(self,search_element):
        c = 1 #counter 
        f=  0 #flag  0 -> no element found  1-> if element is found 
        nodeNow = self.head
        if nodeNow.data == search_element:
            print("the element you want to find is the head of the linkedlist")
            f=1

        else:
            nodeNow = nodeNow.next
            c = c + 1
            while True:
                
                if nodeNow.data == search_element:
                    print("Linked list element no.")
                    print(c)
                    f = 1
                nodeNow = nodeNow.next
                c = c + 1 

                if nodeNow is None:
                    break
        if f == 0:
            print("No such element was found in the linked list")
            
print("There is a linked list with 3 names in 3 different Nodes",end='\n')

#Linked List is  Mihir--> Anmol--> Aman
linkedList1 = LinkedList()

node1 = Node("Mihir")
linkedList1.insertNode(node1)
node2 = Node("Anmol")
linkedList1.insertNode(node2)
node3 = Node("Aman")
linkedList1.insertNode(node3)
linkedList1.printNodes()

####Creating a function that accepts an array 3 elements and puts each
####element into a linked list
