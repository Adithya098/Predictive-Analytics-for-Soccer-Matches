from jinja2 import Template
import os
from config import TEMPLATE_FILE

def getParamsTemplate():
   return {
      "formationAttGK": "",
      "formationAttDL": "",
      "formationAttML": "",
      "formationAttFL": "",
      "formationDefGK": "",
      "homeTeamFreeKickRating" : 0,
      "homeTeamPenaltyRating" : 0,
      "awayTeamKeeperSaveRating" : 0,
      "homeGkCodeLine": "",
      "homeDefCodeLine": "",
      "homeMidCodeLine": "",
      "homeAttkCodeLine": "",
      "awayGkCodeLine": "",
  }

def save_file(rendered_template, fileName):
    with open(os.path.join(".", f'{fileName}.pcsp'), "w") as file:
        file.write(rendered_template)

def renderNSave(templateFile, parameters, fileName):
    with open(os.path.join(".", templateFile), "r") as file:
        template_str = file.read()
        
    template = Template(template_str)
    rendered_template = template.render(parameters)
    save_file(rendered_template, fileName)

def remove_render(fileName):
    os.remove(os.path.join(".", f'{fileName}.pcsp'))

def getPlayerDetails(dfrating, playerFifaId):
  # Find the row where the 'sofifa_id' column matches 'playerFifaId'
  player_data = dfrating.loc[dfrating['sofifa_id'] == playerFifaId]

  # If the player is found in the DataFrame, create a dictionary from the row
  if not player_data.empty:
    # The 'to_dict' function can be used to convert the row to a dictionary
    # 'orient=records' returns a list of dictionaries
    # We extract the first element of the list since there will only be one match
    player_dict = player_data.iloc[:, 1:].to_dict(orient='records')[0]
    return player_dict
  else:
    # If the player is not found, return None or an empty dictionary
    return None

def getTeamDetails(match_row, isHome):

  homeOrAway = "home" if(isHome) else "away"
  reverse = "away" if(isHome) else "home"

  # Get the home formation, fifaids, and sequence for the match
  team_formation = match_row[f'{homeOrAway}_formation'].iloc[0]
  team_fifaids = match_row[f'{homeOrAway}_xi_sofifa_ids'].iloc[0]  # Assuming home fifaids are in this column
  team_sequence = match_row[f'{homeOrAway}_sequence'].iloc[0]  # Assuming home positions are in this column

  # Adjust the formation
  parts = list(map(int, team_formation.split('-')))
  parts = [x for x in parts if x != 0]
  if len(parts) > 3:
      middle_sum = sum(parts[1:-1])
      adjusted_parts = [parts[0], middle_sum, parts[-1]]
  else:
      adjusted_parts = parts

  # Group the sequence according to the adjusted formation
  fifaid_parts = [int(float(id)) for id in team_fifaids.split(',')]
  location_parts = team_sequence.split(',')

  # Pair the goalkeeper's fifaid and position
  teamgoalkeeper = [(location_parts[0], fifaid_parts[0])]
  oppteamgoalkeeper=[('C', int(float(match_row[f'{reverse}_xi_sofifa_ids'].iloc[0].split(',')[0])))]
  # Process outfield players
  outfield_players_fifaid = fifaid_parts[1:]
  outfield_players_sequence = location_parts[1:]  # Omit the goalkeeper
  grouped_sequence1 = [teamgoalkeeper]  # Start with the goalkeeper's position and fifaid

  start = 0
  for count in adjusted_parts:
      # Create a list of tuples (position, fifaid) for the current group
      current_group = [(position, fifaid) for position, fifaid in zip(outfield_players_sequence[start:start+count], outfield_players_fifaid[start:start+count])]
      grouped_sequence1.append(current_group)
      start += count
  grouped_sequence1.append(oppteamgoalkeeper)
  return (grouped_sequence1, fifaid_parts)

