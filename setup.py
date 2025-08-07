from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return the list of requirements for the project.

    Returns:
        List[str]: A list of requirements.
    """

    requirement_lst: List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            ## Read lines from the file
            lines = file.readlines()

            ## Process lines to remove any leading/trailing whitespace and comments
            for line in lines:
                requirement = line.strip()
                ## ignore empty lines and -e . 
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")
    
    return requirement_lst

setup(
    name = "NetworkSecuritySystem",
    version = "0.0.1",
    author = "Nitin Mishra",
    author_email = "mishranitin6076@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements(),
)