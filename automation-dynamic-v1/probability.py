
import os
from config import BETTING_SIMULATION_DIR


def get_probability_file_name(csv_file_name):
    # Create a csv file with the following columns:
    # match_url, home_team, attack_team, home_team_players, attack_team_players, output
    file_name = os.path.split(csv_file_name)[-1]
    name, _ = os.path.splitext(file_name)
    
    return os.path.join(BETTING_SIMULATION_DIR, "new_probabilities", f"{name}.csv")
    

