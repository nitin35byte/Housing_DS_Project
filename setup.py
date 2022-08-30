from setuptools import setup , find_packages
from typing import List


#declaring variable for setup functions
PROJECT_NAME="housing-predictor"
VERSION="0.0.2"
AUTHOR="Nitin"
DESCRIPTION="THIS IS A FIRST FSDS COMPLETE PROJECT"
PACKAGES=["HOUSING"]
REQUIREMENTS_FILE_NAME='requirements.txt'



def get_requirements_list()->List[str]:

    """"
Description: thsi function is going to rwturn the lidt of requirements mention in requirements.txt file

Return: this function is going to return a list which conatain anme of libraries  mentioned in requirements.txt file

    """
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
       return  requirement_file.readlines()

setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(),#find_packages-is return  all the packages (packags is init file under folders(folder= Module))
install_requires=get_requirements_list()
)

