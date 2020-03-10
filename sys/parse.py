import sys
from os import listdir
from os.path import isfile, join

folder_path = "../sections/"

onlyfiles = list(filter(lambda x: x[-4:] == ".tex", [f for f in listdir(folder_path) if isfile(join(folder_path, f))]))

print(onlyfiles)

for filename in onlyfiles:

    f = open(folder_path + filename, "r")
    source = []
    for line in f:
        source.append(line.strip())
    f.close()
    f = open(folder_path + filename, "w")

    counter = 0
    isEmptyPrevious = False

    for line in source:
        if line == "" and isEmptyPrevious:
            continue
        isEmptyPrevious = False
        if line == "":
            isEmptyPrevious = True
    
        if line[1:5] == "end{":
            counter -= 1
        
        for i in range(counter):
            print("\t", file=f, end="")
        print(line, file=f)
    
        if line[1:7] == "begin{":
            counter += 1
