# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 16:23:53 2020

@author: Faysal
"""

"""
Singly Linked List
"""

class SingleNode:
    def __init__(self, key):
        self.key = key
        self.next = None
    
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def push_front(self, key):
        node = SingleNode(key)
        node.next = self.head
        self.head = node
        if self.tail is None:
            self.tail = self.head
    
    def top_front(self):
        if self.head is None:
            return None
        return self.head.key
    
    def pop_front(self):
        if self.head is None:
            return None
        self.head = self.head.next 
        if self.head is None:
            self.tail = None
            
    def push_back(self, key):
        node = SingleNode(key)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
            
    def top_back(self):
        if self.tail is None:
            return None
        return self.tail.key 
    
    def pop_back(self):
        if self.head is None:
            return None
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            p = self.head 
            while p.next.next is not None:
                p = p.next 
            p.next = None
            self.tail = p
            
    def add_after(self, node, key):
        node2 = SingleNode(key)
        node2.next = node.next 
        node.next = node2 
        if self.tail == node:
            self.tail = node2 
    
    def add_before(self, node, key):
        node2 = SingleNode(key)
        node2.next = node
        if self.head != node:
            p = self.head 
            while p.next != node:
                p = p.next 
            p.next = node2 
        else:
            self.head = node2 
            
    def find(self, key):
        if self.head is None:
            return False
        p = self.head 
        while p.next is not None:
            if key == p.key:
                return True 
            p = p.next 
        if self.tail.key == key:
            return True 
        return False
    
    
    def empty(self):
        if self.head is None:
            return True 
        return False 
    
    def erase(self, key):
        if self.head is None:
            return
        if self.head.key == key:
            self.pop_front()
            return
        p = self.head 
        while p.next.key != key:
            p = p.next 
        p.next = p.next.next 
        if p.next is None:
            self.tail = p
            
            
    def get(self, key):
        if self.head is None:
            return None
        if self.head.key == key:
            return self.head
        p = self.head 
        while p.next.key != key:
            p = p.next 
        return p.next 
    
    def print(self):
        if self.empty():
            return 
        if self.head == self.tail:
            print(self.head.key)
            return 
        p = self.head 
        while p.next is not None:
            print(p.key, end=' ')
            p = p.next 
        print(p.key) 
        
if __name__ == '__main__':
    
    llist = SinglyLinkedList()
    llist.push_front(7)
    llist.push_back(10)
    llist.pop_back()
    llist.push_back(4)
    llist.push_back(13)
    llist.print()
    llist.add_before(llist.get(7), 5)
    llist.print()
    print(llist.find(10))
        








