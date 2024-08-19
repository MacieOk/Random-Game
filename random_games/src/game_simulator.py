import csv
import numpy as np
import matplotlib.pyplot as plt
from random_games.game_logic import JeuDeTacquin
from random_games.random_list_generator import RandomListGenerator

class GameSimulator:
    def __init__(self, num_words, word_length):

        """
        Initializes the GameSimulator with the number of random words and the length of each word.
        :param num_words: Number of random words to generate.
        :param word_length: Length of each random word.
        """

        self.num_words = num_words
        self.word_length = word_length
        self.results = []

    def simulate(self)-> None:

        """
        Simulates the Jeu de Tacquin experiment for the specified number of random words.
        """

        for _ in range(self.num_words):
            random_generator = RandomListGenerator(self.word_length, np.random.rand())
            random_word = random_generator.generate_list()

            jeu_de_tacquin = JeuDeTacquin(random_word)
            tableau = jeu_de_tacquin.insertion_tableau()
            path = jeu_de_tacquin.find_path(tableau)

            start_value = random_word[0]
            i_j_difference = path[-1][0] - path[-1][1]

            self.results.append((start_value, i_j_difference))

    def save_results_to_csv(self, file_name)-> None:

        """
        Saves the results of the simulation to a CSV file.
        :param file_name: Name of the CSV file.
        """

        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Start Value", "i-j Difference"])
            writer.writerows(self.results)

    def plot_results(self)-> None:

        """
        Plots the dependency of i-j difference on the start value of the random word.
        """

        start_values = [result[0] for result in self.results]
        i_j_differences = [result[1] for result in self.results]

        plt.figure(figsize=(10, 6))
        plt.scatter(start_values, i_j_differences, color='blue')
        plt.title("Dependency of i-j Difference on Start Value")
        plt.xlabel("Start Value")
        plt.ylabel("i-j Difference")
        plt.grid(True)
        plt.show()

