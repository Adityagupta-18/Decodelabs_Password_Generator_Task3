# RANDOM PASSWORD GENERATOR
import random
import math
def passgen(length):
    spc="!@#$%^&*()-_=+~?/"
    Letter='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    Digit='0123456789'
    randalpha=random.choice(Letter)
    randspc=random.choice(spc)
    randdig=random.choice(Digit)
    pas=''
    lenalpha=math.ceil(length/2)
    lendig=math.floor(length/4)
    for i in range(0,lenalpha):
        pas+=random.choice(Letter)
    for i in range(0,lendig):
        pas+=random.choice(Digit)
    for i in range(0,lendig):
        pas+=random.choice(spc)
    paslst=list(pas)
    random.shuffle(paslst)
    finalpass=''.join(paslst)
    return finalpass

ch='y'
while ch=='y':
    n=int(input("Enter Length of password : "))
    if n<8:
        print("Enter Minimun length 8 !")
    else:
        rand_pass=passgen(n)
        print("Generated Password : ",rand_pass)
    ch=input("\nPress 'Y' to generate again : ").lower()