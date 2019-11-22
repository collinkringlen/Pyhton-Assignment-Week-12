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
