from random_games.tableau_manager import TableauManager
import pickle

class JeuDeTacquin(TableauManager):
    def find_path(self, tableau):

        """
        Finds the path in the Young tableau by always choosing the maximum value
        between the element to the right and the element below the current one.
        :param tableau: Young tableau as a list of lists.
        :return: List of tuples representing the path.
        """

        path = []
        i, j = 0, 0
        path.append((i, j))

        while True:
            down = (i + 1, j) if i + 1 < len(tableau) else None
            right = (i, j + 1) if j + 1 < len(tableau[i]) else None

            if down and right:
                if j < len(tableau[down[0]]) and tableau[down[0]][j] >= tableau[i][right[1]]:
                    i, j = down
                elif j + 1 < len(tableau[i]):
                    i, j = right
                else:
                    break
            elif down and j < len(tableau[down[0]]):
                i, j = down
            elif right and j + 1 < len(tableau[i]):
                i, j = right
            else:
                break

            path.append((i, j))

        return path

    def draw_young_table_with_path(self, tableau, picture_name)->None:

        """
        Draws the Young tableau with the path.
        :param tableau: Young tableau as a list of lists.
        :param picture_name: Name of the picture file.
        """

        path = self.find_path(tableau)
        self.draw_young_table(tableau, picture_name, path)

    def save_path_to_file(self, path, file_path)->None:

        """
        Saves the path to a binary file.
        :param path: List of tuples representing the path.
        :param file_path: Path to the file where the path should be saved.
        """

        with open(file_path, 'wb') as file:
            pickle.dump(path, file)

    def read_path_from_file(self, file_path)->list:

        """
        Reads the path from a binary file.
        :param file_path: Path to the file where the path is stored.
        :return: List of tuples representing the path.
        """

        with open(file_path, 'rb') as file:
            path = pickle.load(file)
        return path

