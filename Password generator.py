import random
print "     How strong you wanna make your Password ?"
password=None
strength = int(input("   Type 1 for easy , 2 for medium , 3 for strong :"))
strings = 'abcdefghijklmnopqrstuvwxyz012456789!@#$%^&*()-_+`'
if strength==1:
    password = ''.join(random.sample(strings,4))
if strength==2:
    password = ''.join(random.sample(strings,6))
if strength==3:
    password = ''.join(random.sample(strings,8))
else: print "Enter your password strength properly."

print 'Your password is ',password
