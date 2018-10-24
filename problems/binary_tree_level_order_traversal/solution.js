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
    var queue = [{
        level: 0,
        node: root
    }];
    var output = [];
    var nodeObj;
    while(queue.length) {
        nodeObj = queue.pop();
        if (!output[nodeObj.level]) {
            output[nodeObj.level] = [nodeObj.node.val];
        } else {
            output[nodeObj.level].splice(0, 0, nodeObj.node.val);
        }
        if (nodeObj.node.left) {
            queue.push({
                level: nodeObj.level + 1,
                node: nodeObj.node.left
            });
        }
        if (nodeObj.node.right) {
            queue.push({
                level: nodeObj.level + 1,
                node: nodeObj.node.right
            })
        }
    }
    return output;
};