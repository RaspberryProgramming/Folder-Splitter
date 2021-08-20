# Folder-Splitter
Python script designed to copy files from a source folder into a destination folder which the files will be split into folders of N files.

## Requirements

- [Python3](https://www.python.org/downloads/)

## Running the script

```git clone https://github.com/RaspberryProgramming/Folder-Splitter```

```cd Folder-Splitter```

Below is the help printout

```
usage: main.py [-h] [--filesPerFolder [FILESPERFOLDER]] [--input INPUT]
               [--output OUTPUT] [--prefix [PREFIX]] [--move [MOVE]]

Copies files from a source folder to a new destination which the files are
split into folders of N files

optional arguments:
  -h, --help            show this help message and exit
  --filesPerFolder [FILESPERFOLDER]
                        Maximum files per folder (default: 100)
  --input INPUT         Specify the input folder with all of the files.
  --output OUTPUT       Destination folder for the folders/files.
  --prefix [PREFIX]     Prefix for the folder I.E Folder = Folder-1, Folder-2,
                        etc. (default: Folder)
  --move [MOVE]         Instead of copying the files, move the files.
```

Example

```python3 main.py --input ./input --output ./output```
