from extratypes import Tree
import sys
sys.setrecursionlimit(10**6)
import copy

def solution(T):
    result = pre_order_traversal(T)
    return result

def pre_order_traversal(self):
    self.maxValue = 1
    def _pre_order_traversal(root, xList):
        xList_copy = copy.deepcopy(xList)
        if root is None:
            if self.maxValue < len(xList_copy):
                self.maxValue = len(xList_copy)
            pass
        elif root.x in xList_copy:
            if self.maxValue < len(xList_copy):
                self.maxValue = len(xList_copy)
            pass
        else:
            xList_copy.append(root.x)
            _pre_order_traversal(root.l, xList_copy)
            _pre_order_traversal(root.r, xList_copy)
    _pre_order_traversal(self, [])
    return self.maxValue

