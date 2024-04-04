from jinja2 import Template
import os

parameters = {
    'ShortPass_AtkKep' : 0,
    'LongPass_DefKep' : 0,
    'Mental_DefKep' : 0,
    'ShortPass_AtkDef_r' : 0,
    'LongPass_AtkDef_r' : 0,
    'BallLosePass_AtkDef_r' : 0,
    'Mental_AtkDef_r' : 0,
    'ShortPass_AtkDef_cr' : 0,
    'LongPass_AtkDef_cr' : 0,
    'BallLosePass_AtkDef_cr' : 0,
    'Mental_AtkDef_cr' : 0,
    'ShortPass_AtkDef_cl' : 0,
    'LongPass_AtkDef_cl' : 0,
    'BallLosePass_AtkDef_cl' : 0,
    'Mental_AtkDef_cl' : 0,
    'ShortPass_AtkDef_l' : 0,
    'LongPass_AtkDef_l' : 0,
    'BallLosePass_AtkDef_l' : 0,
    'Mental_AtkDef_l' : 0,
    'ShortPass_AtkMid_rl' : 0,
    'LongPass_AtkMid_rl' : 0,
    'LongShot_AtkMid_rl' : 0,
    'LoseBall_AtkMid_rl' : 0,
    'Mental_AtkMid_rl' : 0,
    'ShortPass_AtkMid_c' : 0,
    'LongPass_AtkMid_c' : 0,
    'LongShot_AtkMid_c' : 0,
    'LoseBall_AtkMid_c' : 0,
    'Mental_AtkMid_c' : 0,
    'ShortPass_AtkMid_lr' : 0,
    'LongPass_AtkMid_lr' : 0,
    'LongShot_AtkMid_lr' : 0,
    'LoseBall_AtkMid_lr' : 0,
    'Mental_AtkMid_lr' : 0,
    'Fin_AtkFor_RL' : 0,
    'LongShot_AtkFor_RL' : 0,
    'Volley_AtkFor_RL' : 0,
    'Heading_AtkFor_RL' : 0,
    'LoseBall_AtkFor_RL' : 0,
    'Mental_AtkFor_RL' : 0,
    'Fin_AtkFor_C' : 0,
    'LongShot_AtkFor_C' : 0,
    'Volley_AtkFor_C' : 0,
    'Heading_AtkFor_C' : 0,
    'LoseBall_AtkFor_C' : 0,
    'Mental_AtkFor_C' : 0,
    'Fin_AtkFor_LR' : 0,
    'LongShot_AtkFor_LR' : 0,
    'Volley_AtkFor_LR' : 0,
    'Heading_AtkFor_LR' : 0,
    'LoseBall_AtkFor_LR' : 0,
    'Mental_AtkFor_LR' : 0,
    'Save_DefKep' : 0,
    'Mental_DefKep' : 0,
    "ShortPass_AtkMidBwd_cl": 0, 
    "LongPass_AtkMidBwd_cl": 0, 
    "LongShot_AtkMidBwd_cl": 0, 
    "LoseBall_AtkMidBwd_cl": 0, 
    "Mental_AtkMidBwd_cl" : 0,
    "ShortPass_AtkMidBwd_cr": 0, 
    "LongPass_AtkMidBwd_cr": 0, 
    "LongShot_AtkMidBwd_cr": 0, 
    "LoseBall_AtkMidBwd_cr": 0, 
    "Mental_AtkMidBwd_cr" : 0,
    "ShortPass_AtkMidFwd_rl": 0, 
    "LongPass_AtkMidFwd_rl": 0, 
    "LongShot_AtkMidFwd_rl": 0, 
    "LoseBall_AtkMidFwd_rl": 0, 
    "Mental_AtkMidFwd_rl" : 0,
    "ShortPass_AtkMidFwd_c": 0, 
    "LongPass_AtkMidFwd_c": 0, 
    "LongShot_AtkMidFwd_c": 0, 
    "LoseBall_AtkMidFwd_c": 0, 
    "Mental_AtkMidFwd_c" : 0,
    "ShortPass_AtkMidFwd_lr": 0, 
    "LongPass_AtkMidFwd_lr": 0, 
    "LongShot_AtkMidFwd_lr": 0, 
    "LoseBall_AtkMidFwd_lr": 0, 
    "Mental_AtkMidFwd_lr" : 0,
}

