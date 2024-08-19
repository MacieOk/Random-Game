import numpy as np
from random_games.tableau_manager import TableauManager
from random_games.game_logic import JeuDeTacquin
from random_games.random_list_generator import RandomListGenerator

def main():

    # Set parameters
    word_length = 100
    initial_value = 0.5

    random_word = RandomListGenerator(word_length, initial_value).generate_list()

    # Young tableau initialization
    tableau_manager = TableauManager(random_word)
    young_tableau = tableau_manager.insertion_tableau

    #Print Young tableau
    print("Young tableau:")
    for row in young_tableau:
        print(row)

    # JeuDeTacquin initialization
    jeu = JeuDeTacquin(random_word)

    # Find path in Young tableau
    path = jeu.find_path(young_tableau)
    print("Path is found:", path)

    # Draw Young tableau with path
    jeu.draw_young_table_with_path(young_tableau, "example_path")

    # Save path to file
    jeu.save_path_to_file(path, "path.pkl")

    # Read path from file
    loaded_path = jeu.read_path_from_file("path.pkl")
    print("Path:", loaded_path)

if __name__ == "__main__":
    main()

