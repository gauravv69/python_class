import os

# Specify the directory you want to list
directory_path = '/'

# List all files and directories in the specified path
contents = os.listdir(directory_path)

# Print the contents of the directory
print(contents)