import numpy as np

class LargeDeviationAnalyzer:
    def __init__(self, results):

        """
        Initializes the LargeDeviationAnalyzer with simulation results.
        :param results: List of tuples containing (start_value, i_j_difference).
        """

        self.results = results
        self.i_j_differences = [result[1] for result in results]

    def estimate_large_deviation_probabilities(self, threshold)->float:

        """
        Estimates the probability of large deviations above a certain threshold.
        :param threshold: The threshold for large deviations.
        :return: Estimated probability of large deviations.
        """

        large_deviations = [diff for diff in self.i_j_differences if abs(diff) >= threshold]
        probability = len(large_deviations) / len(self.i_j_differences)
        return probability

    def analyze_tail_behavior(self)->tuple:

        """
        Analyzes the tail behavior of the i-j difference distribution.
        :return: Tail behavior statistics.
        """

        sorted_differences = sorted(self.i_j_differences)
        tail_size = int(0.05 * len(sorted_differences))  # 5% największych różnic
        tail = sorted_differences[-tail_size:]
        return np.mean(tail), np.var(tail)

    def find_extreme_events(self, threshold)->list:

        """
        Finds and returns extreme events where i-j differences exceed the threshold.
        :param threshold: The threshold for identifying extreme events.
        :return: List of extreme events.
        """

        extreme_events = [result for result in self.results if abs(result[1]) >= threshold]
        return extreme_events


