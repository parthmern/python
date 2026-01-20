# Types of files

# 1. Text Files: store data in readable text form
#    Examples: .txt, .docx, .log, .csv, .json

# 2. Binary Files: store data in binary (0s and 1s), not readable
#    Examples: .mp4, .mov, .png, .jpeg, .pdf, .exe

# f = open("file_name", "mode")
# 'r'  : open file for reading (default mode)
# 'w'  : open file for writing, truncates (clears) file if it exists (overwrite)
# 'x'  : create a new file and open it for writing (error if file exists)
# 'a'  : open file for writing, appends data at end if file exists
# 'b'  : binary mode (used with other modes like 'rb', 'wb')
# 't'  : text mode (default)
# '+'  : open file for both reading and writing (update mode)
# 'w+'  -> write and read
# 'a+'  -> append and read


f = open("sample.txt", "r")   # r : read mode
data = f.read()               # reads complete file
data = f.readline( ) #reads one line at a time
print(data)
f.close()

f = open("demo.txt", "a") 
f.write("this is appneded text") #adds to the file

import os 
os.remove( "filename" )

with open("demo.txt", "r") as f:
    while line:
        line = f.readline()
        if( "xxx" in line):
            print(line)
        