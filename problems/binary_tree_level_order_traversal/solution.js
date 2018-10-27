/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var levelOrder = function(root) {
  if (!root) {
    return [];
  }
  var output = [];
  var queue = [{
    level: 0,
    node: root
  }];
  while (queue.length) {
    node = queue.pop();
    if (!output[node.level]) {
      output[node.level] = [];
    }
    output[node.level].push(node.node.val);
    if (node.node.left) {
      queue.unshift({
        node: node.node.left,
        level: node.level + 1
      });
    }
    if (node.node.right) {
      queue.unshift({
        node: node.node.right,
        level: node.level + 1
      });
    }
  }
  return output;
}