def change_parameter(parameter, value):
    parameters[parameter] = value

def render():
    with open(os.path.join(".", "template.txt"), "r") as file:
        template_str = file.read()
        
    template = Template(template_str)
    rendered_template = template.render(parameters)
    
    return rendered_template

def save_file(rendered_template):
    with open(os.path.join(".", "rendered_template.pcsp"), "w") as file:
        file.write(rendered_template)

def remove_render():
    os.remove(os.path.join(".", "rendered_template.pcsp"))
    
def initialize_attack_team_params(attack_team_players):
    for player in attack_team_players:
        player_positions = player["player_positions"].split(", ")
        
        for position in player_positions:
            
            if position == "GK":
                parameters["ShortPass_AtkKep"] = int(player["attacking_short_passing"])
                parameters["LongPass_DefKep"] = int(player["skill_long_passing"])
                parameters["Mental_DefKep"] = int(player["mentality_composure"])
            
            elif position == "LB":
                parameters["ShortPass_AtkDef_l"] = int(player["attacking_short_passing"])
                parameters["LongPass_AtkDef_l"] = int(player["skill_long_passing"])
                parameters["BallLosePass_AtkDef_l"] = int((int(player["defending_standing_tackle"]) + int(player["defending_sliding_tackle"]) + int(player["mentality_interceptions"])) / 3)
                parameters["Mental_AtkDef_l"] = int(player["mentality_composure"])
            
            elif  position == "LCB":
                parameters["ShortPass_AtkDef_cl"] = int(player["attacking_short_passing"])
                parameters["LongPass_AtkDef_cl"] = int(player["skill_long_passing"])
                parameters["BallLosePass_AtkDef_cl"] = int((int(player["defending_standing_tackle"]) + int(player["defending_sliding_tackle"]) + int(player["mentality_interceptions"])) / 3)
                parameters["Mental_AtkDef_cl"] = int(player["mentality_composure"])
            
            elif  position == "CB":
                
                if parameters["ShortPass_AtkDef_cl"] == 0:
                    parameters["ShortPass_AtkDef_cl"] = int(player["attacking_short_passing"])
                    parameters["LongPass_AtkDef_cl"] = int(player["skill_long_passing"])
                    parameters["BallLosePass_AtkDef_cl"] = int((int(player["defending_standing_tackle"]) + int(player["defending_sliding_tackle"]) + int(player["mentality_interceptions"])) / 3)
                    parameters["Mental_AtkDef_cl"] = int(player["mentality_composure"])
                else:
                    parameters["ShortPass_AtkDef_cr"] = int(player["attacking_short_passing"])
                    parameters["LongPass_AtkDef_cr"] = int(player["skill_long_passing"])
                    parameters["BallLosePass_AtkDef_cr"] = int((int(player["defending_standing_tackle"]) + int(player["defending_sliding_tackle"]) + int(player["mentality_interceptions"])) / 3)
                    parameters["Mental_AtkDef_cr"] = int(player["mentality_composure"])
                    
            
            elif  position == "LCB":
                parameters["ShortPass_AtkDef_cr"] = int(player["attacking_short_passing"])
                parameters["LongPass_AtkDef_cr"] = int(player["skill_long_passing"])
                parameters["BallLosePass_AtkDef_cr"] = int((int(player["defending_standing_tackle"]) + int(player["defending_sliding_tackle"]) + int(player["mentality_interceptions"])) / 3)
                parameters["Mental_AtkDef_cr"] = int(player["mentality_composure"])
            
            elif position == "RB":
                parameters["ShortPass_AtkDef_r"] = int(player["attacking_short_passing"])
                parameters["LongPass_AtkDef_r"] = int(player["skill_long_passing"])
                parameters["BallLosePass_AtkDef_r"] = int((int(player["defending_standing_tackle"]) + int(player["defending_sliding_tackle"]) + int(player["mentality_interceptions"])) / 3)
                parameters["Mental_AtkDef_r"] = int(player["mentality_composure"])
            
            
            elif position == "LWB":
                parameters["ShortPass_AtkMidBwd_cl"] = int(player["attacking_short_passing"])
                parameters["LongPass_AtkMidBwd_cl"] = int(player["skill_long_passing"])
                parameters["LongShot_AtkMidBwd_cl"] = int(player["power_long_shots"])
                parameters["LoseBall_AtkMidBwd_cl"] = int((int(player["defending_standing_tackle"]) + int(player["defending_sliding_tackle"]) + int(player["mentality_interceptions"])) / 3)
                parameters["Mental_AtkMidBwd_cl"] = int(player["mentality_composure"])        
            
            elif position == "LDM":
                parameters["ShortPass_AtkMidBwd_cl"] = int(player["attacking_short_passing"])
                parameters["LongPass_AtkMidBwd_cl"] = int(player["skill_long_passing"])
                parameters["LongShot_AtkMidBwd_cl"] = int(player["power_long_shots"])
                parameters["LoseBall_AtkMidBwd_cl"] = int((int(player["defending_standing_tackle"]) + int(player["defending_sliding_tackle"]) + int(player["mentality_interceptions"])) / 3)
                parameters["Mental_AtkMidBwd_cl"] = int(player["mentality_composure"])   
 
            elif position == "CDM":
                
                if parameters["ShortPass_AtkMidBwd_cl"] == 0:        
                    parameters["ShortPass_AtkMidBwd_cl"] = int(player["attacking_short_passing"])
                    parameters["LongPass_AtkMidBwd_cl"] = int(player["skill_long_passing"])
                    parameters["LongShot_AtkMidBwd_cl"] = int(player["power_long_shots"])
                    parameters["LoseBall_AtkMidBwd_cl"] = int((int(player["defending_standing_tackle"]) + int(player["defending_sliding_tackle"]) + int(player["mentality_interceptions"])) / 3)
                    parameters["Mental_AtkMidBwd_cl"] = int(player["mentality_composure"])        
                else:
                    parameters["ShortPass_AtkMidBwd_cr"] = int(player["attacking_short_passing"])
                    parameters["LongPass_AtkMidBwd_cr"] = int(player["skill_long_passing"])
                    parameters["LongShot_AtkMidBwd_cr"] = int(player["power_long_shots"])
                    parameters["LoseBall_AtkMidBwd_cr"] = int((int(player["defending_standing_tackle"]) + int(player["defending_sliding_tackle"]) + int(player["mentality_interceptions"])) / 3)
                    parameters["Mental_AtkMidBwd_cr"] = int(player["mentality_composure"])  
                    
                
            elif position == "RDM":
                parameters["ShortPass_AtkMidBwd_cr"] = int(player["attacking_short_passing"])
                parameters["LongPass_AtkMidBwd_cr"] = int(player["skill_long_passing"])
                parameters["LongShot_AtkMidBwd_cr"] = int(player["power_long_shots"])
                parameters["LoseBall_AtkMidBwd_cr"] = int((int(player["defending_standing_tackle"]) + int(player["defending_sliding_tackle"]) + int(player["mentality_interceptions"])) / 3)
                parameters["Mental_AtkMidBwd_cr"] = int(player["mentality_composure"])  

            elif position == "RWB":
                parameters["ShortPass_AtkMidBwd_cr"] = int(player["attacking_short_passing"])
                parameters["LongPass_AtkMidBwd_cr"] = int(player["skill_long_passing"])
                parameters["LongShot_AtkMidBwd_cr"] = int(player["power_long_shots"])
                parameters["LoseBall_AtkMidBwd_cr"] = int((int(player["defending_standing_tackle"]) + int(player["defending_sliding_tackle"]) + int(player["mentality_interceptions"])) / 3)
                parameters["Mental_AtkMidBwd_cr"] = int(player["mentality_composure"])  
                
            elif position == "LM":
                parameters["ShortPass_AtkMidFwd_rl"] = int(player["attacking_short_passing"])
                parameters["LongPass_AtkMidFwd_rl"] = int(player["skill_long_passing"])
                parameters["LongShot_AtkMidFwd_rl"] = int(player["power_long_shots"])
                parameters["LoseBall_AtkMidFwd_rl"] = int((int(player["defending_standing_tackle"]) + int(player["defending_sliding_tackle"]) + int(player["mentality_interceptions"])) / 3)
                parameters["Mental_AtkMidFwd_rl"] = int(player["mentality_composure"]) 
            
            elif position == "LCM":
                parameters["ShortPass_AtkMidFwd_rl"] = int(player["attacking_short_passing"])
                parameters["LongPass_AtkMidFwd_rl"] = int(player["skill_long_passing"])
                parameters["LongShot_AtkMidFwd_rl"] = int(player["power_long_shots"])
                parameters["LoseBall_AtkMidFwd_rl"] = int((int(player["defending_standing_tackle"]) + int(player["defending_sliding_tackle"]) + int(player["mentality_interceptions"])) / 3)
                parameters["Mental_AtkMidFwd_rl"] = int(player["mentality_composure"])
            
            elif position == "CM":
                parameters["ShortPass_AtkMidFwd_c"] = int(player["attacking_short_passing"])
                parameters["LongPass_AtkMidFwd_c"] = int(player["skill_long_passing"])
                parameters["LongShot_AtkMidFwd_c"] = int(player["power_long_shots"])
                parameters["LoseBall_AtkMidFwd_c"] = int((int(player["defending_standing_tackle"]) + int(player["defending_sliding_tackle"]) + int(player["mentality_interceptions"])) / 3)
                parameters["Mental_AtkMidFwd_c"] = int(player["mentality_composure"])
            
            elif position == "RCM":
                parameters["ShortPass_AtkMidFwd_lr"] = int(player["attacking_short_passing"])
                parameters["LongPass_AtkMidFwd_lr"] = int(player["skill_long_passing"])
                parameters["LongShot_AtkMidFwd_lr"] = int(player["power_long_shots"])
                parameters["LoseBall_AtkMidFwd_lr"] = int((int(player["defending_standing_tackle"]) + int(player["defending_sliding_tackle"]) + int(player["mentality_interceptions"])) / 3)
                parameters["Mental_AtkMidFwd_lr"] = int(player["mentality_composure"])
            
            elif position == "RM":
                parameters["ShortPass_AtkMidFwd_lr"] = int(player["attacking_short_passing"])
                parameters["LongPass_AtkMidFwd_lr"] = int(player["skill_long_passing"])
                parameters["LongShot_AtkMidFwd_lr"] = int(player["power_long_shots"])
                parameters["LoseBall_AtkMidFwd_lr"] = int((int(player["defending_standing_tackle"]) + int(player["defending_sliding_tackle"]) + int(player["mentality_interceptions"])) / 3)
                parameters["Mental_AtkMidFwd_lr"] = int(player["mentality_composure"])
            
            elif position == "LAM":
                parameters["Fin_AtkFor_LR"] = int(player["attacking_finishing"])
                parameters["LongShot_AtkFor_LR"] = int(player["power_long_shots"])
                parameters["Volley_AtkFor_LR"] = int(player["attacking_volleys"])
                parameters["Heading_AtkFor_LR"] = int(player["attacking_heading_accuracy"])
                parameters["LoseBall_AtkFor_LR"] = int((int(player["defending_standing_tackle"]) + int(player["defending_sliding_tackle"]) + int(player["mentality_interceptions"])) / 3)
                parameters["Mental_AtkFor_LR"] = int(player["mentality_composure"])

            elif position == "CAM":
                parameters["Fin_AtkFor_C"] = int(player["attacking_finishing"])
                parameters["LongShot_AtkFor_C"] = int(player["power_long_shots"])
                parameters["Volley_AtkFor_C"] = int(player["attacking_volleys"])
                parameters["Heading_AtkFor_C"] = int(player["attacking_heading_accuracy"])
                parameters["LoseBall_AtkFor_C"] = int((int(player["defending_standing_tackle"]) + int(player["defending_sliding_tackle"]) + int(player["mentality_interceptions"])) / 3)
                parameters["Mental_AtkFor_C"] = int(player["mentality_composure"])
            
            elif position == "RAM":
                parameters["Fin_AtkFor_RL"] = int(player["attacking_finishing"])
                parameters["LongShot_AtkFor_RL"] = int(player["power_long_shots"])
                parameters["Volley_AtkFor_RL"] = int(player["attacking_volleys"])
                parameters["Heading_AtkFor_RL"] = int(player["attacking_heading_accuracy"])
                parameters["LoseBall_AtkFor_RL"] = int((int(player["defending_standing_tackle"]) + int(player["defending_sliding_tackle"]) + int(player["mentality_interceptions"])) / 3)
                parameters["Mental_AtkFor_RL"] = int(player["mentality_composure"])

