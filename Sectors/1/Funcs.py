import base64, binascii
AZ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
az="abcdefghijklmnopqrstuvwxyz"

def InsertChar_each(s="ABCDEFGHIJKLMNOPQRSTUVWXYZ",InCh=' '):return(InCh.join(s))
def P(c='-',n=50):return(print(c*n))

def az_List():return         [chr(i) for i in range(ord('a'),ord('z')+1)]
def AZ_List():return         [chr(i) for i in range(ord('A'),ord('Z')+1)]
def az_Str(): return ''.join([chr(i) for i in range(ord('a'),ord('z')+1)])
def AZ_Str(): return ''.join([chr(i) for i in range(ord('A'),ord('Z')+1)])

def cipher_caesar_az(s="abcdefghijklmnopqrstuvwxyz",k=3): return(''.join([ chr(ord('a')+(ord(c)-ord('a')+k)%26) for c in s]))
def cipher_caesar_AZ(s="ABCDEFGHIJKLMNOPQRSTUVWXYZ",k=3): return(''.join([ chr(ord('A')+(ord(c)-ord('A')+k)%26) for c in s]))
def cipher_caesar_BRUTE(s="ABCDEFGHIJKLMNOPQRSTUVWXYZ",AZ_or_az='AZ'):
    if AZ_or_az == 'AZ':return[cipher_caesar_AZ(s,k) for k in range(0,26)]
    if AZ_or_az == 'az':return[cipher_caesar_az(s,k) for k in range(0,26)]

def ASUB(m,A,B):
    o   = m.maketrans(A,B)
    r   = m.translate(o)
    return(r)

def Bys(s="ABC"):return(bytes(s,'UTF8'))




# Note, the 'b' below (out == 'b' ..) means the b'' output. 
def HX(s="ABC",E_D='E',out='s'):
    if E_D == 'E' and out == 's':return(binascii.hexlify(Bys(s)).decode())
    if E_D == 'E' and out == 'b':return(binascii.hexlify(Bys(s)))
    if E_D == 'D' and out == 's':return(binascii.unhexlify(Bys(s)).decode())
    if E_D == 'D' and out == 'b':return(binascii.unhexlify(Bys(s)))

#
def B6(s="ABC",E_D='E',out='s'):
    if E_D == 'E' and out == 's':return(base64.b64encode(Bys(s)).decode())
    if E_D == 'E' and out == 'b':return(base64.b64encode(Bys(s)))
    if E_D == 'D' and out == 's':return(base64.b64decode(Bys(s)).decode())
    if E_D == 'D' and out == 'b':return(base64.b64decode(Bys(s)))
#


def file_text(in_file="test.txt",splitlines=0):
    with open(in_file, 'rt') as f:
        text=f.read()
    text_notsplit   = text
    text_splitlines = text.splitlines()
    if splitlines == 0: return(text_notsplit)
    if splitlines == 1: return(text_splitlines)
#

def file_lines(in_file="test.txt"):
    with open(in_file, 'rt') as f:
        lines=f.readlines()
    return(lines)
