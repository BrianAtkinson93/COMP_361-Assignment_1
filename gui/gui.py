import random
import sys

from argparse import ArgumentTypeError

from PyQt6 import QtCore
from PyQt6.QtCore import QRectF
from PyQt6.QtGui import QColor, QPainter
from PyQt6.QtWidgets import QWidget, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QApplication


class Board:
    def __init__(self, columns, rows, obstacles):
        """
        Initializes the board with given number of columns, rows and obstacles.
        """
        self.distances = None
        self.columns = columns
        self.rows = rows
        self.obstacles = obstacles
        self.grid = [[0 for _ in range(columns)] for _ in range(rows)]
        self.populate_obstacles()
        self.start = self.choose_random_start()
        self.end = self.choose_random_end()

    def is_obstacle(self, x, y) -> bool:
        """
        Returns true if the cell at x, y is an obstacle.
        """
        return self.grid[x][y] == 1

    def populate_obstacles(self) -> None:
        """
        Populate the grid with obstacles randomly.
        """
        for x in range(self.rows):
            for y in range(self.columns):
                if random.randint(0, 100) < self.obstacles:
                    self.grid[x][y] = 1

    def choose_random_start(self) -> tuple:
        """
        Choose a random location on the board as the start location.
        """

        while True:
            x = random.randint(0, self.rows - 1)
            y = random.randint(0, self.columns - 1)
            if not self.is_obstacle(x, y):
                return x, y

    def choose_random_end(self) -> tuple:
        """
        Choose a random location on the board as the end location.
        """
        while True:
            x = random.randint(0, self.rows - 1)
            y = random.randint(0, self.columns - 1)
            if not self.is_obstacle(x, y):
                return x, y

    def run_algorithm(self) -> None:
        """
        Run the algorithm to calculate the shortest distance from start to end.
        """
        queue = [self.start]
        distances = [[-1 for _ in range(self.columns)] for _ in range(self.rows)]
        distances[self.start[0]][self.start[1]] = 0
        while queue:
            x, y = queue.pop(0)
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < self.rows and 0 <= new_y < self.columns and not self.is_obstacle(new_x, new_y) and \
                        distances[new_x][new_y] == -1:
                    distances[new_x][new_y] = distances[x][y] + 1
                    queue.append((new_x, new_y))
        self.distances = distances

    def output_distances(self) -> None:
        """ Print the distances to console as matrix"""
        for x in range(self.rows):
            for y in range(self.columns):
                print(self.distances[x][y], end=" ")
            print()


class BoardWidget(QWidget):
    def __init__(self, columns: int, rows: int, obstacles: int):
        super().__init__()
        self.columns = columns
        self.rows = rows
        self.obstacles = obstacles
        self.playing_board = Board(columns, rows, obstacles)
        self.cell_size = 20
        self.horizontal_padding = 150
        self.vertical_padding = 20
        self.setFixedSize((columns * self.cell_size) + self.horizontal_padding, (rows * self.cell_size) + self.vertical_padding)

    def paintEvent(self, event):
        """Handles the painting of the grid on the widget"""
        qp = QPainter()

        qp.begin(self)
        for x in range(self.rows):
            for y in range(self.columns):
                if self.playing_board.is_obstacle(x, y):
                    qp.setBrush(QColor(0, 0, 0))
                    qp.setPen(QColor(255, 255, 255))
                else:
                    distance = self.playing_board.distances[x][y]
                    qp.setBrush(QColor(255, 255, 255))
                    shift_horiz = 90
                    shift_vert = 10
                    qp.drawRect(y * self.cell_size + shift_horiz, x * self.cell_size + shift_vert, self.cell_size, self.cell_size)
                    if (x, y) == self.playing_board.start:
                        qp.setPen(QColor(0, 0, 0))
                        qp.drawText(QRectF(y * self.cell_size + shift_horiz, x * self.cell_size + shift_vert, self.cell_size, self.cell_size),
                                    QtCore.Qt.AlignmentFlag.AlignCenter,
                                    "S")
                    elif (x, y) == self.playing_board.end:
                        qp.setPen(QColor(0, 0, 0))
                        qp.drawText(QRectF(y * self.cell_size + shift_horiz, x * self.cell_size + shift_vert, self.cell_size, self.cell_size),
                                    QtCore.Qt.AlignmentFlag.AlignCenter,
                                    "E")
                    elif distance != -1:
                        qp.setPen(QColor(255, 0, 0))
                        qp.drawText(QRectF(y * self.cell_size + shift_horiz, x * self.cell_size + shift_vert, self.cell_size, self.cell_size),
                                    QtCore.Qt.AlignmentFlag.AlignCenter,
                                    str(distance))
        qp.end()

    def update_board(self):
        """ Updates the board based on running a new iteration of the algorithm"""
        self.playing_board.run_algorithm()
        self.update()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.remove = None
        self.board_widget = None
        self.counter = 0
        self.min_w = 400
        self.min_h = 400
        self.setWindowTitle("GrassFire Simulation")
        self.setMinimumSize(self.min_w, self.min_h)

        layout = QVBoxLayout()

        width_layout = QHBoxLayout()
        width_layout.addWidget(QLabel("Width:"))
        self.width = QLineEdit()
        self.width.setText("10")
        width_layout.addWidget(self.width)
        layout.addLayout(width_layout)

        height_layout = QHBoxLayout()
        height_layout.addWidget(QLabel("Height:"))
        self.height = QLineEdit()
        self.height.setText("10")
        height_layout.addWidget(self.height)
        layout.addLayout(height_layout)

        obstacle_layout = QHBoxLayout()
        obstacle_layout.addWidget(QLabel("Obstacle Percentage:"))
        self.obstacle_percentage = QLineEdit()
        self.obstacle_percentage.setText("10")
        obstacle_layout.addWidget(self.obstacle_percentage)
        layout.addLayout(obstacle_layout)

        button_layout = QHBoxLayout()
        start_button = QPushButton("Start")
        start_button.clicked.connect(self.start_simulation)
        button_layout.addWidget(start_button)
        stop_button = QPushButton("Stop")
        stop_button.clicked.connect(self.stop_simulation)
        button_layout.addWidget(stop_button)
        layout.addLayout(button_layout)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def start_simulation(self):
        if self.counter != 0:
            self.remove.removeWidget(self.board_widget)
        width = int(self.width.text())
        height = int(self.height.text())
        obstacles = int(self.obstacle_percentage.text())
        if width < 8 or height < 8:
            raise ArgumentTypeError("Width and height must be greater than 8.")
        if obstacles < 0 or obstacles > 100:
            raise ArgumentTypeError("Obstacle percentage must be between 0 and 100.")
        self.board_widget = BoardWidget(width, height, obstacles)
        self.board_widget.update_board()
        layout = self.centralWidget().layout()
        self.remove = layout
        layout.insertWidget(0, self.board_widget)
        self.counter += 1

    def stop_simulation(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
