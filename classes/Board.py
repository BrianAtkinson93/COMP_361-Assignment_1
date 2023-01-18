import random
from classes.Cell import Cell


class Board:
    def __init__(self, width, height, obstacle_percentage=10):
        """
        Initializes the board with the given width, height and obstacle percentage

        :param width: width of the board
        :param height: height of the board
        :param obstacle_percentage: percentage of the board that is obstacles
        """
        self.width = width
        self.height = height
        self.obstacle_percentage = obstacle_percentage
        self.board_layout = [[Cell(x, y) for x in range(self.width)] for y in range(self.height)]
        self.start = (random.randint(0, self.height - 1), random.randint(0, self.width - 1))
        self.end = (random.randint(0, self.height - 1), random.randint(0, self.width - 1))
        self.populate()

    def populate(self):
        """
        Populate the board with obstacles randomly
        """
        total_cells = self.height * self.width
        obstacle_count = int(total_cells * (self.obstacle_percentage / 100))

        for _ in range(obstacle_count):
            obstacle = (random.randint(0, self.height - 1), random.randint(0, self.width - 1))
            self.board_layout[obstacle[0]][obstacle[1]].is_obstacle = True

    def run_simulation(self):
        """
        This function simulates the pathfinding algorithm by initializing a 2D list to store the distance values,
        setting the distance at the starting point to 0, creating a queue to hold the cells to be checked,
        and while there are cells to be checked, it gets the next cell from the queue, gets the distance value for the current cell,
        checks the cells adjacent to the current cell, and updates the distance value for the adjacent cell and add the
        adjacent cell to the queue
        """
        # Create a 2D list to store the distance values
        self.distances = [[-1 for _ in range(self.width)] for _ in range(self.height)]
        # Set the distance at the starting point to 0
        self.distances[self.start[0]][self.start[1]] = 0
        # Create a queue to hold the cells to be checked
        queue = [self.start]
        # While there are cells to be checked
        while queue:
            # Get the next cell from the queue
            current = queue.pop(0)
            # Get the distance value for the current cell
            distance = self.distances[current[0]][current[1]]
            # Check the cells adjacent to the current cell
            for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                x, y = current[0] + i, current[1] + j
                if x < 0 or y < 0 or x >= self.height or y >= self.width:
                    continue
                if self.distances[x][y] != -1 or self.board_layout[x][y].is_obstacle:
                    continue
                # Update the distance value for the adjacent cell
                self.distances[x][y] = distance + 1
                # Add the adjacent cell to the queue
                queue.append((x, y))

    def output_map(self):
        for i, row in enumerate(self.board_layout):
            for j, cell in enumerate(row):
                if (i, j) == self.start:
                    print("S", end=" ")
                elif (i, j) == self.end:
                    print("E", end=" ")
                elif cell.is_obstacle:
                    print("X", end=" ")
                else:
                    print("0", end=" ")
            print()
        print('\n')

    def output_distances(self):
        for row in self.distances:
            print(row)
        print("\n")
        print("Start:", self.start)
        print("End:", self.end)
