package trees;
import java.util.ArrayList;

public interface TreeMethods<T> {
  public ArrayList<T> preorderTraversal();
  public ArrayList<T> inorderTraversal();
  public ArrayList<T> postorderTraversal();
  public ArrayList<T> BreathFirstTraversal();
}
