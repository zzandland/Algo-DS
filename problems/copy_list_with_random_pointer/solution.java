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
  public RandomListNode copyRandomList(RandomListNode head) {
    HashMap<RandomListNode, RandomListNode> map = new HashMap<RandomListNode, RandomListNode>();
    RandomListNode copyHead = copyNext(head, map);
    copyRandom(head, copyHead, map);
    return copyHead;
  }

  private RandomListNode copyNext(RandomListNode head, HashMap<RandomListNode, RandomListNode> map) {
    RandomListNode output = null, outputHead = null;
    while (head != null) {
      if (output == null) {
        output = new RandomListNode(head.label);
        outputHead = output;
      } else {
        output.next = new RandomListNode(head.label);
        output = output.next;
      }
      map.put(head, output);
      head = head.next;
    }
    return outputHead;
  }

  private void copyRandom(RandomListNode head, RandomListNode copyHead, HashMap<RandomListNode, RandomListNode> map) {
    while (head != null) {
      if (head.random != null) copyHead.random = map.get(head.random);
      head = head.next;
      copyHead = copyHead.next;
    }
  }
}