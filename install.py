
"""
A script that installs my personal LaTeX templates 
By Brymer Meneses
"""

# Initial Writing Date : May 25, 2021

import os
import requests

# Dictionary that contains the name and 
# filename of the LaTeX template
TEMPLATES = { "module" : r"templates/module-template.tex", }
REPO_LINK = r"https://raw.githubusercontent.com/brymer-meneses/latex-templates/main"


def show_prompt():
    print("\n")
    print("Install LaTeX Templates")
    print("By Brymer Meneses v0.1")
    print("05-2021")
    print("\n")

    print("Available LaTeX Templates")
    for number, template_name in enumerate(TEMPLATES.keys()):
        print(f"\t[{number + 1}]: {template_name}")

    print("\nEnter the LaTeX templates you want to install \n(separated by space)")
    chosen_templates = input("Choices : ")
    inputs = parse_input(chosen_templates)

    return inputs

def parse_input(input):
    input = input.split(" ")
    return input

def process_inputs(choices):
    choices_to_be_installed = []

    print(f"\nThe following {'template' if len(choices_to_be_installed) == 1 else 'templates'} will be installed:")
    for choice in choices:
        for number, template_name in enumerate(TEMPLATES.keys()):
            if number + 1 == int(choice):
                choices_to_be_installed.append(template_name)
                print(f"\t - {template_name}")

    proceed_decision = input("Proceed? (y/n): ")
    if proceed_decision.lower() == "n":
        exit()
    elif proceed_decision.lower() == "y":
        pass
    else:
        print("Invalid decision!")

    return choices_to_be_installed

def get_file_from_repo(repo_file_name, dowloaded_file_name):
    r = requests.get(f"{REPO_LINK}/{repo_file_name}")
    with open(dowloaded_file_name, "w") as file:
        file.write(r.text)
    return

def download_files(choices):
    template_folder = os.path.join(os.getcwd(), "templates")
    if not os.path.exists(template_folder):
        os.mkdir(template_folder)

    for choice in choices:
        file_name = os.path.join(os.getcwd(), TEMPLATES[choice])
        get_file_from_repo(TEMPLATES[choice], file_name)

    decision = input("\nDownload boilerplate tex file (y/n): ")
    # TODO Dynamically import files based on the 
    # choices
    if decision.lower() == "y":
        get_file_from_repo("boilerplate.tex", "main.tex")
    else:
        pass
    print("Success, have a nice day!")
    return
        
        
if __name__ == "__main__":

    inputs = show_prompt()
    choices = process_inputs(inputs)
    download_files(choices)


