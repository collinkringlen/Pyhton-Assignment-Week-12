#Definitions
#Collin Kringlen
#CSCI 102-Section B
#Week 12-Part A



def PrintOutput(hello):
    print("OUTPUT", hello)

def LoadFile(filestring):
    file = open(filestring, 'r')
    readfile = file.read().splitlines()
    printlist = list(readfile)
    return printlist
    file.close()
def UpdateString(str1, str2, a):
    str1 = list(str1)
    str1[a]=str2
    str1 = ''.join(str1)
    finalstr = str(str1)
    print("OUTPUT", finalstr)
def FindWordCount(lst, string):
    x = 0
    lst = (''.join(lst))
    lst = lst.split()
    for a in lst:
        if a == string:
            x = x+1
    print("OUTOUT", x)
def ScoreFinder(names, points, string):
    names = str(' '.join(names))
    names = names.lower()
    names = names.split()
    string = string.lower()
    a = 0
    b = 0
    while b< len(names):
        if string == names[b]:
            points = points[b]
            string = string.title()
            a= 1
            break
        elif string != names[b]:
            b = b+1
    if a == 1:
        print("OUTPUT", string, "got a score of", points)
    elif a!= 1:
        print('OUTPUT player not found')
