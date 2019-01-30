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

def add(x,y):
        maxlen = max(len(x), len(y))
        result = ''
        carry = 0

        for i in range(maxlen-1, -1, -1):
            r = carry
            r += 1 if x[i] == '1' else 0
            r += 1 if y[i] == '1' else 0

            # r can be 0,1,2,3 (carry + x[i] + y[i])
            # and among these, for r==1 and r==3 you will have result bit = 1
            # for r==2 and r==3 you will have carry = 1

            result = ('1' if r % 2 == 1 else '0') + result
            carry = 0 if r < 2 else 1

        if carry !=0 : result = '1' + result

        return result.zfill(maxlen)


A=str(decbin(8))
B=str(decbin(16))
print(A,"+",B,"=",add(A,B))
#Addition binaire
#bin1=decbin(56)
#bin2=decbin(64)
#bin3=[]
#for i in range(8) :
#    bintemp=(bin1[i]+bin2[i])%2
#    if bintemp==2 :
#        bin3.append(0)
#    else :
#        bin3.append(bintemp)
#print(bin3)
