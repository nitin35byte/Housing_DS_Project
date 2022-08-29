from setuptools import setup
from typing import List

def get_requirements_list()->List[str]:
    pass

#declaring variable for setup functions
PROJECT_NAME="housing-predictor"
VERSION="0.0.1"
AUTHOR="Nitin"
DESCRIPTION="THIS IS A FIRST FSDS OMPLETE PROJECT"
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
packages=PACKAGES,
install_requires=get_requirements_list()
)

if __name__=="__main__":
    print(get_requirements_list())