def initialize_home_team_params(home_team_players):
    for player in home_team_players:
        player_positions = player["player_positions"].split(", ")
        
        for position in player_positions:
            if position == "GK":
                parameters["ShortPass_AtkKep"] = int(player["attacking_short_passing"])
                parameters["LongPass_DefKep"] = int(player["skill_long_passing"])
                parameters["Mental_DefKep"] = int(player["mentality_composure"])
            
            elif position == "LCB":
                parameters["ShortPass_AtkDef_cl"] = int(player["attacking_short_passing"])
                parameters["LongPass_AtkDef_cl"] = int(player["skill_long_passing"])
                parameters["BallLosePass_AtkDef_cl"] = int((int(player["defending_standing_tackle"]) + int(player["defending_sliding_tackle"]) + int(player["mentality_interceptions"])) / 3)
                parameters["Mental_AtkDef_cl"] = int(player["mentality_composure"])
            
            elif  position == "CB":
                
                if parameters["ShortPass_AtkDef_cl"] == 0:
                    parameters["ShortPass_AtkDef_cl"] = int(player["attacking_short_passing"])
                    parameters["LongPass_AtkDef_cl"] = int(player["skill_long_passing"])
                    parameters["BallLosePass_AtkDef_cl"] = int((int(player["defending_standing_tackle"]) + int(player["defending_sliding_tackle"]) + int(player["mentality_interceptions"])) / 3)
                    parameters["Mental_AtkDef_cl"] = int(player["mentality_composure"])
                else:
                    parameters["ShortPass_AtkDef_cr"] = int(player["attacking_short_passing"])
                    parameters["LongPass_AtkDef_cr"] = int(player["skill_long_passing"])
                    parameters["BallLosePass_AtkDef_cr"] = int((int(player["defending_standing_tackle"]) + int(player["defending_sliding_tackle"]) + int(player["mentality_interceptions"])) / 3)
                    parameters["Mental_AtkDef_cr"] = int(player["mentality_composure"])
                    
            
            elif  position == "LCB":
                parameters["ShortPass_AtkDef_cr"] = int(player["attacking_short_passing"])
                parameters["LongPass_AtkDef_cr"] = int(player["skill_long_passing"])
                parameters["BallLosePass_AtkDef_cr"] = int((int(player["defending_standing_tackle"]) + int(player["defending_sliding_tackle"]) + int(player["mentality_interceptions"])) / 3)
                parameters["Mental_AtkDef_cr"] = int(player["mentality_composure"])
            
            elif position == "RB":
                parameters["ShortPass_AtkDef_r"] = int(player["attacking_short_passing"])
                parameters["LongPass_AtkDef_r"] = int(player["skill_long_passing"])
                parameters["BallLosePass_AtkDef_r"] = int((int(player["defending_standing_tackle"]) + int(player["defending_sliding_tackle"]) + int(player["mentality_interceptions"])) / 3)
                parameters["Mental_AtkDef_r"] = int(player["mentality_composure"])
            
                
            

def initialize_params(home_team_players, attack_team_players):
    initialize_attack_team_params(attack_team_players)
    initialize_home_team_params(home_team_players)