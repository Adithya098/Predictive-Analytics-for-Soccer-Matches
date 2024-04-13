from pat import execute_pat, read_output_file, delete_output_file, parse_output
from crawl import send_request, find_teams
from betting import find_csv_files, match_csv_files
import pandas as pd
from db import DatabaseConnection
from pprint import pprint
from teams import find_most_similar
from tqdm import tqdm
from pcsp_generator import change_parameter, render, save_file, remove_render, initialize_params
from softmax import calculate_softmax
from probability import get_probability_file_name
from cli import get_parser
from config import SAMPLE_SIZE, RANDOM_SEED
from simulate import simulate_betting

def main():
    parser = get_parser()
    args = parser.parse_args()
    
    databaseConnection = DatabaseConnection()
    for csv_file in tqdm(find_csv_files(), desc="Processing CSVs"):
        probabilities_df = pd.DataFrame(columns=["match_url", "home_prob_softmax"])
        # read the csv file and parse the link
        df = pd.read_csv(csv_file)
        
        if args.sampling:
            df = df.sample(n=SAMPLE_SIZE, random_state=RANDOM_SEED)
        
        for _, row in tqdm(df.iterrows(), total=df.shape[0], desc="Processing rows", leave=False):
            
            request_success = False
            
            while request_success == False:
                try:
                    url = row['match_url']
                    request_success = True
                except Exception as e:
                    continue
            
            # find the teams
            soup = send_request(url)
            teams = find_teams(soup)
            
            home_team = teams["home_team"]
            attack_team = teams["attack_team"]
            
            # print(home_team, "->", find_most_similar(home_team))
            # print(attack_team, "->", find_most_similar(attack_team))

            # find the players corresponding to each team -> there is some inconsistency in team names
            home_team = find_most_similar(home_team)
            attack_team = find_most_similar(attack_team)
            
            
            home_team_players = databaseConnection.get_players_by_club(home_team)
            attack_team_players = databaseConnection.get_players_by_club(attack_team)
        
            initialize_params(home_team_players, attack_team_players)
            rendered_template = render(args.template)
            save_file(rendered_template)
            
            # execute pat
            execute_pat()
            output = read_output_file()

            
            delete_output_file()
            
            #remove render
            remove_render()
            
            # parse the output
            parsed_output = parse_output(output)
            print(parsed_output)
            
            softmax = calculate_softmax(parsed_output)
            
            probabilities_df = probabilities_df.append({"match_url": url, "home_prob_softmax": softmax}, ignore_index=True)
            
            # print(softmax)


        probabilities_df.to_csv(get_probability_file_name(csv_file), index=False)
        
    match_csv_files()
    
    seasons = [1516, 1617, 1718, 1819, 1920, 2021]
    for season in seasons:
        simulate_betting(season)
        
        
if __name__ == "__main__":
    main()