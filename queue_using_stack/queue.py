class MyQueue:
    def __init__(self) -> None:
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int):
        self.stack1.append(x)

    def pop(self) -> int:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        res = self.stack2.pop()

        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return res

    def peek(self) -> int:
        return self.stack1[-1]

    def empty(self) -> bool:
        return len(self.stack1) == 0


if __name__ == "__main__":
    obj = MyQueue

    for i in range(1, 11):
        obj.push(i)

    print(obj.top())
    print(obj.empty())
