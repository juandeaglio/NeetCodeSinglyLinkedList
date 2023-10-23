from typing import List


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        if self.head is None:
            return -1
        return self.head.value
    def insertHead(self, val: int) -> None:
        self.head = Node(val)
    def insertTail(self, val: int) -> None:
        pass
    def remove(self, index: int) -> bool:
        curNode = self.head
        while curNode.next:
            curNode = curNode.next

        if curNode == None:
            return False

        return True
    def getValues(self) -> List[int]:
        list = []
        return list
