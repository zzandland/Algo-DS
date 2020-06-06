class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, size):
        self.key_to_value = {}
        self.head = None
        self.tail = None
        self.space = size

    def __str__(self):
        curr = self.head
        output = []
        while curr:
            output.append(str(curr.key))
            curr = curr.next
        return ' -> '.join(output)

    def bring_item_to_front(self, key):
        if self.head.key == key:
            return
        curr = self.key_to_value[key]

        # link curr's prev node to curr's next node
        curr.prev.next = curr.next

        if curr.next is not None:
            curr.next.prev = curr.prev
        else:
            self.tail = curr.prev

        # make curr the new head
        self.head.prev = curr
        curr.next = self.head
        curr.prev = None

        self.head = curr

    def put(self, key, value):
        # if key exists in the dictionary then we want to replace the value
        # with the new value and then bring item to the front
        if key in self.key_to_value:
            self.key_to_value[key].val = value
            self.bring_item_to_front(key)
            return

        self.key_to_value[key] = Node(key, value)
        # if there is no head
        if not self.head:
            self.head = self.key_to_value[key]
            self.tail = self.head
        else:
            # create a new node and set it as the head
            self.key_to_value[key].next = self.head
            self.head.prev = self.key_to_value[key]
            self.head = self.key_to_value[key]
        # lose the tail if there is no space available
        if self.space <= 0:
            # delete the node from dictionary
            del(self.key_to_value[self.tail.key])
            save = self.tail.prev
            save.next = None
            self.tail.prev = None  # could omit this line?
            self.tail = save
        else:
            self.space -= 1

    def get(self, key):
        if not self.head or key not in self.key_to_value:
            return -1

        if self.head.key == key:
            return self.key_to_value[key].val

        self.bring_item_to_front(key)

        return self.head.val

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)