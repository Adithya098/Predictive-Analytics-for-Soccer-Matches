import os 
from config import BETTING_DATASET_DIR
from pathlib import Path
import pandas as pd

def find_csv_files():
    """
    Find all CSV files in the specified directory without checking subdirectories.

    :param directory: The directory to search for CSV files.
    :return: A list of paths to CSV files found in the directory.
    """
    csv_files = []
    for item in os.listdir(BETTING_DATASET_DIR):
        # Construct the full path to the item
        full_path = os.path.join(BETTING_DATASET_DIR, item)
        
        # Check if the item is a file and has a .csv extension
        if os.path.isfile(full_path) and item.endswith('.csv'):
            csv_files.append(full_path)
    
    return csv_files

def match_csv_files():
    original_probabilities_csv = dict()
    new_probabilities_csv = dict()
    bets = dict()
    
    for item in os.listdir(os.path.join(BETTING_DATASET_DIR, "original_probabilities")):
        full_path = os.path.join(BETTING_DATASET_DIR,"original_probabilities", item)
        
        # Check if the item is a file and has a .csv extension
        if os.path.isfile(full_path) and item.endswith('.csv'):
            original_probabilities_csv[Path(full_path).name] = full_path
    
    for item in os.listdir(os.path.join(BETTING_DATASET_DIR, "new_probabilities")):
        full_path = os.path.join(BETTING_DATASET_DIR,"new_probabilities", item)
        
        # Check if the item is a file and has a .csv extension
        if os.path.isfile(full_path) and item.endswith('.csv'):
            new_probabilities_csv[Path(full_path).name] = full_path

    for item in os.listdir(os.path.join(BETTING_DATASET_DIR, "bets")):
        full_path = os.path.join(BETTING_DATASET_DIR, "bets", item)
        
        # Check if the item is a file and has a .csv extension
        if os.path.isfile(full_path) and item.endswith('.csv'):
            bets[Path(full_path).name] = full_path

    for key in original_probabilities_csv.keys():
        original_csv = pd.read_csv(original_probabilities_csv[key])
        new_csv = pd.read_csv(new_probabilities_csv[key])
        bets_csv = pd.read_csv(bets[key])
        
        filtered_original_csv = original_csv[original_csv['match_url'].isin(new_csv['match_url'])]
        filtered_original_csv.to_csv(os.path.join(BETTING_DATASET_DIR, "filtered_original_probabilities", key), index=False)
        
        filtered_bets_csv = bets_csv[bets_csv['match_url'].isin(new_csv['match_url'])]
        filtered_bets_csv.to_csv(os.path.join(BETTING_DATASET_DIR, "filtered_bets", key), index=False)
        

        
            

    
    
    
if __name__ == "__main__":
    match_csv_files()