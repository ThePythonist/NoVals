import sys, os

class FoundString(Exception):
    def __init__(self, lineNumber):
        super().__init__("Found string on line: "+str(lineNumber))

class FoundNumber(Exception):
    def __init__(self, lineNumber):
        super().__init__("Found number on line: "+str(lineNumber))

class FoundNone(Exception):
    def __init__(self, lineNumber):
        super().__init__("Found None on line: "+str(lineNumber))

file = os.path.abspath(sys.argv[0])

read = open(file, "r")
rawLines = read.readlines()
lines = [rawLines[x].strip() for x in range(len(rawLines))]
read.close()

lineNumber = 1
while lineNumber <= len(lines):
    line = lines[lineNumber-1]
    if "'" in line or "\"" in line:
        raise FoundString(lineNumber)
    for digit in range(9):
        while str(digit) in line:
            index = line.index(str(digit))
            if index == 0:
                raise FoundNumber(lineNumber)
            previous = line[index-1]
            if ord(previous) not in list(range(97,123)) + list(range(65,91)):
                raise FoundNumber(lineNumber)
            line = line[:index] + line[index+1:]
    while "None" in line:
        index =line.index("None")
        if index == 0:
            raise FoundNone(lineNumber)
        previous = line[index-1]
        if ord(previous) not in list(range(97,123)) + list(range(65,91)):
            raise FoundNone(lineNumber)
        line = line[:index] + line[index+4:]
    lineNumber += 1
