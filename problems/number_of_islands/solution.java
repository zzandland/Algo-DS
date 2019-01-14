class Solution {
  public int numIslands(char[][] grid) {
        Queue<int[]> queue = new LinkedList<>();
        int shapes = 0;
        int[] coord = new int[2];
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                if (grid[i][j] == '1') {
                    shapes++;
                    grid[i][j] = '0';
                    coord[0] = i;
                    coord[1] = j;
                    queue.add(coord.clone());
                    while (queue.peek() != null) {
                        coord = queue.poll();
                        int y = coord[0];
                        int x = coord[1]; 
                        if (y - 1 >= 0 && grid[y - 1][x] == '1') {
                            coord[0] = y - 1;
                            coord[1] = x;
                            grid[y - 1][x] = '0';
                            queue.add(coord.clone());
                        }
                        if (y + 1 < grid.length && grid[y + 1][x] == '1') {
                            coord[0] = y + 1;
                            coord[1] = x;
                            grid[y + 1][x] = '0';
                            queue.add(coord.clone());
                        }
                        if (x - 1 >= 0 && grid[y][x - 1] == '1') {
                            coord[0] = y;
                            coord[1] = x - 1;
                            grid[y][x - 1] = '0';
                            queue.add(coord.clone());
                        }
                        if (x + 1 < grid[i].length && grid[y][x + 1] == '1') {
                            coord[0] = y;
                            coord[1] = x + 1;
                            grid[y][x + 1] = '0';
                            queue.add(coord.clone());
                        }
                    }
                }
            }
        }
        return shapes;
  }
}