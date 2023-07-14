#open hashing
#in case of hash collision, instead of making linked list
#it re-hashes and find another spot

#rehashing
#method can be anything
#in this case, we added 1 into hash value

from __future__ import annotations
from typing import Any, Type
from enum import Enum
import hashlib

class Status(Enum):
    OCCUPIED = 0
    EMPTY = 1
    DELETED = 2

class Bucket:
    #constructor for Bucket class
    def __init__(self, key: Any = None, value: Any = None,
                 stat: Status = Status.EMPTY) -> None:
        self.key = key
        self.value = value
        self.stat = stat

    #using for changing field of the Bucket class
    def set(self, key: Any, value: Any, stat: Status) -> None:
        self.key = key
        self.value = value
        self.stat = stat

    #using for changing status of the bucket
    def set_status(self, stat: Status) -> None:
        self.stat = stat

class OpenHash:
    #make an empty hash table
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.table = [Bucket()] * self.capacity

    #convert key into hash value
    def hash_value(self, key: Any) -> int:
        if isinstance(key, int):
            return key % self.capacity
        return (int(hashlib.md5(str(key).encode()).hexdigest(), 16)
                % self.capacity)
    
    #rehash the value in case of collision
    def rehash_value(self, key: Any) -> int:
        return (self.hash_value(key) + 1) % self.capacity
    
    #search for corresponding cnode
    def search_node(self, key: Any) -> Any:
        hash = self.hash_value(key)
        p = self.table[hash]

        for i in range(self.capacity):
            #if corresponding node is empty than there's no data
            if p.stat == Status.EMPTY:
                break
            #if data exists, return that node
            elif p.stat == Status.OCCUPIED and p.key == key:
                return p
            #in case of deleted
            #then rehash and re-assign the corresponding node to re-hashed node
            hash = self.rehash_value(hash)
            p = self.table[hash]
        
        #in case if corresponding node is not found
        return None
    
    def search(self, key: Any) -> Any:
        p = self.search_node(key)
        if p is not None:
            return p.value
        #in case corresponding node is empty
        else:
            return None
        
    def add(self, key: Any, value: Any) -> bool:
        if self.search(key) is not None:
            return False
        
        hash = self.hash_value(key)
        p = self.table[hash]

        #if corresponding node is empty or deleted, add new bucket
        for i in range(self.capacity):
            if p.stat == Status.EMPTY or p.stat == Status.DELETED:
                self.table[hash] = Bucket(key, value, Status.OCCUPIED)
                return True
            #in case when node is occupied, rehash and move to next bucket
            hash = self.rehash_value(hash)
            p = self.table[hash]
        
        #when all the hash table is filled
        return False
    
    #simply change the status to remove the bucket
    def remove(self, key: Any) -> int:
        p = self.search_node(key)
        if p is None:
            return False
        p.set_status(Status.DELETED)
        return True
    
    def dump(self) -> None:
        for i in range(self.capacity):
            print(f'{i:2} ', end = '')
            if self.table[i].stat == Status.OCCUPIED:
                print(f'{self.table[i].key} ({self.table[i].value})')
            elif self.table[i].stat == Status.EMPTY:
                print('-- EMPTY --')
            elif self.table[i].stat == Status.DELETED:
                print('--DELETED--')