import os

# Specify the name of the file to check for
file_name = 'example12.txt'

# Check if the file exists in the current directory
if not os.path.isfile(file_name):
    # If the file doesn't exist, create it
    with open(file_name, 'w') as f:
        f.write('This is a new file.')

# Check for changes in the local repository
output = os.popen('git status').read()
if 'Changes not staged for commit' in output:
    print('There are changes in the local repository.')
else:
    print('There are no changes in the local repository.')
