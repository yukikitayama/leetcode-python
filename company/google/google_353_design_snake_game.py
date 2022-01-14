from typing import List
import collections


class SnakeGame:
    def __init__(self, width: int, height: int, food: List[List[int]]):
        # Queue left side is head, and right side is tail
        # Queue: [(row, col), (row, col), ...]
        self.snake = collections.deque([(0, 0)])
        # 1 is not really used
        self.snake_set = {(0, 0)}
        self.width = width
        self.height = height
        self.food = food
        # Index to iterate self.food list
        self.food_index = 0
        self.movement = {'U': [-1, 0], 'L': [0, -1], 'R': [0, 1], 'D': [1, 0]}

    def move(self, direction: str) -> int:
        new_head = (
            self.snake[0][0] + self.movement[direction][0],
            self.snake[0][1] + self.movement[direction][1]
        )

        # Row
        crosses_boundary1 = new_head[0] < 0 or new_head[0] >= self.height
        # Column
        crosses_boundary2 = new_head[1] < 0 or new_head[1] >= self.width

        # Check if the snake bites itself
        # If a new head cell is not in the set of snake body cells
        # and if a new head cell is not the tail of snake cells
        bites_itself = new_head in self.snake_set and new_head != self.snake[-1]

        #
        if crosses_boundary1 or crosses_boundary2 or bites_itself:
            return -1

        # If there's still remaining food
        if self.food_index < len(self.food):
            next_food_item = self.food[self.food_index]
        else:
            next_food_item = None

        # If there's available food and new head is on the food, eat it
        # self.food_index < len(self.food) to avoid None error
        # because when next_food_item is None, next_food_item[0] throws an error
        if self.food_index < len(self.food) and next_food_item[0] == new_head[0] and next_food_item[1] == new_head[1]:
            self.food_index += 1
        # If not food, delete tail
        else:
            # Pop from right
            tail = self.snake.pop()
            self.snake_set.remove(tail)

        #
        self.snake.appendleft(new_head)

        # Add cell to set for O(1) check
        self.snake_set.add(new_head)

        # -1 because length of snake becomes 1 after eating the first food,
        # originally 0 length even if self.snake contains (0, 0) originally
        return len(self.snake) - 1


if __name__ == '__main__':
    width = 3
    height = 2
    food = [[1, 2], [0, 1]]
    obj = SnakeGame(width, height, food)
    print(obj.move('R'))
    print(obj.move('D'))
    print(obj.move('R'))
    print(obj.move('U'))
    print(obj.move('L'))
    print(obj.move('U'))
