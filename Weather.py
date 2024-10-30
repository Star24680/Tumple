Weather=(1,0,0,0,1,1,0)
S=0
R=0
for i in range(0,7):
    if (Weather[i]==0):
        R+=1
    else:
        S+=1
if (S>R):
    print("Good weather")
else:
    print("Bad Weather")