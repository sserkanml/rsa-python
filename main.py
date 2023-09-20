import math
import sys
# step 1
# two primary numbers
p = 3
q = 7

# step 2

n = p*q
print("n =", n)

# step 3
# totient numbers
phi = (p-1)*(q-1)

# step 4
e = 2
while(e < phi):
    if (math.gcd(e, phi) == 1):
        break
    else:
        e += 1

print("e =", e)
# step 5
k = 2
d = ((k*phi)+1)/e
print("d =", d)
print(f'Public key: {e, n}')
print(f'Private key: {d, n}')

# plain text
msg = int(sys.argv[1])
print(f'Original message:{msg}')

# encryption
C = pow(msg, e)
C = math.fmod(C, n)
print(f'Encrypted message: {C}')

# decryption
M = pow(C, d)
M = math.fmod(M, n)

print(f'Decrypted message: {M}')
