#Bartosz Białczak
from typing import Any, Callable

class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value: Any):
        self.value = value
        self.left_child = None
        self.right_child = None

    def is_leaf(self) -> bool:
        if self.right_child == None and self.left_child == None:
            return True
        else:
            return False

    def add_left_child(self, value: Any):
        if self == None:
            return
        else:
            self.left_child = BinaryNode(value)


    def add_right_child(self, value: Any):
        if self == None:
            return
        else:
            self.right_child = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[[Any], None]):
        if self == None:
            return
        if self.left_child != None:
            self.left_child.traverse_in_order(visit)
        visit(self)
        if self.right_child != None:
            self.right_child.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        if self == None:
            return
        if self.left_child != None:
            self.left_child.traverse_post_order(visit)
        if self.right_child != None:
            self.right_child.traverse_post_order(visit)
        visit(self)

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        if self == None:
            return
        visit(self)
        if self.left_child != None:
            self.left_child.traverse_pre_order(visit)
        if self.right_child != None:
            self.right_child.traverse_pre_order(visit)

    def __str__(self):
        return str(self.value)

    def to_show(self): #większość ze stackoverflow, ale rozumiem co się dzieje w kodzie. Można zapytać ;)
        if self.right_child == None and self.left_child == None:
            line = '%s' % self.value
            width = len(line)
            height = 1
            middle = height // 2
            return [line], width, height, middle

        if self.right_child == None:
            lines, n, p, x = self.left_child.to_show()
            s = '%s' % self.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        if self.left_child == None:
            lines, n, p, x = self.right_child.to_show()
            s = '%s' % self.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        left, n, p, x = self.left_child.to_show()
        right, m, q, y = self.right_child.to_show()
        s = '%s' % self.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
        
class BinaryTree:
    root: BinaryNode

    def __init__(self, value):
        self.root = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[[Any], None]):
        if self == None:
            return
        else:
            self.root.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        if self == None:
            return
        else:
            self.root.traverse_post_order(visit)

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        if self == None:
            return
        else:
            self.root.traverse_pre_order(visit)

    def show(self):
        lines, *_ = self.root.to_show()
        for line in lines:
            print(line)

tree = BinaryTree(10)
tree.root.add_left_child(9)
tree.root.add_right_child(2)
tree.root.left_child.add_left_child(1)
tree.root.left_child.add_right_child(3)
tree.root.right_child.add_left_child(4)
tree.root.right_child.add_right_child(6)
tree.root.left_child.right_child.add_left_child(100)
tree.root.left_child.right_child.add_right_child(200)
tree.root.right_child.left_child.add_left_child(300)
tree.root.right_child.left_child.add_right_child(400)

assert tree.root.value == 10
assert tree.root.right_child.value == 2
assert tree.root.right_child.is_leaf() is False
assert tree.root.left_child.left_child.value == 1
assert tree.root.left_child.left_child.is_leaf() is True

print('Show')
tree.show()
pass