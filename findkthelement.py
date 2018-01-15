# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 17:26:02 2017

@author: voldemort
"""

from listfifo import LinkedListFIFO
from node import Node


class LinkedListFIFO_find_kth(LinkedListFIFO):


    def find_kth_to_last(self, k):
        p1, p2 = self.head, self.head
        i = 0
        while p1:
            if i > k:
                try:
                    p2 = p2.pointer
                except:
                    break
            p1 = p1.pointer
            i += 1
        return p2.value



if __name__ == '__main__':
    ll = LinkedListFIFO_find_kth()
    for i in range(1, 11):
        ll.addNode(i)
    print('The Linked List:')
    print(ll._printList())
    k = 3
    k_from_last = ll.find_kth_to_last(k)
    print("The %dth element to the last of the LL of size %d is %d" %(k, ll.length, k_from_last))