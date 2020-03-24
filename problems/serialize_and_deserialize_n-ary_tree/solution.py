"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque

class Codec:

    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if not root: return ''
        output = []
        def fn(n: Node) -> None:
            nonlocal output
            output.append(str(n.val))
            if n.children:
                for c in n.children:
                    fn(c)
                output.append('#')    
            else: output.append('#')        
        fn(root)
        return ','.join(output)

    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data: return None
        split, rt, i = data.split(','), Node(0, []), -1
        n = rt;
        def fn(n: Node) -> None:
            nonlocal i
            i+=1
            if split[i] == '#':
                i+=1
                return
            while i < len(split) and split[i] != '#':
                c = Node(int(split[i]), [])
                n.children.append(c)
                fn(c)
            i+=1    
        fn(rt)        
        return rt.children[0]
            
        
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))