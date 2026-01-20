# string are immutable
# you cannot reassign val like str[2] = "A"

name="parth"
capital = name.upper()
print(name.lower())
print(name) # part
print(capital)  # PART

print( name.find('s') ) # -1        # in python nothing like char so you can use "" double quote as well
print( name.find('rt') ) # 2 index
print( name.find("r") ) # 2 index

print( name.replace("rt", "replaced") ) # pareplacedh

print( "par" in name )  # True
print( "xx" in name )   # False

# slicing
str = "parth"
print(str[1:3]) # ar [start, end)
print(str[:3]) # par    same as 0:3
print(str[2:]) # rth    same as [2: len(str)]

# negavtive index slicing
str2 = "APPLE" # -5 -4 -3 -2 -1
print(str2[-3: -1]) # PL

# func
str = "I am a coder."
str.endswith("er.") #returns true if string ends with substr
str.capitalize() #capitalizes 1st char
# str.replace(old, new) #replaces all occurrences of old with new
# str.find(word) #returns 1st index of 1st occurrence
str.count("am") #counts the occurrence of substr in string
str.lower()