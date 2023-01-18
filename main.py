import argparse
from classes import *


def validate_board_size(value: str) -> int:
    """
    Validator for input of cmd-line arguments, as size should be greater than 8 x 8
    :param value: string input from cmd-line
    :return: integer value of the input, if it's greater than 8
    :raises: ArgumentTypeError if value is less than 8
    """
    int_val = int(value)
    if int_val < 8:
        raise argparse.ArgumentTypeError("%s is an invalid value. It must be greater than 8." % value)
    return int_val


def main(args: argparse.Namespace) -> None:
    """
    The main function of the program
    :param args: parsed command-line arguments
    """
    playing_board = Board.Board(args.columns, args.rows, args.obstacles)
    playing_board.run_simulation()
    playing_board.output_map()
    playing_board.output_distances()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-c', '--columns', help='Define the columns you want the grid to have', default=10,
                        type=validate_board_size)
    parser.add_argument('-r', '--rows', help='Define the rows you want the grid to have', default=10,
                        type=validate_board_size)
    parser.add_argument('-o', '--obstacles', help='Define the level of complexity you want the grid to have, %',
                        default=10)

    args = parser.parse_args()

    main(args)
