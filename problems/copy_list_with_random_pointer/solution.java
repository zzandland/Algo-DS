/**
 * Definition for singly-linked list with a random pointer.
 * class RandomListNode {
 *     int label;
 *     RandomListNode next, random;
 *     RandomListNode(int x) { this.label = x; }
 * };
 */
import java.util.HashMap;

public class Solution {
  HashMap<RandomListNode, RandomListNode> map = new HashMap<RandomListNode, RandomListNode>();

  public RandomListNode copyRandomList(RandomListNode head) {
    RandomListNode output = null;
    RandomListNode outputHead = null;
    while (head != null) {
      if (output == null) {
        output = copyNode(head);
        outputHead = output;
      } else {
        output.next = copyNode(head);
        output = output.next;
      }
      if (head.random != null) output.random = copyNode(head.random);
      head = head.next;
    }
    return outputHead;
  }

  private RandomListNode copyNode(RandomListNode node) {
    if (node != null) {
      if (map.containsKey(node)) {
        return map.get(node);
      } else {
        map.put(node, new RandomListNode(node.label));
        return map.get(node);
      } 
    } 
    return null;
  }
}