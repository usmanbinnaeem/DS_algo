from collections import deque


class Stack:
    def __init__(self) -> None:
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        for i in range(len(self.q) - 1):
            self.push(self.q.popleft())
        return self.q.popleft()

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return len(self.q) == 0


if __name__ == "__main__":
    obj = Stack()
    for i in range(1, 11):
        obj.push(i)

    print(obj.top())
    print(obj.empty())

    for i in range(1, 11):
        obj.pop()

    print(obj.empty())
