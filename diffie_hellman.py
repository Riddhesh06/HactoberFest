p = int(input("Enter prime number : "))
g = int(input("Enter primitive root : "))
Xa = int(input("Enter private key of A : "))
Xb = int(input("Enter private key of B : "))

while(Xa >= p):
    Xa = input("Enter a private key for A less than the prime number.")
while(Xb >= p):
    Xb = input("Enter a private key for B less than the prime number.")

A = pow(g,Xa,p)
B = pow(g,Xb,p)

Ka = pow(B,Xa,p)
Kb = pow(A,Xb,p)

print("Public key of A is " + str(A))
print("Public key of B is " + str(B))
print("Symmetric key of A is " + str(Ka))
print("Symmetric key of B is " + str(Kb))
