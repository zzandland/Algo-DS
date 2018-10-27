/**
 * Initialize your data structure here.
 * @param {number} size
 */
var MovingAverage = function(size) {
  this.queue = [];
  this.total = 0;
  this.size = size;
};

/** 
 * @param {number} val
 * @return {number}
 */
MovingAverage.prototype.next = function(val) {
  this.queue.unshift(val);
  this.total += val;
  if (this.queue.length <= this.size) {
    return this.total / this.queue.length;
  }
  this.total -= this.queue.pop();
  return this.total / this.queue.length;
};

/** 
 * Your MovingAverage object will be instantiated and called as such:
 * var obj = Object.create(MovingAverage).createNew(size)
 * var param_1 = obj.next(val)
 */