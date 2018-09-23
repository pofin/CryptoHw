#Small program that shows part of a Diff Crypto attack
from bitstring import BitArray

#Sbox S0
def sbox(inp):
    S0 = [[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]]
    tmp = str(inp.bin)
    col = int(''.join(tmp[i] for i in [1,2]),2)    
    row = int(''.join(tmp[i] for i in [0,3]),2)
    return S0[row][col]    
    

if __name__ == '__main__':
    Table = []
    for i in range(16):
        Table.append([0,0,0,0])
    
    #sets of possible input values with input XOR 5
    set5 = [set(),set(),set(),set()]
    
    #Builds Distribution table
    for i in range(16):
        for j in range(16):
            inp = i^j
            out = sbox(BitArray(uint=i,length=4))^sbox(BitArray(uint=j,length=4))
            Table[inp][out] += 1
            #collects possible input values for XOR 5
            if inp == 5:
                set5[out].update([i,j])
    
    #prints table
    for i in range(16):        
        print(Table[i])
    
    print(set5)
    
    #known that (0,5) XORs to 5 and known the output XOR is 3 
    #From slide 36 S1K = S1I XOR S1E
    #So the possible keys are the XOR of 0,5 with the values of
    #Xor 5 with output D which equals 3 here
    pkeys1 = set()
    for i in set5[3]:
        pkeys1.add(i^0)
        pkeys1.add(i^5)
    
    print(pkeys1)
     
    #now it is also known 2,7 Xors to 5 and the output Xor is 0
    #same operation as before
    pkeys2 = set()
    for i in set5[0]:
        pkeys2.add(i^2)
        pkeys2.add(i^7)    
    
    print(pkeys2)
    
    #The union of both these sets is the set of possible keys
    print('Set of possible keys:',pkeys1&pkeys2)
    
    #Continue with more to narrow down and get the key