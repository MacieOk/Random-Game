# **Random Games - Young Tableau and Jeu de Tacquin Simulation**

## **Table of Contents**
1. [Project Overview](#project-overview)
2. [Motivation and Purpose](#motivation-and-purpose)
3. [Features](#features)
4. [Installation](#installation)
5. [Usage](#usage)
    - [Generating a Young Tableau](#generating-a-young-tableau)
    - [Finding a Path Using Jeu de Tacquin](#finding-a-path-using-jeu-de-tacquin)
    - [Generating an HTML Report](#generating-an-html-report)
6. [Publication](#publication)
7. [License](#license)

## **Project Overview**
This project provides a Python library for generating and analyzing Young tableaux, as well as simulating the Jeu de Tacquin game. The library allows users to create a Young tableau from a list of random numbers, find optimal paths within the tableau using a predefined algorithm, and generate visualizations and reports based on the results.

## **Motivation and Purpose**
The motivation behind this project is to provide a toolset for researchers and enthusiasts interested in combinatorial mathematics and algorithmic game theory. The algorithms implemented in this project can be applied to analyze complex structures like Young tableaux, which have applications in various mathematical and computational fields.

## **Features**
- **Generate Young Tableau:** Easily create a Young tableau from random or specific sequences of numbers.
- **Simulate Jeu de Tacquin:** Find the optimal path in a Young tableau by simulating the Jeu de Tacquin game.
- **Visualization:** Generate visual representations of Young tableaux with highlighted paths.
- **Report Generation:** Automatically generate detailed HTML reports that include analysis and visualizations.

## **Installation**
To install the library, you can clone the repository and install it locally using `pip`:

```bash
git clone https://github.com/your-username/random_games.git
cd random_games
pip install -e . ```

## **Usage**

import numpy as np
from random_games.tableau_manager import TableauManager

random_numbers = np.random.randint(1, 10, size=100)
tableau_manager = TableauManager(random_numbers)
young_tableau = tableau_manager.insertion_tableau

for row in young_tableau:
    print(row)


## **Publication**
The results derived from the code in this project were used in a scientific publication. You can find the full paper here: https://arxiv.org/abs/2302.03762
