import os

"""
r = read   open the file for reading, error if not found
w = write  open the file for writing and overwrite existing contents and if not found create new one
a = append open the file for writing and appending the new contents to the end of the file, if not found create new one
x = create create new file, error if file already exists
"""

"""
we can specify if the fil should be handled as a text file or a binary file
t  for text mode
b  for binary mode

tf = open('text.txt', 'xt')
bf = open('binary.txt', 'xb')
"""

# f = open('names_list.txt')
# print(f.mode) # check the mode of the file
# print(f.read()) # read all file content
# print(f.read(4)) # read 4 characters

# print(f.readlines()) # read all lines and return a list of lines

# print(f.readline()) # read first line, the newline character (\n) at the end of the line is part of the string returned by readline() "line1\n"

# print(f.readline()) # read second line "line2\n"

# f.seek(0)  # reset pointer to beginning of the file, i have to do this to read the file again otherwise the next print will not print anything

# print([line.strip() for line in f.readlines()]) # read all lines and remove the new line character (\n) at the end of each line

#-------------------------------------------------------------

# Removing the line with 2 ways

# print(f.readline().strip()) # read first line, the newline character (\n) at the end of the line is removed
# print(f.readline(), end='') # Removes the extra newline from print

# for line in f:
#     print(line, end='')

# f.close() # always remember to close the file


# using try/except with file opening is a more better way to make sure you closed the file in the finally statement
# try:
#     # f = open('names_list.txt')
#     f = open('names.txt')
#     print(f.read())
# except:
#     print('File not found')
# finally:
#     f.close()


# append - create the file if it doesn't exist
# f = open('names.txt', 'a')
# f.write('\nNeil')
# f.close()
# f = open('names.txt')
# print(f.read())
# f.close()


# write "overwrite"
# f = open('context.txt', 'w')
# f.write('I will delete all the context file content')
# f.close()
# f = open('context.txt')
# print(f.read())
# f.close()

#--------------------------------------------------------------

## 2 ways to create the file 

# 1- open the fil for writing, create the file if it doesn't exist
# f = open('names_list.txt', 'w')
# f.close()

# 2- create the file, and returns error if it exists
# try:
#     # first way
#     # f = open('names_list.txt', 'x')
#     # f.close()

#     # second way
#     with open('islam.txt', 'x') as f:
#         pass
# except:
#     print('File already exists')

#--------------------------------------------------------------

## delete a file

# first way
# if os.path.exists('islam.txt'):
#     os.remove('islam.txt')
# else:
#     print("File not found")


# second way
# try:
#     os.remove('dave.txt')
# except:
#     print("File not found")


# delete folder
# os.rmdir('foldername')

#--------------------------------------------------------------

# using "with" statement is the best practice to open file, it closes it automatically

# copying the names_list file content to more_names file 

with open("names_list.txt", "r") as rf:
    with open("more_names.txt", "w") as wf:
        rf_content = rf.read()
        for line in rf_content:
            wf.write(line)

#-----------------------------------------------------------------------------

"""
This approach reads the file in chunks, not all at once.

That means:

    Efficient for large files — You don’t load the entire file into memory.

    You control how much to read at a time (like buffering).

    Useful for streaming, network transfers, or when processing a large file piece by piece.
"""

with open("names_list.txt") as f:
    size_to_read = 7

    f_content = f.read(size_to_read)
    print(f.tell())  # ⬅️ Shows where the pointer is after reading 7 characters

    while len(f_content) > 0:
        print(f_content, end='')
        f_content = f.read(size_to_read)

    print("\n", f.tell())  # ⬅️ Shows the final position (i.e., end of the file)

    f.seek(0)  # ⬅️ Reset pointer to start
    print(f.tell())  # ⬅️ Should now print 0


with open("jaguar.jpg", "rb") as rf:
    with open("jaguar_copy.jpg", "wb") as wf:
        chunk_size = 4096
        rf_content = rf.read(chunk_size)

        while len(rf_content) > 0:
            wf.write(rf_content)
            rf_content = rf.read(chunk_size)

#------------------------------------------------------------------------------

## Notes

# combining the with statement with a try-except block is indeed one of the best ways to handle file operations. This approach ensures that:
# The file is properly closed when the block exits (because of with).
# Any errors during the file operation are gracefully handled (using try-except).

try:
    with open('file_name.txt', 'r') as f:  # Change mode ('r', 'w', 'x', etc.) as needed
        # Perform operations with the file
        content = f.read()
        print(content)
except FileNotFoundError:
    print("Error: The file does not exist.")
except PermissionError:
    print("Error: You do not have permission to access the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


try:
    f = open('context.txt');
    try:
        f.write("Ahmed goes to school") # file opened for read, add w to open it for writing
        print('text written')
    except Exception as e:
        print(f"Can't write to file because : {e}")
    finally:
        f.close()
except Exception:
    print(f"File not found")
