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
        output, q = [str(root.val)], deque([root])
        while q:
            n = q.popleft()
            if n.left:
                output.append(str(n.left.val))
                q.append(n.left)
            else:
                output.append('null')
            if n.right:    
                output.append(str(n.right.val))
                q.append(n.right)
            else:
                output.append('null')    
        while output[-1] == 'null': output.pop()        
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
        while q and buf:
            n = q.popleft()
            s = buf.popleft()
            if s != 'null':
                l = TreeNode(int(s))
                n.left = l
                q.append(l)
            if not buf: break    
            s = buf.popleft()
            if s != 'null':
                r = TreeNode(int(s))
                n.right = r
                q.append(r)
        return root        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))