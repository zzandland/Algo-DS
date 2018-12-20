/**
 * Initialize your data structure here.
 */
var SinglyLinkedNode = function(val) {
  this.val = val;
  this.next = null;
}

var MyLinkedList = function() {
  this.head = null;
  this.tail = null;
};

/**
 * Get the value of the index-th node in the linked list. If the index is invalid, return -1. 
 * @param {number} index
 * @return {number}
 */
MyLinkedList.prototype.get = function(index) {
  if (!this.head) {
    return -1;
  }
  var node = this.head;
  while (index > 0 && node.next) {
    node = node.next;
    index--;
  }
  if (index === 0) { 
    return node.val;
  } else {
    return -1;
  }
};

/**
 * Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. 
 * @param {number} val
 * @return {void}
 */
MyLinkedList.prototype.addAtHead = function(val) {
  var newHead = new SinglyLinkedNode(val);  
  if (!this.head) {
    this.head = newHead; 
  } else {
    var oldHead = this.head;
    this.head = newHead;
    this.head.next = oldHead;
  }
  if (!this.tail) this.tail = newHead;
};

/**
 * Append a node of value val to the last element of the linked list. 
 * @param {number} val
 * @return {void}
 */
MyLinkedList.prototype.addAtTail = function(val) {
  var newTail = new SinglyLinkedNode(val);
  if (!this.head) this.head = newTail;
  if (!this.tail) {
    this.tail = newTail; 
  } else {
    var oldTail = this.tail;
    this.tail = newTail;
    oldTail.next = this.tail;
  }
};

/**
 * Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. 
 * @param {number} index 
 * @param {number} val
 * @return {void}
 */
MyLinkedList.prototype.addAtIndex = function(index, val) {
  if (index === 0) {
    this.addAtHead(val);
  } else if (index > 0) {
    var node = this.head;
    while (index - 1 > 0 && node) {
      node = node.next;
      index--;
    }
    if (node) {
      var oldNext = node.next;
      var newNode = new SinglyLinkedNode(val);
      node.next = newNode;
      newNode.next = oldNext;
      if (!oldNext) {
        this.tail = newNode;
      }
    }
  }
};

/**
 * Delete the index-th node in the linked list, if the index is valid. 
 * @param {number} index
 * @return {void}
 */
MyLinkedList.prototype.deleteAtIndex = function(index) {
  if (index === 0) {
    this.head = this.head.next;
  } else if (index > 0) {
    var node = this.head;
    while (index - 1 > 0 && node) {
      node = node.next;
      index--;
    }
    if (node && node.next) {
      node.next = node.next.next;
      if (!node.next) this.tail = node;
    }
  }
};

/** 
 * Your MyLinkedList object will be instantiated and called as such:
 * var obj = Object.create(MyLinkedList).createNew()
 * var param_1 = obj.get(index)
 * obj.addAtHead(val)
 * obj.addAtTail(val)
 * obj.addAtIndex(index,val)
 * obj.deleteAtIndex(index)
 */