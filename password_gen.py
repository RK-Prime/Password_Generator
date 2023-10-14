try:
    from string import ascii_letters, digits, punctuation, join
except ImportError:
    from string import ascii_letters, digits, punctuation
from random import choice, sample, randint
# specific imports to make this small, fast, efficient

#=====================================METHODS===================================
def isEven(integer):
    """Return Boolean: True if input is even, False if not."""
    return integer % 2 == 0

def RandPass(size = 8):
    """This is the password generator"""
    s0 = ascii_letters # Upercase and Lowercase letters
    s1 = digits # integer and float Digits
    s3 = "!$%^&*-_~" # Speial Symbols
    s = s0 + s1
    s_full = s + s3
    passlen = size.get()
    password_new = ""

    # assigning specific sizes for each section of the pw generated
    if isEven(passlen) == True:
        front = passlen // 3
    else:
        front = passlen // 2
    mid = 2
    back = passlen - (front + mid) - 1

    p0 = "".join(choice(s0)) # NO punctuations as 1st character!!!
    p1 = "".join(sample(s_full, front))
    p2 = "".join(sample(s3, mid))
    # forces a minimum number of punctuations in the middle
    p3 = "".join(sample(s,back ))
    if passlen != len(p0 + p1 + p2 + p3):
        p2 = "".join(sample(s3, passlen - (front+back+1) ))

    if p3[:-1] == ' ': # to avoid having an empty space at the end of password
        temp = list(p3)
        temp[:-1] = choice(s)
        p3 = ''.join(str(e) for e in temp)
    password_new = p0 + p1 + p2 + p3
    
    if passlen <= 8:
        message = 'VERY WEAK'
        color_value = "#6d0001"
    elif passlen <=10:
        message = 'WEAK'
        color_value = "#cc0000"
    elif passlen <=12:
        message = 'DECENT'
        color_value = "#fc8600"
    elif passlen <=14:
        message = 'GOOD'
        color_value = "#eae200"
    elif passlen <=16:
        message = 'STRONG'
        color_value = "#9ff400"
    elif passlen <=18:
        message = 'VERY STRONG'
        color_value = "#007715"
    elif passlen >18:
        message = 'EXCELLENT'
        color_value = "#001fef"
    else:
        pass

    return password_new, message, color_value
