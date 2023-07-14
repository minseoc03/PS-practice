#queue
#FIFO

#queue using array
#enque -> O(1)
#deque -> O(n)

#queue using ring buffer
#enque -> O(1)
#deque -> O(1)

#deque (data structure ; not removing data from queue)
#double-ended queue
#can push / pop at both front and rear
#deque = queue + stack

from typing import Any

class FixedQueue:

    class Empty(Exception):
        pass
    class Full(Exception):
        pass

    def __init__(self, capacity: int) -> None:
        self.no = 0
        self.front = 0
        self.rear = 0
        self.capacity = capacity
        self.que = [None] * capacity

    def __len__(self) -> int:
        return self.no
    
    def is_empty(self) -> bool:
        return self.no <= 0
    
    def is_full(self) -> bool:
        return self.no >= self.capacity
    
    def enque(self, x: Any) -> None:
        if self.is_full():
            raise FixedQueue.Full
        self.que[self.rear] = x
        self.rear += 1
        self.no += 1
        #ring buffer
        #makes ptr resets as it rotates completely
        if self.rear == self.capacity:
            self.rear = 0

    def deque(self) -> Any:
        if self.is_empty():
            raise FixedQueue.Empty
        x = self.que[self.front]
        self.front += 1
        #reduce number of data in queue
        self.no -= 1
        #ring buffer
        if self.front == self.capacity:
            self.front = 0

        return x
    
    def peek(self) -> Any:
        if self.is_empty():
            raise FixedQueue.Empty
        #return the data where will be popped first
        return self.que[self.front]
    
    #linear search
    #O(n)
    def find(self, value: Any) -> Any:
        for i in range(self.no):
            #convert i into idx fit to ring buffer
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:
                return idx
        return -1
    
    def count(self, value: Any) -> int:
        c = 0
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:
                c += 1
        
        return c
    
    def __contains__(self, value: Any) -> bool:
        return self.count(value)
    
    def clear(self) -> None:
        self.no = self.front = self.rear = 0

    def dump(self) -> None:
        if self.is_empty():
            print('The queue is empty')
        else:
            for i in range(self.no):
                print(self.que[(i + self.front) % self.capacity], end = '')
            print()