def getMatchDetails(df, match_url):

    # Find the match row by URL
    match_row = df.loc[df['match_url'] == match_url]

    # Check if the match row exists
    if not match_row.empty:
        # Call the subfunction to get the grouped sequence for home team
        home_grouped_sequence, home_players = getTeamDetails(match_row, True)
        away_grouped_sequence, away_players = getTeamDetails(match_row, False)

        # You could do similar for the away team if you have the corresponding data
        # For example: away_grouped_sequence = away(match_row)

        # Return the grouped sequence wrapped in a dictionary under the 'home' key
        return {
            'home': {
              "formation": home_grouped_sequence,
              "players": home_players
            },
            'away':{
              "formation": away_grouped_sequence,
              "players": away_players
            }
          }

    raise KeyError("Match URL not found in the DataFrame")

def getPosIndex(posSym):
    index = 0
    if posSym == 'L':
        index = 0
    elif posSym == 'LR':
        index = 1
    elif posSym == 'CL':
        index = 2
    elif posSym == 'C':
        index = 3
    elif posSym == 'CR':
        index = 4
    elif posSym == 'RL':
        index = 5
    elif posSym == 'R':
        index = 6
    return index

def generate_pos(input_data):
    result = []
    for data in input_data:
        pos = [0] * 7
        positionSet = set()
        for val in data:
            positionSet.add(val[0])

        for sym in positionSet:
            posIndex = getPosIndex(sym)
            pos[posIndex] = 1
        result.append(pos)
    return result

def getSumOfSpecificRating(playersDB, gridLine, ratingKeyword):
  sumOfRatings = 0
  for pos in gridLine:
    playerId = pos[1]
    sumOfRatings += playersDB[playerId][ratingKeyword]
  return sumOfRatings

def getAvgGettingTackledRating(playersDB, teamGridLine):

  lineSize = len(teamGridLine)

  slidingTackle = getSumOfSpecificRating(playersDB, teamGridLine, "defending_sliding_tackle")
  standingTackle = getSumOfSpecificRating( playersDB, teamGridLine, "defending_standing_tackle")
  interception = getSumOfSpecificRating( playersDB, teamGridLine, "mentality_interceptions")
  gettingTackled = (slidingTackle + standingTackle + interception) / (lineSize * 3)
  return int(gettingTackled)

def getAvgGettingFouledRating(playersDB, teamGridLine):

  lineSize = len(teamGridLine)

  sumMentalityAggression = getSumOfSpecificRating(playersDB, teamGridLine, "mentality_aggression")
  sumMentalityComposure = getSumOfSpecificRating( playersDB, teamGridLine, "mentality_composure")
  gettingFoulRating = sumMentalityComposure if(sumMentalityComposure != 0) else sumMentalityAggression
  gettingFoulRating = gettingFoulRating/lineSize
  return int(gettingFoulRating)

def convertFormationLineIntoPatCode(actionName, formationLine):
  formationCodeLine = ""
  for position in formationLine:
    posSym, posVals = position
    posVals = ", ".join(map(str, posVals))
    formationCodeLine += f"[pos[{posSym}] == 1]{actionName}({posVals},{posSym}) [] "
  return formationCodeLine[:-4]

def getHomeTeamGkCodeLine(playersDB, homeTeamGkLine):
  lineDetails = []
  for player in homeTeamGkLine:
    fifaId = player[1]
    gkHandling = int(playersDB[fifaId]["goalkeeping_handling"])
    gkKicking = int(playersDB[fifaId]["goalkeeping_kicking"])

    ratings = [gkHandling, gkKicking]
    lineDetails.append((player[0], ratings))
  return convertFormationLineIntoPatCode("Kep_1", lineDetails)

def getHomeTeamDefCodeLine(playersDB, homeTeamDefLine, awayTeamAttkLine):

  lineDetails = []

  gettingTackled = getAvgGettingTackledRating(playersDB, awayTeamAttkLine)
  gettingFoulRating = getAvgGettingFouledRating(playersDB, awayTeamAttkLine)

  for player in homeTeamDefLine:
    fifaId = player[1]
    shortPassing = int(playersDB[fifaId]["attacking_short_passing"])
    longPassing = int(playersDB[fifaId]["skill_long_passing"])
    ratings = [shortPassing, longPassing, gettingTackled, gettingFoulRating]
    lineDetails.append((player[0], ratings))
  return convertFormationLineIntoPatCode("Def", lineDetails)

