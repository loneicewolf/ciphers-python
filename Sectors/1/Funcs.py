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
