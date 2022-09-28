# https://leetcode.com/problems/design-circular-queue/

class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0 for _ in range(k)]
        self.size = k
        self.count = 0
        self.head_idx = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.queue[(self.head_idx + self.count) % self.size] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.head_idx = (self.head_idx + 1) % self.size
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self.queue[self.head_idx]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        return self.queue[(self.head_idx + self.count - 1) % self.size]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.size

    def __repr__(self) -> str:
        repr = ""
        repr += f"Queue: {self.queue}, Size: {self.size}, "
        repr += f"Current Count: {self.count}, Current Head: {self.head_idx}"
        return repr

def main():
    print("Create Object")
    q = MyCircularQueue(3)
    print(f"Default queue: {q}")

    status = q.enQueue(1)
    print(f"Enque status: {status}")
    print (f"Queue after enque: {q}")

    status = q.enQueue(2)
    print(f"Enque status: {status}")
    print (f"Queue after enque: {q}")

    status = q.enQueue(3)
    print(f"Enque status: {status}")
    print (f"Queue after enque: {q}")

    status = q.enQueue(4)
    print(f"Enque status: {status}")
    print (f"Queue after enque: {q}")

    rear = q.Rear()
    print(f"Rear element of queue: {rear}")

    print(f"Is queue full: {q.isFull()}")

    status = q.deQueue()
    print(f"Deque status: {status}")
    print (f"Queue after deque: {q}")

    status = q.enQueue(4)
    print(f"Enque status: {status}")
    print (f"Queue after enque: {q}")

    rear = q.Rear()
    print(f"Rear element of queue: {rear}")


if __name__ == "__main__":
    main()