import os

# update these absolute paths according to ur system

# ------
# absolute path of PAT3.Console.exe file
# if windows
PAT_CONSOLE_EXE_DIRECTORY = "C:\\Program Files\\Process Analysis Toolkit\\Process Analysis Toolkit 3.5.1\\PAT3.Console-2.exe"
# if linus/mac
# PAT_CONSOLE_EXE_DIRECTORY = "/Users/alperen/Downloads/PAT_351/PAT3.Console-2.exe"
# ------

# ------
# absolute path of this automation folder
# if windows
OUTPUT_DIRECTORY = "C:\\Users\\adith\\Desktop\\CS5232-Project\\automation-dynamic-v1"
# if linus/mac
# OUTPUT_FILE_DIRECTORY = "/Users/alperen/Projects/CS5232-Project/automation-dynamic-v1"
# ------

# ----
BETTING_SIMULATION_DIR = os.path.join(".", "betting_simulation")
BETTING_DATASET_DIR = os.path.join(".", "betting_simulation", "betting_dataset")
MATCHES_DATASET_DIR = os.path.join(".", "Datasets", "matches")
RATINGS_DATASET_DIR = os.path.join(".", "Datasets", "ratings")
TEMPLATE_FILE = os.path.join(".", "template.txt")
SAMPLE_SIZE = 30
RANDOM_SEED = 42
