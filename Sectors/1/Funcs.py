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


