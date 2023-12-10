import random
import os
import time

class Universe:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.world = [[' ' for _ in range(width)] for _ in range(height)]

    def show(self):
        for row in self.world:
            print(''.join(row))
        print()

    def seed(self):
        for i in range(self.height):
            for j in range(self.width):
                if random.random() < 0.25:
                    self.world[i][j] = '*'

    def alive(self, i, j):
        if i < 0 or i >= self.height or j < 0 or j >= self.width:
            return False
        return self.world[i][j] == '*'

    def neighbors(self, i, j):
        count = 0
        for x in range(i-1, i+2):
            for y in range(j-1, j+2):
                if (x, y) != (i, j) and self.alive(x, y):
                    count += 1
        return count

    def next(self, i, j):
        alive = self.alive(i, j)
        count = self.neighbors(i, j)
        if alive and (count < 2 or count > 3):
            return False
        elif not alive and count == 3:
            return True
        return alive

    def step(self):
        new_world = [[' ' for _ in range(self.width)] for _ in range(self.height)]
        for i in range(self.height):
            for j in range(self.width):
                new_world[i][j] = '*' if self.next(i, j) else ' '
        self.world = new_world

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    height = 15
    width = 80
    universe = Universe(height, width)
    universe.show()
    universe.seed()
    while True:
        clear_screen()
        universe.show()
        universe.step()
        time.sleep(0.2)

if __name__ == "__main__":
    main()
