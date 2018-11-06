/**
 * Initialize your data structure here.
 */
var MyHashMap = function() {
  this.storage = [];
  this.hashFunc = function(key) {
    return (key + 1) % 10000;
  }
};

/**
 * value will always be non-negative. 
 * @param {number} key 
 * @param {number} value
 * @return {void}
 */
MyHashMap.prototype.put = function(key, value) {
  var hashed = this.hashFunc(key);
  if (this.storage[hashed] === undefined) {
    this.storage[hashed] = [];
  }
  for (var i = 0; i < this.storage[hashed].length; i++) {
    if (this.storage[hashed][i][0] === key) {
      this.storage[hashed].splice(i, 1, [key, value]);
      return;
    }
  }
  this.storage[hashed].push([key, value]);
};

/**
 * Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key 
 * @param {number} key
 * @return {number}
 */
MyHashMap.prototype.get = function(key) {
  var hashed = this.hashFunc(key);
  if (this.storage[hashed] === undefined) {
    return -1;
  }
  for (var i = 0; i < this.storage[hashed].length; i++) {
    if (this.storage[hashed][i][0] === key) {
      return this.storage[hashed][i][1];
    }
  }
  return -1;
};

/**
 * Removes the mapping of the specified value key if this map contains a mapping for the key 
 * @param {number} key
 * @return {void}
 */
MyHashMap.prototype.remove = function(key) {
  var hashed = this.hashFunc(key);
  if (this.storage[hashed] === undefined) {
    return;
  }
  for (var i = 0; i < this.storage[hashed].length; i++) {
    if (this.storage[hashed][i][0] === key) {
      this.storage[hashed].splice(i, 1);
    }
  }
};

/** 
 * Your MyHashMap object will be instantiated and called as such:
 * var obj = Object.create(MyHashMap).createNew()
 * obj.put(key,value)
 * var param_2 = obj.get(key)
 * obj.remove(key)
 */