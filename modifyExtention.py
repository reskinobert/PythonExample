filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = []
for filename in filenames:
    newfilename = filename
    if filename.endswith(".hpp"):
        i=filename.rfind(".")+1
        newfilename = filename[:i]+"h"
    newfilenames.append(newfilename)
print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]
