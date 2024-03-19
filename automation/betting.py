import os 
from config import BETTING_DATASET_DIR

def find_csv_files():
    csv_files = []
    for dirpath, dirnames, filenames in os.walk(BETTING_DATASET_DIR):
        for filename in filenames:
            if filename.endswith('.csv'):
                csv_files.append(os.path.join(dirpath, filename))
    return csv_files