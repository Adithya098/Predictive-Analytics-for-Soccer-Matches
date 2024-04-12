import subprocess
import os

def run_sampling_experiment(template_file : str = "template.txt"):
    subprocess.run(f"python main.py -s -t {template_file}", shell=True)

def run_whole_experiment(template_file : str = "template.txt"):
    subprocess.run(f"python main.py -t {template_file}", shell=True)
    
def main():
    sampling_models = [
        os.path.join("isolated_feature_templates", "Improved_soccer_model_f2_gridExpansion.txt.txt"), 
        os.path.join("isolated_feature_templates", "Improved_soccer_model_f2_gridExpansion.txt"), 
        os.path.join("isolated_feature_templates", "Improved_soccer_model_f1_penalty.txt")
        ]
    
    print("running experiments for isolated features")
    for model in sampling_models:
        run_sampling_experiment(model)
    
    print("running experiment for complete model")
    run_whole_experiment()

if __name__ == "__main__":
    main()