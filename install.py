"""
A script that installs my personal LaTeX templates 
By Brymer Meneses
"""

# initial writing date : may 25, 2021
# last modified        : oct 12, 2021
# version              : 0.2
# author               : brymer meneses

import os
import requests

# Dictionary that contains the name and
# filename of the LaTeX template
TEMPLATES = {
    "module": r"templates/module-template.tex",
}
REPO_LINK = r"https://raw.githubusercontent.com/brymer-meneses/latex-templates/main"

CORE_FILES = {
    "packages": r"core/packages.tex",
    "macros": r"core/macros.tex",
}


def show_prompt():
    """Handles main loop"""
    print(
        """
        LaTeX Templates Installer
        Brymer Meneses v0.2, 10-2021
        """
    )

    print("Available LaTeX Templates")
    for number, template_name in enumerate(TEMPLATES.keys()):
        print(f"\t[{number + 1}]: {template_name}")

    print("\nEnter the LaTeX templates you want to install")
    chosen_templates = input("=> ")
    template_choices = chosen_templates.split(" ")

    templates_to_be_installed = []
    for template_id in template_choices:
        for number, template_name in enumerate(TEMPLATES.keys()):
            if number + 1 == int(template_id):
                templates_to_be_installed.append(template_name)

    proceed_decision = input("Proceed? (y/n): ")
    if proceed_decision.lower() == "n":
        exit()
    elif proceed_decision.lower() == "y":
        pass
    else:
        print("Invalid decision!")

    print("Success, have a nice day!")
    return templates_to_be_installed


def merge_files(core_files, template_files):
    """Splices core tex files into a single file"""
    install_path = os.getcwd()

    core_content = None
    for file in core_files:
        core_content += file
        core_content += "\n"

    for template_content, template_name in template_files:
        with open(template_name) as spliced_file:
            data = core_content
            data += template_content
            spliced_file.write(data)
    return


def download_templates(choices):
    """Helper function to recursively downloads templates"""

    data = []
    core_files = None
    template_files = None

    # download core tex files
    for file in CORE_FILES:
        core_files = data.append(get_file_from_repo(CORE_FILES[file]))

    # download template choices
    for choice in choices:
        # save the template name as it will serve as the
        # filename of the spliced file
        template_files = data.append((get_file_from_repo(TEMPLATES[choice]), choice))

    merge_files(core_files, template_files)
    return


def get_file_from_repo(repo_file_name):
    """Helper function to download specific files in a repository"""
    content = requests.get(f"{REPO_LINK}/{repo_file_name}")
    return content.text


if __name__ == "__main__":

    template_choices = show_prompt()
    download_templates(template_choices)
