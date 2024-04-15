from config import PAT_CONSOLE_EXE_DIRECTORY, OUTPUT_FILE_DIRECTORY
import subprocess
import os
import platform
import re
import time

def execute_pat():
    # print("Executing PAT")
    model_directory = os.path.join(".", "rendered_template.pcsp")
    
    command = f"{PAT_CONSOLE_EXE_DIRECTORY} -pcsp {model_directory} {OUTPUT_FILE_DIRECTORY}"
    
    if platform.system() == "Darwin":
        command = f"mono {command}"
    # print(command)
    child_process = subprocess.run(command.split(" "), check=True, capture_output=True)
    # print(child_process.stdout.decode("utf-8"))
    # print(child_process.stderr.decode("utf-8"))

def read_output_file():
    with open(OUTPUT_FILE_DIRECTORY, "r") as file:
        return file.read()

def delete_output_file():
    os.remove(OUTPUT_FILE_DIRECTORY)

def parse_output(output):
    pattern = r"F G (\w+) with prob.*?\[(-*\d+\.-*\d+),\s*(-*\d+\.-*\d+)\]"
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
        

