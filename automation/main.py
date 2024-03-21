from pat import execute_pat, read_output_file, delete_output_file, parse_output
from crawl import send_request, find_teams
from betting import find_csv_files
import pandas as pd
from db import DatabaseConnection
from pprint import pprint
from teams import find_most_similar
from tqdm import tqdm
from pcsp_generator import change_parameter, render, save_file, remove_render, initialize_params
from softmax import calculate_softmax
from probability import get_probability_file_name

def main():
    databaseConnection = DatabaseConnection()
    for csv_file in find_csv_files():
        probabilities_df = pd.DataFrame(columns=["match_url", "home_prob_softmax"])
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

            home_team_players = databaseConnection.get_players_by_club(home_team)
            attack_team_players = databaseConnection.get_players_by_club(attack_team)
        
            # generate pcsp file : TODO: correctly match parameters
            initialize_params()
            rendered_template = render()
            save_file(rendered_template)
            
            # execute pat
            execute_pat()
            output = read_output_file()
            
            
            delete_output_file()
            
            #remove render
            remove_render()
            
            # parse the output
            parsed_output = parse_output(output)
            
            softmax = calculate_softmax(parsed_output)
            
            # output the result to the excel file : TODO
            probabilities_df = probabilities_df.append({"match_url": url, "home_prob_softmax": softmax}, ignore_index=True)

        probabilities_df.to_csv(get_probability_file_name(csv_file), index=False)
if __name__ == "__main__":
    main()