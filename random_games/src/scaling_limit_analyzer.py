import numpy as np

class ScalingLimitAnalyzer:
    def __init__(self, results: list):

        """
        Initializes the ScalingLimitAnalyzer with simulation results.
        :param results: List of tuples containing (start_value, i_j_difference).
        """

        self.results = results
        self.start_values = [result[0] for result in results]
        self.i_j_differences = [result[1] for result in results]

    def analyze_scaling_limits(self)->tuple:

        """
        Analyzes the scaling limits of i-j differences.
        :return: Scaling limit statistics.
        """

        scaling_factors = np.array(self.start_values) / np.max(self.start_values)
        scaled_i_j = np.array(self.i_j_differences) / np.max(self.i_j_differences)
        return scaling_factors, scaled_i_j

    def fit_scaling_law(self)->np.ndarray:

        """
        Fits a scaling law to the i-j differences.
        :return: Parameters of the scaling law.
        """

        scaling_factors, scaled_i_j = self.analyze_scaling_limits()
        coefficients = np.polyfit(scaling_factors, scaled_i_j, 1)
        return coefficients

