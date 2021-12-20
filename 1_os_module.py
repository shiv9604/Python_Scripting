
import os
# for our current working directory
def current_directory():
    cwd = os.getcwd()
    print(cwd)

# for the path we want to know anout the file....
def file_path(filename):
    path = os.path.abspath(filename) # --> gives the path for the file
    print(path)


current_directory()
filename = "input.txt"
file_path(filename)