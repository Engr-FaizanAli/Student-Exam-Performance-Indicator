from setuptools import find_packages,setup
from typing import List
hypen_e_dot='-e .'
def get_requirements(file_path:str)->List[str]:
    '''this func will return list of requirements'''
    requirements=[]
    with open(file_path) as file_obj:
        requiremtns=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]
    if hypen_e_dot in requirements:
        requirements=requirements.remove(hypen_e_dot)
    return requirements

setup(
    name='mlproject',
    version='0.0.3',
    author='Faizan Ali',
    author_email='fali31820@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),

)
if __name__=='__main__':
    setup()
