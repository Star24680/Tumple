def Palindrome(R):
    E= len(R)-1
    S=0
    while (S<E):
        if (R[S]!=R[E]):
            return False
        S+=1
        E-=1
    return True
R=(2,4,4,0,4,2,2)
if (Palindrome(R)):
    print("This tuple is officially flip flip")
else:
    print("This tuple has not gained title of flip flop")