class node:
    def __init__(self, data, next):
        self.data = data
        self.nextNode = next

def printList(myList, rootPointer):
    loopPointer = rootPointer

    while loopPointer != -1: #while not end of linked list
        print(myList[loopPointer])
        loopPointer = myList[loopPointer].next

def addnode_at_end(myList, rootPointer, newNode):
    global freePointer
    if freePointer != -1:
        newFreePointer = myList[freePointer].nextNode #new free pointer will be what our current free pointer was pointing at
        myList[freePointer] = newNode #store our new node at free pointer, with a nextNode = -1 because its at the end
        
        loopPointer = rootPointer #create a temp pointer "loopPointer"
        while loopPointer != -1: #Search to grab the index of the current last element
            currentNodeIndex = loopPointer
            loopPointer = myList[loopPointer].next
        
        myList[currentNodeIndex].nextNode = freePointer #last element's next pointer will now point to our new node at free pointer, instead of -1
        freePointer = newFreePointer #update free pointer
    else:
        print("List is full, no free spaces left")

def deleteNode(myList, rootPointer, delItem, freePointer):
    searchPointer = rootPointer #create a temp search pointer starts at the root

    while (currentPointer != -1) and (myList[currentPointer].data != delItem): #search for the item
        currentPointer = searchPointer #keep track of the index of the current node ("searchPointer") before updating it
        searchPointer = myList[searchPointer].nextNode 
        #search pointer will either end up as -1 so no item, or will actually end up pointing at the index of the node we're searching for to delete
    
    if searchPointer == -1:
        print("Item not found")
    else:
        myList[currentPointer].nextNode = myList[searchPointer].nextNode #let the node before our to-be-deleted node, point to the node linked to our to-be-deleted node
        myList[searchPointer].data = None #Delete the contents of our desired to-be-deleted node

        #linking the deleted node to the end of the free nodes
        freeSearch = freePointer #create temp pointer
        while freeSearch != -1: #loop until end of free nodes is found
            currentFree = freeSearch #keep track of index of free node we're looking through
            freeSearch = myList[freeSearch].nextNode
        
        myList[currentFree].nextNode = searchPointer #we link our node at the last space of the free list, to point to the deleted node
        myList[searchPointer].nextNode = -1 #let the deleted node now point to -1, because its the last element of the free list





#-----------------------------------------#
#-----------sample linked list------------#
i0 = node(13, 1)
i1 = node(15, 4)
i2 = node(21, 7)
i3 = node(29, -1)
i4 = node(17, 2)
i5 = node(0, 6)
i6 = node(0, 8)
i7 = node(23, 3)
i8 = node(0, 9)
i9 = node(0, -1)

list = [i0, i1, i2, i3, i4, i5, i6, i7, i8, i9]
rootPointer = 0
freePointer = 5
