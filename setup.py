from setuptools import setup,find_packages
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This functions will return list of requirements
    '''
    requirements = []
    with open(file_path,'r') as file_obj:
        requirements =  file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)  
    return requirements

setup(
name = 'student_performance',
version = '0.0.1',
author = 'Tushar Shevade',
author_email='shevade.tushar@gmail.com',
packages=find_packages(),
install_requires = get_requirements('requirements.txt')
)