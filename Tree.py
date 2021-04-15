from typing import Any, List, Callable, Union
from Lab_2 import Queue
class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self, value_):
        self.children = []
        self.value = value_


    def is_leaf(self) -> bool:
        if self.children == None:
            return True
        else:
            return False

    def add(self, child: 'TreeNode'):
        if self != None:
            self.children.append(child)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]):
        visit(self)
        for i in self.children:
            i.for_each_deep_first(visit)

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]):
        visit(self)
        q = Queue()
        for i in self.children:
            q.enqueue(i)
        while len(q) != 0:
            a = q.dequeue()
            a.for_each_level_order(visit)

    def search(self, value: Any) -> 'TreeNode':
        if self.value == value:
            return self
        for i in self.children:
            i.search(value)
            if i.value == value:
                return i

    def __str__(self) -> str:
        return str(self.value)
        
class Tree:
    root: 'TreeNode'
    
    def __init__(self, value):
        self.root = TreeNode(value)

    def add(self, value: Any, parent_value: Any):
        NewNode = TreeNode(value)
        HelperNode = self.root.search(parent_value)
        if HelperNode != None:
            HelperNode.add(NewNode)

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]):
        self.root.for_each_level_order(visit)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]):
        self.root.for_each_deep_first(visit)

    def show(self):
        self.for_each_level_order(print)

Drzewo = Tree('F')

Drzewo.add('B','F')
Drzewo.add('G','F')
Drzewo.add('A','B')
Drzewo.add('D','B')
Drzewo.add('C','D')
Drzewo.add('E','D')
Drzewo.add('I','G')
Drzewo.add('H','I')

Drzewo.root.for_each_level_order(print)
pass