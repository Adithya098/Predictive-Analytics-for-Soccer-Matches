import pandas as pd
import sqlite3
from tqdm import tqdm

connection = sqlite3.connect('my_database.db')

df = pd.read_csv('dataset/male_players.csv') 
print("read the dataset")

chunksize = 100000  
for start in tqdm(range(0, len(df), chunksize)):
    df.iloc[start:start+chunksize].to_sql('my_table', con=connection, if_exists='append', index=False)