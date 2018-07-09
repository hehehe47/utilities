class Node(object):
    def __init__(self, data, lchild, rchild):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild


def create(root):
    a = input('enter: ')
    if a == '#':
        root = None
    else:
        root = Node(a, None, Node)
        root.lchild = create(root.lchild)
        root.rchild = create(root.rchild)

    return root


def preorder(root):
    if not root:
        return
    else:
        print(root.data)
        preorder(root.lchild)
        preorder(root.rchild)


root = None
root = create(root)
preorder(root)
