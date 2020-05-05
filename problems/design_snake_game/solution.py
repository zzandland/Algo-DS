from collections import deque

class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.W = width
        self.H = height
        self.foods = deque(food)
        self.body = deque([(0, 0)])
        self.dir_ = {'U': (-1, 0), 'L': (0, -1), 'R': (0, 1), 'D': (1, 0)}

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        y, x = self.body[0]
        r, c = self.dir_[direction]
        ny, nx = y+r, x+c
        if not 0 <= ny < self.H or not 0 <= nx < self.W: return -1
        if self.foods and [ny, nx] == self.foods[0]: self.foods.popleft()
        else:
            self.body.pop()
            if (ny, nx) in self.body: return -1
        self.body.appendleft((ny, nx))
        return len(self.body)-1

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)