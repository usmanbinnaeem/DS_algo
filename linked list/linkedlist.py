class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None

    def addNode(self, x):
        newNode = Node(x)
        if (self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def printLList(self):
        current = self.head
        print('[ ', end=' ')
        while(current):
            print(str(current.data) + ', ', end=' ')
            current = current.next
        print('] ', end=' ')

    def countNodes(self):
        count = 0
        while(self.head):
            count += 1
            self.head = self.head.next
        print('No of nodes = ', count)

    def getMiddle(self):
        fast = self.head
        slow = self.head

        while(fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next

        return slow.data


if __name__ == '__main__':
    linkl = SLinkedList()
    linkl.addNode(5)
    linkl.addNode(4)
    linkl.addNode(3)
    linkl.addNode(2)
    linkl.addNode(1)
    linkl.printLList()
    linkl.countNodes()
    # print(linkl.getMiddle())
