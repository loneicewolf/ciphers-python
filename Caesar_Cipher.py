## Defs Part
## 97 is ord('a')
def r_string(s,k): return(''.join([ chr(97+(ord(c)-97+k)%26) for c in s ]))
def r_letter(l,k): return(          chr(97+(ord(l)-97+k)%26)              )

# r_string - caesar cipher on a string. so 'abc' -> 'def' for example.
# r_letter - caesar cipher on a letter/character (single), so 'a' -> 'b' for example.
