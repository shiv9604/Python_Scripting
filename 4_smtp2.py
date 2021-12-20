from os import path


def createfile(destination):
    if not path.isfile(destination):
        with open("Destination.txt",'w') as f:
            f.write("Welcome to email scripting")

#If we are entering the path we should put doble \\ over their!
destination = 'C:\\Users\\shivk\\OneDrive\\Desktop\\Code Files Softwares\\C & C++ & PYTHON Vscode\\.vscode'

createfile(destination)
print("File is created sucessfully")