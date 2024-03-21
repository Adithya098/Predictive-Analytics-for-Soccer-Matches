import os 
from config import BETTING_DATASET_DIR

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
