from scipy.optimize import curve_fit
import numpy as np

class AsymptoticAnalyzer:
    def __init__(self, results):

        """
        Initializes the AsymptoticAnalyzer with simulation results.
        :param results: List of tuples containing (start_value, i_j_difference).
        """

        self.results = results
        self.start_values = [result[0] for result in results]
        self.i_j_differences = [result[1] for result in results]

    def fit_asymptotic_function(self, func):

        """
        Fits an asymptotic function to the results.
        :param func: The function to fit, e.g., lambda x, a, b: a * np.log(x) + b
        :return: Parameters of the fitted function.
        """

        popt, _ = curve_fit(func, self.start_values, self.i_j_differences)
        return popt

    def calculate_mean_and_variance(self):

        """
        Calculates the mean and variance of the i-j differences.
        :return: Mean and variance of i-j differences.
        """

        mean = np.mean(self.i_j_differences)
        variance = np.var(self.i_j_differences)
        return mean, variance

    def perform_regression_analysis(self):

        """
        Performs regression analysis on the data.
        :return: Coefficients of the regression model.
        """

        coefficients = np.polyfit(self.start_values, self.i_j_differences, 1)
        return coefficients

#Example of use:

