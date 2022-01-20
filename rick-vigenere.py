import time

def rickgenere(pt, k):
    d={'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16, 'R':17, 'S':18, 'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25}
    d1={0:'never ', 1:'gonna ', 2:'give ', 3:'you ', 4:'up ', 5:'NEVER ', 6:'GONNA ', 7:'let ', 8:'YOU ', 9:'down ', 10:'Never ', 11:'Gonna ', 12:'turn ', 13:'around ', 14:'and ', 15:'desert ', 16:'You ', 17:'NEver ', 18:'GOnna ', 19:'tell ', 20:'a ', 21:'lie ', 22:'AND ', 23:'hurt ', 24:'YoU ', 25:'rickroll '}        
    ct=""
    j=0;
    for i in range(len(pt)):       
       if(pt[i]!=' '):
               if(j<len(k)):
                   ct=ct+d1[(d[pt[i]]+d[k[j]])%26]
               else:
                   j=j%len(k)
                   ct=ct+d1[(d[pt[i]]+d[k[j]])%26]
               j=j+1
       else:
            continue
    print (ct)
    
    
ptxt=input("Enter the plain text : ")
key1=input("Enter the key : ")
ptxt=ptxt.upper()
key1=key1.upper()
rickgenere(ptxt, key1)      
print("The program will close in 180 seconds so you can copy and paste")
time.sleep(180)
