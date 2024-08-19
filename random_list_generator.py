import numpy as np
import random
class RandomListGenerator:
    def __init__(self, length: int, initial_value: float):

        """
        Initializes RandomListGenerator with length and initial_value.

        :param length: Length of generated list.
        :param initial_value: Initial value of generated list.
        """

        self.length = length
        self.initial_value = initial_value

    def generate_list(self)-> np.array:

        """
        Generates a list of random numbers.

        :return: Numpy array of random numbers.
        """

        random_array = np.array(self.initial_value)

        for _ in range(self.length):
            random_value = random.uniform(0, 1)
            random_array = np.append(random_array, random_value)

        return random_array

    def save_to_file(self, filename: str)-> None:

        """
        Saves generated list to a file.

        :param filename: Name of the file.
        """

        random_list = self.generate_list()
        with open(filename, 'wb') as file:
            pickle.dump(random_list, file)

    @staticmethod
    def read_from_file(filename: str)-> np.array:

        """
        Reads a list from a file.

        :param filename: Name of the file.
        :return: Numpy array of random numbers.
        """

        with open(filename, 'rb') as file:
            random_list = pickle.load(file)
        return random_list
