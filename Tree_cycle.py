class Node(object):
    def __init__(self, data=-1, lchild=None, rchild=None):
        '''
        :param data:数据 
        :param lchild: 左结点
        :param rchild: 右结点
        '''
        self.data = data
        self.lchild = lchild
        self.rchild = rchild


class BinaryTree(object):
    def __init__(self):
        self.root = Node()

    def isEmpty(self):
        return True if self.root.data == -1 else False

    def add(self, data):
        '''
        每一批新增节点先传入data，判断当前二叉树是否为空，如果为空，更结点等于当前节点，否则插入左/右结点
        :param data: 
        :return: 
        '''
        node = Node(data)
        if self.isEmpty():
            self.root = node
        else:
            tree_node = self.root
            queue = []
            queue.append(self.root)
            while queue:
                tree_node = queue.pop()
                if tree_node.lchild is None:
                    tree_node.lchild = node
                    return
                elif tree_node.rchild is None:
                    tree_node.rchild = node
                    return
                else:
                    queue.append(tree_node.lchild)
                    queue.append(tree_node.rchild)

    def pre_order(self, start):
        node = start
        if node is None:
            return
        print(node.data)
        if node.lchild is None and node.rchild is None:
            return
        self.pre_order(node.lchild)
        self.pre_order(node.rchild)
