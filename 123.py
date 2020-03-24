#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/11/7 22:35 
# @Author : Patrick 
# @File : 123.py 
# @Software: PyCharm


class Node:
    def __init__(self, x):
        self.value = x
        self.next = None


# 1->2->3->4->5   1,3
# 1->4->3->2->5


def reverseT(head, m, n):
    p = q = a = b = head

    l = []
    count = 0
    while count != m:
        count += 1
        p = p.next
        if count != m - 1:
            a = a.next

    while count != n:
        count += 1
        l.append(p)
        p = p.next
    b = p.next

    a.next = l[-1]
    for i in range(len(l) - 1, 1, -1):
        l[i].next = l[i - 1]
    l[0].next = b
    #
    # count = 0
    # while count

    return head


def reverse(node):
    pass
