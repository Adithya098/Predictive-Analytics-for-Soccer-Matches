from config import PAT_CONSOLE_EXE_DIRECTORY
import subprocess
import os
import platform
import re
import time
from pcsp_generator import renderNSave, remove_render
from softmax import *
import random

def execute_pat(fileName):
    # print("Executing PAT")
    model_directory = os.path.join(".", f'{fileName}.pcsp')
    output_directory = os.path.join(".", f'{fileName}.txt')
    
    command = f"{PAT_CONSOLE_EXE_DIRECTORY} -pcsp {model_directory} {output_directory} "
    
    if platform.system() == "Darwin":
        command = f"mono {command}"
        
    child_process = subprocess.run(command.split(" "), check=True, capture_output=True)
    # print(child_process.stdout.decode("utf-8"))

def read_output_file(fileName):
    output_directory = os.path.join(".", f'{fileName}.txt')
    with open(output_directory, "r") as file:
        return file.read()

def delete_output_file(fileName):
    output_directory = os.path.join(".", f'{fileName}.txt')
    os.remove(output_directory)

def parse_output(output):
    pattern =  r"F G (\w+) with prob.*?\[(\d+\.\d+),\s*(\d+\.\d+)\]"

    matches = re.findall(pattern, output)
    result = dict()
    # Processing all matches
    for match in matches:
        goal = match[0]
        prob_range = [float(match[1]), float(match[2])]
        # print("Goal:", goal)
        # print("Probability Range:", prob_range)
        # print()
        result[goal] = prob_range
    
    return result
        
def calculateSoftmaxOfHomeTeam(matchId, templateFile, homeTeamParams, awayTeamParams):

    homeTeamPcspFileName = f'homeTeamModel_{matchId}'
    awayTeamPcspFileName = f'awayTeamModel_{matchId}'
    renderNSave(templateFile, homeTeamParams, homeTeamPcspFileName)
    renderNSave(templateFile, awayTeamParams, awayTeamPcspFileName)

    execute_pat(homeTeamPcspFileName)
    execute_pat(awayTeamPcspFileName)

    homeTeamOutput = read_output_file(homeTeamPcspFileName)
    awayTeamOutput = read_output_file(awayTeamPcspFileName)

    parsedHomeTeamOutput = parse_output(homeTeamOutput)
    parsedAwayTeamOutput = parse_output(awayTeamOutput)

    softmaxValue = calculateSoftmax(parsedHomeTeamOutput, parsedAwayTeamOutput)
    home_softmaxValue = softmaxValue[0]

    #remove pcsp files
    remove_render(homeTeamPcspFileName)
    remove_render(awayTeamPcspFileName)

    delete_output_file(homeTeamPcspFileName)
    delete_output_file(awayTeamPcspFileName)

    return home_softmaxValue
