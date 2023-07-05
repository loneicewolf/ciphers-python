# Note. this was done in a Jupyter Notebook.
##

#~~~~~~~~~~~~~~~~~~~~~~~~~
#   

#~~~~~~~~~~~~~~~~~~~~~~~~~







#~~~~~~~~~~~~~~~~~~~~~~~~~
AZ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
az="abcdefghijklmnopqrstuvwxyz"

#~~~~~~~~~~~~~~~~~~~~~~~~~



#~~~~~~~~~~~~~~~~~~~~~~~~~
def az_List():return         [chr(i) for i in range(ord('a'),ord('z')+1)]
def az_Str(): return ''.join([chr(i) for i in range(ord('a'),ord('z')+1)])
def AZ_List():return         [chr(i) for i in range(ord('A'),ord('Z')+1)]
def AZ_Str(): return ''.join([chr(i) for i in range(ord('A'),ord('Z')+1)])

# AZ caesar cipher
## Def Values for both, the alphabet as input string, and key = 3
def cipher_caesar_AZ(s="ABCDEFGHIJKLMNOPQRSTUVWXYZ",k=3): return(''.join([ chr(ord('A')+(ord(c)-ord('A')+k)%26) for c in s]))
def cipher_caesar_az(s="abcdefghijklmnopqrstuvwxyz",k=3): return(''.join([ chr(ord('a')+(ord(c)-ord('a')+k)%26) for c in s]))

# Tests
#cipher_caesar_AZ(AZ,3) # DEFGHIJKLMNOPQRSTUVWXYZABC
#cipher_caesar_az(az,3) # defghijklmnopqrstuvwxyzabc
#cipher_caesar_AZ()     # DEFGHIJKLMNOPQRSTUVWXYZABC
#cipher_caesar_az()     # defghijklmnopqrstuvwxyzabc


def ASUB(m,A,B):
    o   = m.maketrans(A,B)
    r   = m.translate(o)
    return(r)



def cipher_caesar_BRUTE(s="ABCDEFGHIJKLMNOPQRSTUVWXYZ",AZ_or_az='AZ'):
    if AZ_or_az == 'AZ':return[cipher_caesar_AZ(s,k) for k in range(0,26)]
    if AZ_or_az == 'az':return[cipher_caesar_az(s,k) for k in range(0,26)]
cipher_caesar_BRUTE()
# by def. it outputs:
#['ABCDEFGHIJKLMNOPQRSTUVWXYZ',
# 'BCDEFGHIJKLMNOPQRSTUVWXYZA',
# 'CDEFGHIJKLMNOPQRSTUVWXYZAB',
# ...
# 'XYZABCDEFGHIJKLMNOPQRSTUVW',
# 'YZABCDEFGHIJKLMNOPQRSTUVWX',
# 'ZABCDEFGHIJKLMNOPQRSTUVWXY']








def InsertChar_each(s="ABCDEFGHIJKLMNOPQRSTUVWXYZ",InCh=' '):return(InCh.join(s))
InsertChar_each("abcxyzdef")#'a b c x y z d e f'






#~~~~~~~~~~~~~~~~~~~~~~~~~




#~~~~~~~~~~~~~~~~~~~~~~~~~
#test.txt
#  LINE 1
#  LINE 2
#  LINE 3

def file_text(in_file="test.txt",splitlines=0):
    with open(in_file, 'rt') as f:
        text=f.read()
    # easier to read
    text_notsplit   = text
    text_splitlines = text.splitlines()
    if splitlines == 0: return(text_notsplit)
    if splitlines == 1: return(text_splitlines)
    
def file_lines(in_file="test.txt"):
    with open(in_file, 'rt') as f:
        lines=f.readlines()
    return(lines)

myfile="test.txt"
splitlines=0
#file_text(myfile,splitlines=1)[0]#'LINE 1'
#file_text(myfile,splitlines=1)#['LINE 1', 'LINE 2', 'LINE 3']

#~~~~~~~~~~~~~~~~~~~~~~~~~




#~~~~~~~~~~~~~~~~~~~~~~~~~
# GUI



#~~~~~~~~~~~~~~~~~~~~~~~~~
# GUI
AZ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def cipher_caesar_AZ(s="ABCDEFGHIJKLMNOPQRSTUVWXYZ",k=3): return(''.join([ chr(ord('A')+(ord(c)-ord('A')+k)%26) for c in s]))
def cipher_caesar_az(s="abcdefghijklmnopqrstuvwxyz",k=3): return(''.join([ chr(ord('a')+(ord(c)-ord('a')+k)%26) for c in s]))
def cipher_caesar_BRUTE(s="ABCDEFGHIJKLMNOPQRSTUVWXYZ",AZ_or_az='AZ'):
    if AZ_or_az == 'AZ':return[cipher_caesar_AZ(s,k) for k in range(0,26)]
    if AZ_or_az == 'az':return[cipher_caesar_az(s,k) for k in range(0,26)]

import ipywidgets as widgets
from ipywidgets import HBox, VBox
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display
%matplotlib inline
@widgets.interact
def f(k=(0,26),m="ABCDEFGHIJKLMNOPQRSTUVWXYZ",choice_1=[0,1]):
    ctx_1=cipher_caesar_BRUTE(m)
    if choice_1 == 0:
        for i in ctx_1:print(i)
    if choice_1 == 1:
        for i in ctx_1: print( cipher_caesar_AZ(i,k) )
    
#~~~~~~~~~~~~~~~~~~~~~~~~~#~~~~~~~~~~~~~~~~~~~~~~~~~
