import java.util.HashSet;

class Solution {
  public boolean isValidSudoku(char[][] board) {
    for (int i = 1; i <= 9; i++) {
      if (!checkBox(board, i)) return false;
    }
    return checkRows(board) && checkColumns(board);
  }
  
  public boolean checkRows(char[][] board) {
    for (char[] row : board) {
      HashSet<Integer> numSet = new HashSet<Integer>();
      for (char slot : row) {
        if (slot != '.') {
          int value = Integer.parseInt(String.valueOf(slot));
          if (value > 9 || value < 1 || numSet.contains(value)) return false;
          else numSet.add(value);
        }
      }
    }
    return true;
  }
  
  public boolean checkColumns(char[][] board) {
    for (int i = 0; i < board[0].length; i++) {
      HashSet<Integer> numSet = new HashSet<Integer>();
      for (int j = 0; j < board.length; j++) {
        if (board[j][i] != '.') {
          int value = Integer.parseInt(String.valueOf(board[j][i]));
          if (value > 9 || value < 1 || numSet.contains(value)) return false;
          else numSet.add(value);
        }
      }
    }
    return true;
  }
  
  public boolean checkBox(char[][] board, int boxNum) {
    switch (boxNum) {
      case 1:
        return checkBoxHelper(board, 0, 2, 0, 2);
      case 2:
        return checkBoxHelper(board, 3, 5, 0, 2);
      case 3:
        return checkBoxHelper(board, 6, 8, 0, 2);
      case 4:
        return checkBoxHelper(board, 0, 2, 3, 5);
      case 5:
        return checkBoxHelper(board, 3, 5, 3, 5);
      case 6:
        return checkBoxHelper(board, 6, 8, 3, 5);
      case 7:
        return checkBoxHelper(board, 0, 2, 6, 8);
      case 8:
        return checkBoxHelper(board, 3, 5, 6, 8);
      case 9:
        return checkBoxHelper(board, 6, 8, 6, 8);
    }
    return true;
  }
  
  public boolean checkBoxHelper(char[][] board, int x, int xEnd, int y, int yEnd) {
    HashSet<Integer> numSet = new HashSet<Integer>();
    for (int i = y; i <= yEnd; i++) {
      for (int j = x; j <= xEnd; j++) {
        if (board[i][j] != '.') {
          int value = Integer.parseInt(String.valueOf(board[i][j]));
          if (value > 9 || value < 1 || numSet.contains(value)) return false;
          else numSet.add(value);
        }
      }
    }    
    return true;
  }
}