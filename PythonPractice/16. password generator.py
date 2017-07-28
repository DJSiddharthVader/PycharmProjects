"""Write a password generator in Python. Be creative with how you generate passwords
 - strong passwords have a mix of lowercase letters, uppercase letters, numbers,
  and symbols. The passwords should be random, generating a new password every
  time the user asks for a new password. Include your run-time code in a main method"""

import random as ra
def passgen():
    Caps = list('THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG')
    letters = list('Thequickbrownfoxjumpsoverthelazydog')
    syms = list("!@#$%^&*()_+=<>//`~")
    pas = ""
    c = ra.randrange(26)
    pas += Caps[c]
    for x in range(8):
        l = ra.randrange(26)
        pas += letters[l]
    n = ra.randrange(9)
    pas += str(n)
    s = ra.randrange(19)
    pas += syms[s]
    print(pas)
    return(pas)

passgen()