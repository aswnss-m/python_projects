class Node:     #This class contains the property of the node
    
    def __init__(self,val=None):    #* This only stores one value
        self.val = val
        self.nextval = None         #! This is the link part

class linked_list:      #This class contains the property of the list , the start of the list
    def __init__(self):
        self.head = None

    def listprint(self):    #? Traversing the linked list in the forward direction
        printval = self.head

        while printval is not None:
            print(printval.val)
            printval = printval.nextval

list1 = linked_list()
list1.head = Node("First Element")
e2 = Node("Second Element")
e3 = Node("Third Element")

list1.head.nextval = e2
e2.nextval = e3

list1.listprint()