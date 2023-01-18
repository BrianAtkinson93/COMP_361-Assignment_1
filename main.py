import argparse
from classes.Board import Board


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
    playing_board = Board(args.columns, args.rows, args.obstacles)
    playing_board.run_simulation()
    playing_board.output_map()
    playing_board.output_distances()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=f'GrassFire Simulation requires columns & rows from user')

    parser.add_argument('columns', help='Please provide how many columns you would like <int>', type=int,
                        default=10)
    parser.add_argument('rows', help='Please provide how many rows you would like <int>', type=int,
                        default=10)
    parser.add_argument('-o', '--obstacles',
                        help='define the percentage of obstacles you would like to populate the grid with <int> (0-100)',
                        required=False, default=10, type=int)

    args = parser.parse_args()

    main(args)
