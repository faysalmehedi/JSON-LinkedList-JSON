# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 15:04:17 2020

@author: Faysal
"""

import json
from singly_linked_list import SinglyLinkedList

with open('linked_list.json') as f:
    data = json.load(f)

new_linked_list = SinglyLinkedList()
new_data = {}

for li in data['list']:
    new_linked_list.push_back(li)

p = new_linked_list.head
i = 0
while p is not None:
    key = f'node_{i}'
    new_data[key] = p.key
    i += 1
    p = p.next
    
with open('result.json', 'w') as f:
  json.dump(new_data, f, indent=2)



