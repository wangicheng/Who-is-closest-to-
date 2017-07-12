import math
number=math.pi
g=float(10)
x=int(0)
y=int(0)

"""sqrt(n)-number"""
def sqr_n(n):
    global y,g
    ans=abs((math.sqrt(n)-math.sqrt(n)//1)+3)
    if abs(ans-math.pi)<g :
        g=abs(ans-math.pi)
        print("√"+str(n)+"-"+str(int(math.sqrt(n)//1-3))+"="+str(ans))
        
"""sqrt(n)-sqrt(m)"""
def sqr_sqr(n):
    global y,g
    m=int(pow(math.sqrt(n)-number,2))
    ans=math.sqrt(n)-math.sqrt(m)
    if abs(ans-math.pi)<g :
        g=abs(ans-math.pi)
        print("√"+str(n)+"-"+"√"+str(m)+"="+str(ans))
for x in range(1,1000001):
    sqr_n(x)
    sqr_sqr(x)
        
