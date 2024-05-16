#!/usr/bin/env python

from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    hypen = '-e .'
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if hypen in requirements:
            requirements.remove(hypen)
    return requirements

setup(
    name='MLprod',
    version='1.0',
    description='Python ML production',
    author='Navya',
    author_email='navyatr13@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
