import os
import sys

def mkfil():
    name = input('File Name ')
    files = open(name, "x")
    
def delfil():
    name = input('File Name ')
    os.remove(name)
