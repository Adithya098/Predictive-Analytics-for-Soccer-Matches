from pat import execute_pat, read_output_file, delete_output_file, parse_output
from crawl import send_request, find_teams
from betting import find_csv_files
import pandas as pd
from db import DatabaseConnection
from pprint import pprint
from teams import find_most_similar
from tqdm import tqdm

def main():
    databaseConnection = DatabaseConnection()
    for csv_file in find_csv_files():
        # read the csv file and parse the link
        df = pd.read_csv(csv_file)
        for _, row in df.iterrows():
            url = row['match_url']
            
            # find the teams
            soup = send_request(url)
            teams = find_teams(soup)
            
            home_team = teams["home_team"]
            attack_team = teams["attack_team"]
            
            print(home_team, "->", find_most_similar(home_team))
            print(attack_team, "->", find_most_similar(attack_team))

            # find the players corresponding to each team -> there is some inconsistency in team names

            # home_team_players = databaseConnection.get_players_by_club(home_team)
            # attack_team_players = databaseConnection.get_players_by_club(attack_team_players)
        
            


    # generate pcsp file : TODO
    # execute pat
    execute_pat()
    output = read_output_file()
    delete_output_file()
    
    # parse the output
    parse_output(output)
    # output the result to the excel file : TODO
    
if __name__ == "__main__":
    main()