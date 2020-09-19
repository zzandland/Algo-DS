# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return ''
        q = deque([root])
        output = []
        while q:
            n = q.popleft()
            if n:
                output.append(str(n.val))
                q.append(n.left)
                q.append(n.right)
            else:
                output.append('null')
        return ','.join(output)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        buf = deque(data.split(','))
        root = TreeNode(int(buf.popleft()))
        q = deque([root])
        while buf:
            n = q.popleft()
            l, r = buf.popleft(), buf.popleft()
            if l != 'null':
                left = TreeNode(int(l))
                n.left = left
                q.append(left)
            if r != 'null':
                right = TreeNode(int(r))
                n.right = right
                q.append(right)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))