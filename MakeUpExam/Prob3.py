import random
import math

def millrab(lis):
    result = []
    for j in range(len(lis)):
        prime = True
        n = lis[j]
        k = 0
        q = n-1
        
        if n%2 == 0:
            result.append(False)
            continue        
        
        while True:
            if q%2 == 0:
                k += 1
                q = int(q/2)
            else:
                break
         
        for i in range(10):  
            if (not prime):
                break
            a = random.randint(2,n-1)
            x = pow(a,q,n)
            if x == 1: 
                continue
            
            for t in range(k):
                y = pow(a,((pow(2,t))*q),n)
                if y != (n-1):
                    prime = False
                    break                    
        
        result.append(prime)

    return result


def g(x):
    return pow(x,2)+1

def pollrho(n):
    x = 2
    y = 2
    d = 1
    
    while d == 1:
        x = g(x)
        y = g(g(y))
        d = math.gcd(abs(x-y),n)

    if d == n:
        return 'failure'
    else:
        return (d,int(n/d))



if __name__ == '__main__':
    print(millrab([31531,520482,485827,15485863]))
    
    #only factor 520482 since other 3 are prime
    print(pollrho(520482))
    