class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None

    def getMiddle(self):
        self.fast = self.head
        self.slow = self.head

        while(self.fast != None and self.fast.next != None):
            self.slow = self.slow.next
            self.fast = self.next.next

        return self.slow.data


if __name__ == '__main__':
    pass
