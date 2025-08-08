import random
chars = "qwertyuiopaasdfghjklzcxvbbmn>-=+@#$^&*(*"

def gen_password(n):
    password = ""
    for i in range(n):
        password += random.choice(chars)
    return password
n = int(input("Enter the range of your password for generating : "))
print(gen_password(n))
        