import numpy as np
import matplotlib.pyplot as plt

class ConvergenceAnalyzer:
    def __init__(self, results):

        """
        Initializes the ConvergenceAnalyzer with simulation results.
        :param results: List of tuples containing (start_value, i_j_difference).
        """

        self.results = results
        self.i_j_differences = [result[1] for result in results]
        self.lengths = list(range(1, len(self.results) + 1))

    def analyze_convergence_rate(self):

        """
        Analyzes the convergence rate of the i-j difference.
        :return: Convergence rate statistics.
        """

        convergence_rate = [abs(self.i_j_differences[i] - self.i_j_differences[i - 1])
                            for i in range(1, len(self.i_j_differences))]
        return np.mean(convergence_rate), np.var(convergence_rate)

    def plot_convergence(self):

        """
        Plots the convergence of i-j differences over the length of the words.
        """

        plt.figure(figsize=(10, 6))
        plt.plot(self.lengths, self.i_j_differences, marker='o')
        plt.title("Convergence of i-j Differences")
        plt.xlabel("Length of Random Words")
        plt.ylabel("i-j Difference")
        plt.grid(True)
        plt.show()


