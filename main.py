import argparse
from os import listdir, mkdir
from os.path import isfile, join
from shutil import copyfile, move
import sys

# Parse arguments passed to file
parser = argparse.ArgumentParser(description='Copies files from a source folder to a new destination which the files are split into folders of N files')
parser.add_argument('--filesPerFolder', nargs="?", default=100, help='Maximum files per folder (default: 100)')
parser.add_argument('--input', help='Specify the input folder with all of the files.')
parser.add_argument('--output', help='Destination folder for the folders/files.')
parser.add_argument('--prefix', nargs="?", default="Folder", help='Prefix for the folder I.E Folder = Folder-1, Folder-2, etc. (default: Folder)')
parser.add_argument('--move', nargs='?', const=True, default=False, help='Instead of copying the files, move the files.')

args = parser.parse_args() # Process Arguments

filesPerFolder = int(args.filesPerFolder) # Maximum files a folder can contain
folderPrefix = args.prefix # Prefix for the name of each folder in output
copy = not args.move # Determines whether or not the files will be copied or moved. files will be copied by default

# If input and output aren't specified than print help and quit
if (not args.input or not args.output):
    print("Input or Output not specified")
    parser.print_help()
    sys.exit(0)

inputFolder = args.input # Folder containing all of the files
outputFolder = args.output # Folder destination for files/folders

# Generate structure of input folder
inputStructure = [f for f in listdir(inputFolder) if isfile(join(inputFolder, f))]
inputStructure.sort()

# Set the function used to move/copy the files from source to destination
if(copy):
    fileFunction = copyfile
else:
    fileFunction = move

for i in range(0, len(inputStructure), filesPerFolder):
    # Folder name uses ternary expression to determine if - is necessary based on folder prefix
    folderName = "%s%s%i" % (folderPrefix, ("-", "")[folderPrefix==""], i/filesPerFolder)
    
    # Generate path to output folder
    path = join(outputFolder,folderName)
    
    # Create new output folder
    mkdir(path)
    
    # Iterate through all files
    for j in inputStructure[i:i+filesPerFolder]:
      
        # Generate source and destination paths
        src = join(inputFolder, j)
        dst = join(path, j)
        # Move/Copy the file
        fileFunction(src, dst)
        
        # Print file
        print("%s -> %s" % (src, dst))
        
print("Finished...")
