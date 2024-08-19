import numpy as np
from bisect import bisect
import pickle
import matplotlib.pyplot as plt


class TableauManager:
    def __init__(self, random_numbers: np.array):

        """
        Initializes TableauManager with random_numbers.
        :param random_numbers: Numpy array of random numbers.
        """

        self.random_numbers = random_numbers
    @property
    def insertion_tableau(self) -> list:

        """
        Generates a Young tableau using the InsertionTableau algorithm.
        :return: Young tableau as a list of lists.
        """

        Young = []

        def insert(m):
            for r in range(len(Young)):
                if m > Young[r][-1]:
                    Young[r].append(m)
                    return

                c = bisect(Young[r], m)

                if c >= len(Young[r]):
                    Young[r].append(m)
                    return

                Young[r][c], m = m, Young[r][c]

            Young.append([m])

        for number in self.random_numbers:
            insert(float(number))

        return Young
    @property
    def recording_tableau(self) -> list:

        """
        Generates a tableau recording the insertion order of elements.
        :return: Tableau recording the insertion order as a list of lists.
        """

        Young = []
        Insertion = []

        def insert(m, n):
            for r in range(len(Young)):
                if m > Young[r][-1]:
                    Young[r].append(m)
                    Insertion[r].append(n)
                    return
                c = bisect(Young[r], m)
                Young[r][c], m = m, Young[r][c]
            Young.append([m])
            Insertion.append([n])

        for i, number in enumerate(self.random_numbers):
            insert(float(number), i + 1)

        return Insertion

    def save_to_file(self, file_path: str) -> None:

        """
        Saves the Young tableau to a binary file.
        :param file_path: Path to the file where the tableau should be saved.
        """

        tableau = self.insertion_tableau()
        with open(file_path, 'wb') as file:
            pickle.dump(tableau, file)

    @staticmethod
    def read_from_file(file_path: str) -> list:

        """
        Reads a Young tableau from a binary file.
        :param file_path: Path to the file where the tableau is stored.
        :return: Young tableau as a list of lists.
        """

        with open(file_path, 'rb') as file:
            tableau = pickle.load(file)
        return tableau

    def draw_young_table(self, tableau: list, picture_name: str, path: list = None) -> None:

        """
        Draws the Young tableau with optional highlighting of a path.
        :param tableau: Young tableau as a list of lists.
        :param picture_name: Name of the output image file.
        :param path: List of tuples representing the path to highlight.
        """

        fig, ax = plt.subplots()
        ax.set_aspect('equal')

        square_size = 1
        margin_top = 0.5
        max_values = 100
        drawn_values = 0

        for i, row in enumerate(tableau):
            for j, value in enumerate(row):
                if drawn_values < max_values:
                    if path and (i, j) in path:
                        facecolor = 'red'
                    else:
                        facecolor = 'white'

                    plt.text(
                        j * square_size + square_size / 2,
                        -i * square_size + square_size / 2 - margin_top,
                        f'{value:.3f}',
                        ha='center',
                        va='center',
                        fontsize=square_size * 8
                    )
                    drawn_values += 1
                else:
                    facecolor = 'white'

                rect = plt.Rectangle(
                    (j * square_size, -i * square_size - margin_top),
                    square_size,
                    square_size,
                    fill=True,
                    facecolor=facecolor,
                    edgecolor='black'
                )
                ax.add_patch(rect)

        ax.set_xlim(0, max(len(row) for row in tableau) * square_size)
        ax.set_ylim(-len(tableau) * square_size - margin_top, margin_top)
        plt.axis('off')

        plt.savefig(f"{picture_name}.png", dpi=300, bbox_inches='tight', pad_inches=0)
        plt.show()


