# FILES, DIRECTORIES, AND PATHS

# FILES
#   Open:
with open("my_file.txt") as file:
    #   Read:
    contents = file.read()
    print(contents)

    #   Close: file takes resources from computer, so you should close when you don't need it
    #   file.close()

with open('new_file.txt', mode="w") as file:
    #   Write to file:
    file.write('New text.')

    # Modes:
    # 'r' - read
    # 'w' - write (replaces)
    # 'a' - appends to end of text

# UNDERSTAND RELATIVE AND ABSOLUTE FILE PATHS
#   Files can live within folders
#   Root is represented by /
#   Absolute File Path: the path relative to the root
#   Relative File Path: the path relative to what folder you already are in (the working directory)
#   ./ - signifies 'look in the current folder for this file'
#   ../ - goes upward in the working directory to the folder beforehand
#   if there is a file in the same level you can just call on the file
#   ../../Desktop/my_file.txt - goes up two levels
