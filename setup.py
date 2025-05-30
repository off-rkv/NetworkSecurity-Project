from setuptools import find_packages, setup
#find_package -> scan all the library and where __init__ file present it take as a package
from typing import List


requirement_lst=[]

def get_requirements()->List[str]:
    '''
    this function is return list of requirements
    '''
    try:
        with open('requirements.txt','r') as file:
            #Read lines from the file
            lines=file.readlines()
            #Process each line
            for line in lines:
                requirement=line.strip() # remove the space
                ##ignore the empty lines and '-e.', "-e. is trigged all the above line, it is refer the 'setup.py' file "
                if requirement and requirement!='-e.':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print('requirements.txt file not found')
    
    return requirement_lst

# print(get_requirements())

#setup metadata
setup(
    name="NetworkSecurity",
    version="0.0.1",
    author='off.rkv',
    author_email='off.rkv@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)

