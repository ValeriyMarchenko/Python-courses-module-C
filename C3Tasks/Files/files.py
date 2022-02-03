import os

def pathfinder(path = None):
    start_path = path if path is not None else os.getcwd()

    for root, dirs, files in os.walk(start_path):
        print('Directory right now')
        print('---')

        if dirs:
            print('List of dirs: ', dirs)
        else:
            print('Dirs not found')

        print('---')

        if files:
            print('List of Files: ', files)
        else:
            print('Files not found')
        
        print('---')

        if files and dirs:
            print('All: ')

        for f in files:
            print('File ', os.path.join(root, f))
        for d in dirs:
            print('Dir ', os.path.join(root, d))

        print('===')

pathfinder(r'C:\Users\Valera\Projects\Python-courses-module-C\C3Tasks')
