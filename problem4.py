import os
# Specify the path to the directory you want to list
path = "/Code Playground"
# list all the files and directories in the specified path
contents = os.listdir(path)
# print each file and directory name in the contents list
print("Contents of the directory:")
for item in contents:
    print(item)