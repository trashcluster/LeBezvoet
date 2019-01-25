#Rotation
def rotation(t) :
    S=[]
    S.append(t[-1])
    for i in range(9) :
        S.append(t[i])
    return S
T=[]
S=[]
T=range(10)
print(rotation(T))

#Décimal --> binaire
def decbin(n) :
    bits = []
    bits.append(n%2)
    while n > 1 :
        n = n // 2
        bits.append(n%2)
    while len(bits)!=8 :
        bits.append(0)
    bits.reverse()
    return bits

#Addition binaire
bin1=decbin(56)
bin2=decbin(64)
bin3=[]
for i in range(8) :
    bintemp=(bin1[i]+bin2[i])%2
    if bintemp==2 :
        bin3.append(0)
    else :
        bin3.append(bintemp)
print(bin3)