def getHomeTeamMidCodeLine(playersDB, homeTeamMidLine, awayTeamMidLine):

  lineDetails = []

  gettingTackled = getAvgGettingTackledRating(playersDB, awayTeamMidLine)
  gettingFoulRating = getAvgGettingFouledRating(playersDB, awayTeamMidLine)

  for player in homeTeamMidLine:
    fifaId = player[1]
    shortPassing = int(playersDB[fifaId]["attacking_short_passing"])
    longPassing = int(playersDB[fifaId]["skill_long_passing"])
    longShot = int(playersDB[fifaId]["power_long_shots"])
    ratings = [shortPassing, longPassing, longShot, gettingTackled, gettingFoulRating]
    lineDetails.append((player[0], ratings))
  return convertFormationLineIntoPatCode("Mid", lineDetails)

def getHomeTeamAttkCodeLine(playersDB, homeTeamAttkLine, awayTeamDefLine):

  lineDetails = []
  gettingTackled = getAvgGettingTackledRating(playersDB, awayTeamDefLine)
  gettingFoulRating = getAvgGettingFouledRating(playersDB, awayTeamDefLine)

  for player in homeTeamAttkLine:
    fifaId = player[1]
    shortPassing = int(playersDB[fifaId]["attacking_short_passing"])
    longPassing = int(playersDB[fifaId]["skill_long_passing"])
    finishing = int(playersDB[fifaId]["attacking_finishing"])
    longShot = int(playersDB[fifaId]["power_long_shots"])
    volley = int(playersDB[fifaId]["attacking_volleys"])
    heading = int(playersDB[fifaId]["attacking_heading_accuracy"])
    ratings = [
        shortPassing,
        longPassing,
        finishing,
        longShot,
        volley,
        heading,
        gettingTackled,
        gettingFoulRating
      ]
    lineDetails.append((player[0], ratings))
  return convertFormationLineIntoPatCode("For", lineDetails)

def getAwayTeamGkCodeLine(playersDB, awayTeamGkLine):

  lineDetails = []
  for player in awayTeamGkLine:
    fifaId = player[1]
    gkOverallRating = int(playersDB[fifaId]["overall"])
    ratings = [gkOverallRating]
    lineDetails.append((player[0], ratings))
  return convertFormationLineIntoPatCode("Kep_2", lineDetails)

def getGkRatingAbleToSave(playersDB, awayTeamGkLine):
  fifaId = awayTeamGkLine[0][1]

  gkDiving = playersDB[fifaId]["goalkeeping_diving"]
  gkReflexes = playersDB[fifaId]["goalkeeping_reflexes"]

  gkAbleToSave = (gkDiving + gkReflexes)/2

  return int(gkAbleToSave)

def getBestFreeKickRating(playersDB, playerIds):
  freeKickRating = 0
  for fifaId in playerIds:
    freeKickRating = max(freeKickRating, playersDB[fifaId]["skill_fk_accuracy"])
  return int(freeKickRating)

def getBestPenaltityRating(playersDB, playerIds):
  penaltyRating = 0
  for fifaId in playerIds:
    penaltyRating = max(penaltyRating, playersDB[fifaId]["mentality_penalties"])
  return int(penaltyRating)

def getPlayersDB(dfPlayer, playerIds):
  playersDB = {}
  for fifaId in playerIds:
    playersDB[fifaId] = getPlayerDetails(dfPlayer, fifaId)
  return playersDB

def updateFormationParams(params, grid):
  formationLines = ["formationAttGK", "formationAttDL", "formationAttML", "formationAttFL", "formationDefGK"]
  for formationLine, gridLine in zip(formationLines, grid):
    params[formationLine] = ", ".join(map(str, gridLine))
  return params
