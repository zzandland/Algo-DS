/**
 * Initialize your data structure here.
 */
var MyHashSet = function() {
  this.storage = [];
  this.hashFunc = function(val) {
    return val % 10000;
  }
};

/** 
 * @param {number} key
 * @return {void}
 */
MyHashSet.prototype.add = function(key) {
  var hashed = this.hashFunc(key);
  if (this.storage[hashed] === undefined) {
    this.storage[hashed] = [];
  }
  for (var i = 0; i < this.storage[hashed].length; i++) {
    if (this.storage[hashed][i] === key) {
      return;
    }
  }
  this.storage[hashed].push(key);
  return;
};

/** 
 * @param {number} key
 * @return {void}
 */
MyHashSet.prototype.remove = function(key) {
  var hashed = this.hashFunc(key);
  if (this.storage[hashed] === undefined) {
    this.storage[hashed] = [];
  }
  for (var i = 0; i < this.storage[hashed].length; i++) {
    if (this.storage[hashed][i] === key) {
      this.storage[hashed].splice(i, 1);
      return;
    }
  }
};

/**
 * Returns true if this set contains the specified element 
 * @param {number} key
 * @return {boolean}
 */
MyHashSet.prototype.contains = function(key) {
  var hashed = this.hashFunc(key);
  if (this.storage[hashed] === undefined) {
    return false;
  } else {
    for (var i = 0; i < this.storage[hashed].length; i++) {
      if (this.storage[hashed][i] === key) {
        return true;
      }
    }
    return false;
  }
};

/** 
 * Your MyHashSet object will be instantiated and called as such:
 * var obj = Object.create(MyHashSet).createNew()
 * obj.add(key)
 * obj.remove(key)
 * var param_3 = obj.contains(key)
 */