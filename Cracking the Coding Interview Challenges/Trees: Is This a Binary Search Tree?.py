""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root):
    return isBST(root, -float('inf'), float('inf'))
    
def isBST(node, min, max):
    if node==None:
        return True
    if node.data<=min or node.data>=max:
        return False
    return isBST(node.left, min, node.data) and isBST(node.right, node.data, max)
        
    
