# -*- coding:utf-8 -*-
# author: li zhang
# date: 2020/3/31 10:41

class Node(object):

    def __init__(self, item):
        self.val = item
        self.left = None
        self.right = None

class Tree(object):

    def __init__(self, head = None):
        self.root = head

    def add(self, item):  # 默认为以满二叉树的方式插入
        node = Node(item)
        if self.root is None:  # 根节点为空
            self.root = node
            return

        queue = []  # 用来存放处理的节点
        queue.append(self.root)

        while queue:
            cur_node = queue.pop(0)
            if cur_node.left is None:
                cur_node.left = node
                return
            else:
                queue.append(cur_node.left)
            if cur_node.right is None:
                cur_node.right = node
                return
            else:
                queue.append(cur_node.right)

    def breadth_travel(self):   # 广度遍历

        if self.root is None:
            print('The tree is None!')
            return

        queue = [self.root]

        while queue:
            cur_node = queue.pop(0)
            print(cur_node.val, end=' ')
            if cur_node.left is not None:
                queue.append(cur_node.left)
            if cur_node.right is not None:
                queue.append(cur_node.right)

    def pre_order(self, node):
        """先序遍历"""
        if node is None:
            return

        print(node.val, end=' ')
        self.pre_order(node.left)
        self.pre_order(node.right)

    def in_order(self, node):
        """中序遍历"""
        if node is None:
            return

        self.in_order(node.left)
        print(node.val, end=' ')
        self.in_order(node.right)

    def post_order(self, node):
        """后序遍历"""
        if node is None:
            return

        self.post_order(node.left)
        self.post_order(node.right)
        print(node.val, end=' ')

    def build_tree(self, pre_order, in_order):  # TODO
        """重建二叉树
        一定要知道结束条件
        """
        if len(pre_order) == 0 or len(in_order) == 0:
            return
        root = Node(pre_order[0])
        middle = in_order.index(pre_order[0])
        root.left = self.build_tree(pre_order[1:middle+1], in_order[0:middle])
        root.right = self.build_tree(pre_order[middle+1:], in_order[middle+1:])
        return root



def main():
    tree = Tree()
    tree.breadth_travel()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breadth_travel()
    print('\n')
    tree.pre_order(tree.root)
    print('\n')
    tree.in_order(tree.root)
    print('\n')
    tree.post_order(tree.root)

    print('\n')
    pre_order = [3, 9, 20, 15, 7]
    in_order = [9, 3, 15, 20, 7]
    tree.build_tree(pre_order, in_order)


if __name__ == '__main__':
    main()