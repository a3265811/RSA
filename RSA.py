import secrets
import sys

def gcd(m,n):
    if n == 0:
        return m
    else:
        return gcd(n, m % n)

def ext_euclid(a, b):
    old_s,s=1,0
    old_t,t=0,1
    old_r,r=a,b
    if b == 0:
        return 1, 0, a
    else:
        while(r!=0):
            q=old_r//r
            old_r,r=r,old_r-q*r
            old_s,s=s,old_s-q*s
            old_t,t=t,old_t-q*t
    return old_s, old_t, old_r

def minv(a,b):
    s,t,r = ext_euclid(a,b)
    if(r != 1):
        raise("error modular inversion")
    else:
        return s % b

def sm(x,H,n):
    h = bin(H)
    y = x
    for i in range(3,len(h)):
        y = (y ** 2) % n
        if(h[i] == '1'):
            y = (y * x) % n
    return y

def FermatTest():
    prime  = secrets.randbelow(10 ** 512)
    for i in range(100):
        a = secrets.randbelow(prime - 2)
        if sm(a, prime-1, prime) != 1:
            return prime,"composite"
    return prime,"prime"

def LargePrime():
    flag = "composite"
    while(flag == "composite"):
        prime,flag = FermatTest()
    return prime

# output file open
fout = open("./report.txt","w")

if(len(sys.argv) > 1 and sys.argv[1] == "-i"):
    p = int(input("請輸入p值: "))
    q = int(input("請輸入q值: "))
else:
    p = LargePrime()
    q = LargePrime()
n = p * q
phi = (p - 1) * (q - 1)
e = 0
for i in range(2,phi):
    if gcd(i,phi) == 1:
        e = i
        break

d = minv(e,phi)
fout.write("p值: " + str(p) + "\n")
fout.write("q值: " + str(q) + "\n")
fout.write("n值: " + str(n) + "\n")
fout.write("phi值: " + str(phi) + "\n")
fout.write("e值: " + str(e) + "\n")
fout.write("d值: " + str(d) + "\n")

# CRT implementation, RSA encryption, RSA decryption
dp = d % (p - 1)
dq = d % (q - 1)
qinv = minv(q,p)
message = int(input("請輸入plaintext: "))
ciphertext = sm(message,e,n)
fout.write("Ciphertext= " + str(ciphertext) + "\n")
m1 = sm(ciphertext,dp,p)
m2 = sm(ciphertext,dq,q)
h = (qinv * (m1 - m2)) % p
plaintext = m2 + h*q
fout.write("Plaintext= " + str(plaintext) + "\n")
fout.close()
