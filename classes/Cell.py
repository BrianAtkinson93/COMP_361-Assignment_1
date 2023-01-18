class Cell:

    def __init__(self, x: int, y: int, is_obstacle: bool = False, distance: int = -1):
        """
        Initialize a new Cell object with the given x and y coordinates.

        :param x: The x-coordinate of the cell.
        :type x: int

        :param y: The y-coordinate of the cell.
        :type y: int

        :param is_obstacle: Whether the cell is an obstacle or not - Defaults to False.
        :type is_obstacle: bool

        :param distance: The distance of the cell from the starting point. Defaults to -1.
        :type distance: int
        """
        self.x = x
        self.y = y
        self.is_obstacle = is_obstacle
        self.distance = distance
