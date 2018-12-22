/**
 * Initialize your data structure here.
 */
var DoublyLinkedNode = function(val) {
  this.val = val;
  this.next = this.prev = null;
}

var MyLinkedList = function() {
  this.head = this.tail = null;   
};

/**
 * Get the value of the index-th node in the linked list. If the index is invalid, return -1. 
 * @param {number} index
 * @return {number}
 */
MyLinkedList.prototype.get = function(index) {
  var node = this.head;
  while (index > 0 && node) {
    index--;
    node = node.next;
  }
  return node === null ? -1 : node.val;  
};

/**
 * Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. 
 * @param {number} val
 * @return {void}
 */
MyLinkedList.prototype.addAtHead = function(val) {
  var newNode = new DoublyLinkedNode(val);
  if (!this.head && !this.tail) {
    this.head = this.tail = newNode;
  } else {
    var oldHead = this.head;
    this.head = newNode;
    this.head.next = oldHead;
    oldHead.prev = this.head;    
  }
};

/**
 * Append a node of value val to the last element of the linked list. 
 * @param {number} val
 * @return {void}
 */
MyLinkedList.prototype.addAtTail = function(val) {
  var newNode = new DoublyLinkedNode(val);
  if (!this.head && !this.tail) {
    this.head = this.tail = newNode;
  } else {
    var oldTail = this.tail;
    this.tail = newNode;
    this.tail.prev = oldTail;
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
    return;
  } 
  var node = this.head;
  for (var i = 0; i < index && node; i++) {
    node = node.next;    
  }
  if (node) {
    var newNode = new DoublyLinkedNode(val);
    var prev = node.prev;
    newNode.next = node;
    newNode.prev = prev;
    prev.next = newNode;
    node.prev = newNode;
  } else if (!node && i === index) {
    this.addAtTail(val);
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
    this.head.prev = null;
    return;
  }
  var node = this.head;
  for (var i = 0; i < index && node; i++) {
    node = node.next;
  }
  if (node) {
    var prev = node.prev;
    if (node.next) {
      node.next.prev = prev;
    } 
    prev.next = node.next;
    if (!prev.next) {
      this.tail = prev;
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