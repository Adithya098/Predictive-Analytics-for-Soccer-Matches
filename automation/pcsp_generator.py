from jinja2 import Template
import os

parameters = {
    'ShortPass_AtkKep' : 10,
    'LongPass_DefKep' : 10,
    'Mental_DefKep' : 10,
    'ShortPass_AtkDef_r' : 10,
    'LongPass_AtkDef_r' : 10,
    'BallLosePass_AtkDef_r' : 10,
    'Mental_AtkDef_r' : 10,
    'ShortPass_AtkDef_cr' : 10,
    'LongPass_AtkDef_cr' : 10,
    'BallLosePass_AtkDef_cr' : 10,
    'Mental_AtkDef_cr' : 10,
    'ShortPass_AtkDef_cl' : 10,
    'LongPass_AtkDef_cl' : 10,
    'BallLosePass_AtkDef_cl' : 10,
    'Mental_AtkDef_cl' : 10,
    'ShortPass_AtkDef_l' : 10,
    'LongPass_AtkDef_l' : 10,
    'BallLosePass_AtkDef_l' : 10,
    'Mental_AtkDef_l' : 10,
    'ShortPass_AtkMid_rl' : 10,
    'LongPass_AtkMid_rl' : 10,
    'LongShot_AtkMid_rl' : 10,
    'LoseBall_AtkMid_rl' : 10,
    'Mental_AtkMid_rl' : 10,
    'ShortPass_AtkMid_c' : 10,
    'LongPass_AtkMid_c' : 10,
    'LongShot_AtkMid_c' : 10,
    'LoseBall_AtkMid_c' : 10,
    'Mental_AtkMid_c' : 10,
    'ShortPass_AtkMid_lr' : 10,
    'LongPass_AtkMid_lr' : 10,
    'LongShot_AtkMid_lr' : 10,
    'LoseBall_AtkMid_lr' : 10,
    'Mental_AtkMid_lr' : 10,
    'Fin_AtkFor_RL' : 10,
    'LongShot_AtkFor_RL' : 10,
    'Volley_AtkFor_RL' : 10,
    'Heading_AtkFor_RL' : 10,
    'LoseBall_AtkFor_RL' : 10,
    'Mental_AtkFor_RL' : 10,
    'Fin_AtkFor_C' : 10,
    'LongShot_AtkFor_C' : 10,
    'Volley_AtkFor_C' : 10,
    'Heading_AtkFor_C' : 10,
    'LoseBall_AtkFor_C' : 10,
    'Mental_AtkFor_C' : 10,
    'Fin_AtkFor_LR' : 10,
    'LongShot_AtkFor_LR' : 10,
    'Volley_AtkFor_LR' : 10,
    'Heading_AtkFor_LR' : 10,
    'LoseBall_AtkFor_LR' : 10,
    'Mental_AtkFor_LR' : 10,
    'Save_DefKep' : 10,
    'Mental_DefKep' : 10
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
        
def initialize_params():
    return