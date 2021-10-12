"""
A script that installs my personal LaTeX templates 
"""

# Initial Writing Date : May 25, 2021
# Last Modified        : Oct 12, 2021
# Version              : 0.2
# Author               : Brymer Meneses

import os
import requests

# Dictionary that contains the name and
# filename of the LaTeX template
TEMPLATES = {
    "module": r"templates/module.tex",
}
REPO_LINK = r"https://raw.githubusercontent.com/brymer-meneses/latex-templates/main"

CORE_FILES = {
    "packages": r"core/packages.tex",
    "macros": r"core/macros.tex",
}


def prompt():
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
    chosen_templates = input("==> ")
    template_choices = chosen_templates.split(" ")

    templates_to_be_installed = []
    for template_id in template_choices:
        for number, template_name in enumerate(TEMPLATES.keys()):
            if number + 1 == int(template_id):
                templates_to_be_installed.append(template_name)

    proceed_decision = input("----> Proceed? [Y/n]: ")
    if proceed_decision.lower() == "n":
        exit()
    elif proceed_decision.lower() == "y" or proceed_decision == "":
        print("----> Downloading Templates ...")
        download_templates(templates_to_be_installed)
    else:
        print("     - ✕ Invalid decision!")

    print("Success, have a nice day!")
    return


def merge_files(core_files, template_files):
    """Splices core tex files into a single file"""
    cwd = os.getcwd()

    print("----> Splicing files ...")
    core_content = ""
    for file in core_files:
        core_content += file
        core_content += "\n"

    for template_content, template_name in template_files:
        filename = os.path.join(cwd, template_name)

        with open(filename, "w") as spliced_file:
            data = core_content
            data += template_content
            spliced_file.write(data)
    print("     -- ✓ Done")
    return


def download_templates(choices):
    """Helper function to recursively downloads templates"""

    core_files = []
    template_files = []

    # download core tex files
    for file in CORE_FILES:
        filename = CORE_FILES[file]
        downloaded_file = get_file_from_repo(filename)
        if downloaded_file is not None:
            core_files.append(downloaded_file)
        else:
            print(f"     -- ✕ Error: failed to get: {filename}")
    print("     -- ✓ Downloaded core tex files")

    # download template choices
    for choice in choices:
        # save the template name as it will serve as the
        # filename of the spliced file
        filename = TEMPLATES[choice]
        downloaded_file = get_file_from_repo(filename)
        if downloaded_file is not None:
            template_files.append((downloaded_file, f"{choice}.tex"))
        else:
            print(f"     -- ✕ Error: failed to get: {filename}")
    print("     -- ✓ Downloaded template tex files")

    merge_files(core_files, template_files)
    return


def get_file_from_repo(repo_filename):
    """Helper function to download specific files in a repository"""
    r = requests.get(f"{REPO_LINK}/{repo_filename}")
    if r.status_code == 404:
        return None
    else:
        return r.text


if __name__ == "__main__":
    prompt()
