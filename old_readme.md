

--------------------------------------------------
| Cryptography In Python (Using Jupyter-Notebooks)
--------------------------------------------------

PREFACE:

This is my first git, or one of the very first anyway.
Because of that, it's not that neatly sorted, and built up. So, it could be errors(language, etc).
I'm fixing those, but if you find any - or want to improve/add/change something, contact me! 
I appreciate it!



*W.M*



Historical and Modern Ciphers - implemented in Python using Jupyter Notebooks!
Key words: Cypher, Cipher, Cyphers, Ciphers, cryptography, encryption, obfuscation, enciphering, deciphering




**Purpose of this git:**
Short: "To see practically with examples how ciphers **COULD** be implemented, (**The way I have done it is probably not the most optimal way(s)** "


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
*Sorted according to order: Newest to oldest, from top to bottom.*
* [x] Alphabetical Substitution
* [x] Runic Cipher
* [x] **BOOK CIPHER** (**FINALLY**)

---------------------------------------------------
# List of Incomplete (In progress) implementations:
---------------------------------------------------
* []  Lorenz SZ // 91.2 % of 100% Done <-- VERY soon done. Will probably get done next week!
* **[X]**  Book Cipher **DONE** **[X]**
* []  Trithemius cipher.    // Coming very very soon! 60.7% of 100% done!
* [/]  Polyalphabetic cipher // Just begun soon done. 85% of 100%!
* []  Transposition cipher  // Just begun



**SP-Networking in Python**
| -----------------------------------
*This part is just for research-code (Not actual anything optimal, or "good" programs)*
*So, do not use these in production code, these here - is **ONLY** for education/learning*
* [\] VERY soon done! (This is, like 99% done!)  Matrix  / Column major order / rotation - Cipher // Just begun



## links:

https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher - "a method of **encrypting alphabetic** text by using a **series of interwoven Caesar ciphers**, based on the letters of a *keyword*. It employs a form of **polyalphabetic substitution.**"


https://en.wikipedia.org/wiki/Polyalphabetic_cipher - "**A polyalphabetic cipher is any cipher based on substitution**, using **multiple substitution alphabets**. The **Vigenère cipher** is probably the best-known example of a **polyalphabetic cipher**, though it is a simplified special case. *The Enigma machine is more complex but **is still fundamentally a polyalphabetic substitution cipher.***"

https://en.wikipedia.org/wiki/Transposition_cipher - "In cryptography, a **transposition cipher** is a method of encryption by which the **positions held by units of plaintext (which are commonly characters or groups of characters) are shifted according to a regular system**, so that the *ciphertext constitutes a permutation of the plaintext*. That is, the *order* of the *units is changed* (*the plaintext is reordered*). Mathematically **a bijective function** is used on the **characters' positions** to **encrypt** and an *inverse function* to **decrypt.** "

https://en.wikipedia.org/wiki/Bijective - "In mathematics, a bijection, bijective function, one-to-one correspondence, or invertible function, is a function between the elements of two sets, where each element of one set is paired with exactly one element of the other set, and each element of the other set is paired with exactly one element of the first set."

