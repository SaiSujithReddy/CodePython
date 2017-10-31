'''

Given current folder location print the directory structure.

'''

import os
def print_directory_structure():
    print(os.walk("."))

def print_directory_contents(sPath):
    import os
    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath,sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)

print_directory_contents(os.curdir)
#print_directory_structure()