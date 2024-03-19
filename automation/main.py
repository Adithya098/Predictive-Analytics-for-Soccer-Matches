from pat import execute_pat, read_output_file, delete_output_file, parse_output
from crawl import send_request, find_teams
from betting import find_csv_files
import pandas as pd
from db import DatabaseConnection

def main():

    for csv_file in find_csv_files():
        # read the csv file and parse the link
        df = pd.read_csv(csv_file)
        for _, row in df.iterrows():
            url = row['match_url']
            
            # find the teams
            soup = send_request(url)
            teams = find_teams(soup)
            print(teams)
            
            home_team = teams["home_team"]
            attack_team = teams["attack_team"]
            
            # find the players corresponding to each team -> there is some inconsistency in team names
            databaseConnection = DatabaseConnection()
            home_team_players = databaseConnection.get_players_by_club(home_team)
            attack_team_players = databaseConnection.get_players_by_club(attack_team_players)
        
            
            break #for now
    
    

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