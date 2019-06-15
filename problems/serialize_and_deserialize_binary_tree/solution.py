# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        output = []
        if root is None:
            return output
        output.append(root.val)
        q = collections.deque()
        q.append(root)
        while q:
            n = q.popleft()
            if n.left:
                q.append(n.left)
                output.append(n.left.val)
            else:
                output.append("null")
            if n.right:
                q.append(n.right)
                output.append(n.right.val)
            else:
                output.append("null")
        while output[-1] == "null":
            output.pop()
        buff = "["    
        for e in output:
            if e == 'null':
                buff += e
            else:
                buff += str(e)
            buff += ','    
        return buff[:-1] + ']'        
                

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) < 3:
            return None
        nodes = data[1:-1].split(",")
        root = TreeNode(int(nodes[0]))
        q = collections.deque()
        q.append(root)
        i = 1
        while q:
            n = q.popleft()
            if i < len(nodes) and nodes[i] != 'null':
                left_t = TreeNode(int(nodes[i]))
                n.left = left_t
                q.append(left_t)
            i += 1    
            if i < len(nodes) and nodes[i] != 'null':
                right_t = TreeNode(int(nodes[i]))
                n.right = right_t
                q.append(right_t)
            i += 1    
        return root        
            

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))