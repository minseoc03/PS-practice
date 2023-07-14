from typing import Any

class FixedStack:

    #raising error
    #customized error is all derived from Exception class, not BaseException class
    #derived classes of BaseException class are ValueError, ZeroDivisionError etc.
    #all the other custom exception should be derived from Exception class
    class Empty(Exception):
        pass
    
    class Full(Exception):
        pass

    def __init__(self, capacity: int = 256) -> None:
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0

    def __len__(self) -> int:
        return self.ptr
    
    def is_empty(self) -> bool:
        return self.ptr <= 0
    
    def is_full(self) -> bool:
        return self.ptr >= self.capacity
    
    def push(self, value: Any) -> None:
        if self.is_full():
            raise FixedStack.Full
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self) -> Any:
        if self.is_empty():
            raise FixedStack.Empty
        self.ptr -= 1
        #but in this case, does it remove data in stack?
        #doesn't it just move the ptr?
        #resolved
        #but when I push new data, it will override the data in next ptr
        return self.stk[self.ptr]
    
    def peek(self) -> Any:
        if self.is_empty():
            raise FixedStack.Empty
        return self.stk[self.ptr - 1]
    
    def clear(self) -> None:
        self.ptr = 0

    def find(self, value: Any) -> Any:
        #for loop iterates from the top of the stack
        #because it can find a data that can be popped first
        for i in range(self.ptr - 1, -1, -1):
            if self.stk[i] == value:
                return i
        
        return -1
    
    def count(self, value: Any) -> int:
        c = 0
        for i in range(self.ptr):
            if self.stk[i] == value:
                c += 1
        
        return c
    
    def __contains__(self, value: Any) -> bool:
        return self.count(value) > 0
    
    def dump(self) -> None:
        if self.is_empty():
            print('The stack is empty')
        else:
            print(self.stk[:self.ptr])
