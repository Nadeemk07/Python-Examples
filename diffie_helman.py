from random import randint

#Prime Number 
Q = 23

#Primitive Root
alpha = 5

#Private Key Alice
Xa = 6

#Publiv Key Alice
Ya = (alpha**Xa)%Q

#Private Key Bob
Xb = 15

#Public Key Bob
Yb = (alpha**Xb)%Q

#Secret Key
Ka = (Yb**Xa)%Q #Alice
Kb = (Ya**Xb)%Q #Bob

print("Prime Number                 : ",Q)
print("Primitive Root               : ",alpha)
print("Alice's Private Key          : ",Xa)
print("Alice's Public Key           : ",Ya)
print("Bob's Private Key            : ",Xb)
print("Bob's Public Key             : ",Yb)
print("Alice's Secret Key           : ",Ka)
print("Bob's Secret Key             : ",Ka)