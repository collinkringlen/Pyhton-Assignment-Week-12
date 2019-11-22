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
