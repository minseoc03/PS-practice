#hashing
#it is one of the method of searching while making inserting and deleting elements  more convinient

#hash value
#hash value is assigned as a remainder of the division of the elements by the number of elements
#ex) if there are 13 elements in the sequence, we can divide the elements by 13 and make remainder as hash value and use it as a index of new sequence

#bucket
#elements of the hash table

#hash collision
#when more than two elements have the same hash value

#chaining
#a method to resolve hash collision
#use linked list

from __future__ import annotations
from typing import Any, Sequence
import hashlib

class Node:
    def __init__(self, key: Any, value: Any, next: Node) -> None:
        self.key = key
        self.value = value
        self.next = next

class ChainedHash:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        #make a empty list for hash table
        self.table = [None] * self.capacity

    def hash_value(self, key: Any) -> int:
        if isinstance(key, int):
            return key % self.capacity
        #sha256 -> an algorithm that generates hash value for key that is not int
        #encode -> converts key into byte string so sha256 can convert key into hash value
        #hexdigest -> convert sha256 hashvalue into hex
        #int -> convert hex into int
        return(int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)
    
    #search function in hash
    #convert key into hash value
    #focus on the bucket with corresponding hash value
    #search linked list and find a key
    def search(self, key: Any) -> Any:
        hash = self.hash_value(key)
        p = self.table[hash]

        #search linked list
        while p is not None:
            if p.key == key:
                return p.value
            p = p.next
        
        return None
    
    def add(self, key: Any, value: Any) -> bool:
        hash = self.hash_value(key)
        p = self.table[hash]

        #return false if key already exist
        while p is not None:
            if p.key == key:
                return False
            p = p.next

        #add Node as a head
        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp
        return True
    
    def remove(self, key: Any) -> bool:
        hash = self.hash_value(key)
        p = self.table[hash]
        pp = None

        while p is not None:
            if p.key == key:
                #in case where desired key is at the head of the linked list
                if pp is None:
                    self.table[hash] = p.next
                else:
                    #re-assign next node of the previous node to next node of the desired node
                    pp.next = p.next
                return True
            #if desired key is not at the head, move to next node
            pp = p
            p = p.next
        return False
    
    def dump(self) -> None:
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end = '')
            while p is not None:
                print(f' -> {p.key} ({p.value})', end = '')
                p = p.next
            print()