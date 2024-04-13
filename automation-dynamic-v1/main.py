import pandas as pd
from pprint import pprint
from tqdm import tqdm
from betting import find_csv_files, match_csv_files
from config import BETTING_DATASET_DIR, MATCHES_DATASET_DIR, RATINGS_DATASET_DIR, SAMPLE_SIZE, RANDOM_SEED
from pcsp_generator import *
from pat import *
from softmax import *
from probability import get_probability_file_name
from cli import get_parser
from simulate import *

bettingCsvFiles = find_csv_files(BETTING_DATASET_DIR)
matchCsvFiles = find_csv_files(MATCHES_DATASET_DIR)
ratingCsvFiles = find_csv_files(RATINGS_DATASET_DIR)

def main():
  parser = get_parser()
  args = parser.parse_args()
  for bettingCsvPath, matchCsvPath, playerCsvPath in tqdm(zip(
    bettingCsvFiles,
    matchCsvFiles,
    ratingCsvFiles
  ), desc="Processing CSVs", total=len(bettingCsvFiles) ,leave=False):

    probabilities_df = pd.DataFrame(columns=["match_url", "home_prob_softmax"])
    dfBetting = pd.read_csv(bettingCsvPath)
    if args.sampling:
        dfBetting = dfBetting.sample(n=SAMPLE_SIZE, random_state=RANDOM_SEED)
        # dfBetting = dfBetting.head(SAMPLE_SIZE)

    dfPlayer = pd.read_csv(playerCsvPath)
    dfPlayer.fillna(0, inplace=True)
    dfMatch = pd.read_csv(matchCsvPath)
    dfMatch.fillna(0, inplace=True)

    for _, row in tqdm(dfBetting.iterrows(), total=dfBetting.shape[0], desc="Processing rows", leave=True):
      try:
        url = row['match_url']
        matchId = url.split("/")[-1]
        matchDetails = getMatchDetails(dfMatch, url)
        homeTeamDetails = matchDetails['home']
        awayTeamDetails = matchDetails['away']

        allPlayersInMatch = matchDetails["home"]["players"] + matchDetails["away"]["players"]
        playersDB = getPlayersDB(dfPlayer, allPlayersInMatch)

        # building params for HOME team pat model
        # ------
        homeTeamParams = getParamsTemplate()
        homeTeamFormationGrid = generate_pos(homeTeamDetails['formation'])
        homeTeamParams = updateFormationParams(homeTeamParams, homeTeamFormationGrid)

        homeTeamParams['homeTeamFreeKickRating'] = getBestFreeKickRating(playersDB, homeTeamDetails['players'])
        homeTeamParams['homeTeamPenaltyRating'] = getBestPenaltityRating(playersDB, homeTeamDetails['players'])
        homeTeamParams['awayTeamKeeperSaveRating'] = getGkRatingAbleToSave(playersDB, homeTeamDetails['formation'][4])

        homeTeamParams['homeGkCodeLine'] = getHomeTeamGkCodeLine(playersDB, homeTeamDetails['formation'][0])
        homeTeamParams['homeDefCodeLine'] = getHomeTeamDefCodeLine(playersDB, homeTeamDetails['formation'][1], awayTeamDetails['formation'][3])
        homeTeamParams['homeMidCodeLine'] = getHomeTeamMidCodeLine(playersDB, homeTeamDetails['formation'][2], awayTeamDetails['formation'][2])
        homeTeamParams['homeAttkCodeLine'] = getHomeTeamAttkCodeLine(playersDB, homeTeamDetails['formation'][3], awayTeamDetails['formation'][1])
        homeTeamParams['awayGkCodeLine'] = getAwayTeamGkCodeLine(playersDB, homeTeamDetails['formation'][4])
        # ------

        # building params for AWAY team pat model
        # ------
        awayTeamParams = getParamsTemplate()
        awayTeamformationGrid = generate_pos(awayTeamDetails['formation'])
        awayTeamParams = updateFormationParams(awayTeamParams, awayTeamformationGrid)

        awayTeamParams['homeTeamFreeKickRating'] = getBestFreeKickRating(playersDB, awayTeamDetails['players'])
        awayTeamParams['homeTeamPenaltyRating'] = getBestPenaltityRating(playersDB, awayTeamDetails['players'])
        awayTeamParams['awayTeamKeeperSaveRating'] = getGkRatingAbleToSave(playersDB, awayTeamDetails['formation'][4])

        awayTeamParams['homeGkCodeLine'] = getHomeTeamGkCodeLine(playersDB, awayTeamDetails['formation'][0])
        awayTeamParams['homeDefCodeLine'] = getHomeTeamDefCodeLine(playersDB, awayTeamDetails['formation'][1], homeTeamDetails['formation'][3])
        awayTeamParams['homeMidCodeLine'] = getHomeTeamMidCodeLine(playersDB, awayTeamDetails['formation'][2], homeTeamDetails['formation'][2])
        awayTeamParams['homeAttkCodeLine'] = getHomeTeamAttkCodeLine(playersDB, awayTeamDetails['formation'][3], homeTeamDetails['formation'][1])
        awayTeamParams['awayGkCodeLine'] = getAwayTeamGkCodeLine(playersDB, awayTeamDetails['formation'][4])
        # ------

        # print("\n awayTeamParams >>", awayTeamParams)
        templateFile = args.template
        homeSoftmaxValue = calculateSoftmaxOfHomeTeam(matchId, templateFile, homeTeamParams, awayTeamParams)
        
        new_probability = pd.DataFrame({"match_url": [url], "home_prob_softmax": [homeSoftmaxValue]})
        probabilities_df = pd.concat([probabilities_df, new_probability], ignore_index=True)


      except Exception as e:
        print("\nERROR:", row)
        raise e
        continue
        
    probabilities_df.to_csv(get_probability_file_name(bettingCsvPath), index=False)
  seasons = [1516, 1617, 1718, 1819, 1920, 2021]
  for season in seasons:
      simulate_betting(season)
main()