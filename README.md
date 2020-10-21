# ciphers-python #

Cipher encryption algorithms implemented in Python3 using Jupyter Notebooks!

Key words: Cypher, Cipher, Cyphers, Ciphers, cryptography, encryption, obfuscation, enciphering, deciphering  - in python3



**Purpose of this git:**

**Try to re-create some historic. Used ciphers, and slowly working them up to advanced, today-used crypto.** 
**For example; S-boxes in today's encryption algorithms; and P-boxes, (both used in so-called SP-Networks)**

An S-Box can be thought of a Substitution cipher. like Caesar. (Example below): abc -> def.

Or, another example of 1 simple (extremely simplified, I should add) can be a Alphabetical Substitution:

Instead of the normal alphabet (a-z); abcdefghijklmnopqrstuvwxyz.

You use (in your Cipher) a permuted, totally mixed up alphabet: uijaopqvwbghklmncxydefszrt

A few test-rounds, to give you the idea..

**Normal alphabet: abcdefghijklmnopqrstuvwxyz**
**Mixed alphabet: uijaopqvwbghklmncxydefszrt**

**Normal alphabet shifted with 3: abcdefghijklmnopqrstuvwxyz -> defghijklmnopqrstuvwxyzabc**

**Mixed alphabet shifted with 3: uijaopqvwbghklmncxydefszrt -> aopqvwbghklmncxydefszrtuij**

**Enciphering the message "abc" with mixed alphabet, shift 5: abc -> wmf**

*These kind of, working-up examples & projects I am right now doing.*
*And, this will be a sub-project, which will be used in my publications. On my website.*
*Go check it out, if you want!*


[x] https://unixresearcher.wixsite.com/thecryptanalyst


-----------------------------------
# List of complete implementations:
-----------------------------------


* [x] Alphabetical Substitution



---------------------------------------------------
# List of Incomplete (In progress) implementations:
---------------------------------------------------
* []  Lorenz SZ // 0.01 % of 100% Done

* [] Trithemius cipher.    // Coming very very soon! 50% of 100% done!
* [] Polyalphabetic cipher // Kinda like Alphabetical Subtitution cipher.
* [] Transposition cipher  // Kinda like Alphabetical Substitution cipher too actually, e.g Vigenere cipher.



## links:

https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
- "a method of **encrypting alphabetic** text by using a **series of interwoven Caesar ciphers**, based on the letters of a *keyword*. It employs a form of **polyalphabetic substitution.**"

https://en.wikipedia.org/wiki/Polyalphabetic_cipher
- "**A polyalphabetic cipher is any cipher based on substitution**, using **multiple substitution alphabets**. The **Vigenère cipher** is probably the best-known example of a **polyalphabetic cipher**, though it is a simplified special case. *The Enigma machine is more complex but **is still fundamentally a polyalphabetic substitution cipher.***"

https://en.wikipedia.org/wiki/Transposition_cipher
- "In cryptography, a **transposition cipher** is a method of encryption by which the **positions held by units of plaintext (which are commonly characters or groups of characters) are shifted according to a regular system**, so that the *ciphertext constitutes a permutation of the plaintext*. That is, the *order* of the *units is changed* (*the plaintext is reordered*). Mathematically **a bijective function** is used on the **characters' positions** to **encrypt** and an *inverse function* to **decrypt.** "

https://en.wikipedia.org/wiki/Bijective
- "In mathematics, a bijection, bijective function, one-to-one correspondence, or invertible function, is a function between the elements of two sets, where each element of one set is paired with exactly one element of the other set, and each element of the other set is paired with exactly one element of the first set."

Thanks for showing interest!

*W.M*
