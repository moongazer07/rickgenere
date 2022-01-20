import time
def rickgenere(pt, k):
    #Flipped dictionaries.
    d={0:'A',  1:'B',  2:'C',  3:'D',  4:'E',  5:'F',  6:'G',  7:'H',  8:'I',  9:'J',  10:'K',  11:'L',  12:'M',  13:'N',  14:'O',  15:'P',  16:'Q',  17:'R',  18:'S',  19:'T',  20:'U',  21:'V',  22:'W',  23:'X',  24:'Y',  25:'Z'}
    d1={'never ':0, 'gonna ':1, 'give ':2, 'you ':3, 'up ':4, 'NEVER ':5, 'GONNA ':6, 'let ':7, 'YOU ':8, 'down ':9, 'Never ':10, 'Gonna ':11, 'turn ':12, 'around ':13, 'and ':14, 'desert ':15, 'You ':16, 'NEver ':17, 'GOnna ':18, 'tell ':19, 'a ':20, 'lie ':21, 'AND ':22, 'hurt ':23, 'YoU ':24, 'rickroll ':25}
    
    #Reverse back into actual letters rather than RickRoll-Text.   
    ct=""    
    ptwrd=pt.split(" ")
    for x in ptwrd:
      ct = ct + (d.get(d1.get(x+" ")))
    print("Using CipherText: ", ct)

    
    decoded_chars = []
    orig_text = [] 
    for i in range(len(ct)): 
      x = (ord(ct[i]) - ord(key[i]) + 26) % 26
      x += ord('A') 
      orig_text.append(chr(x)) 
      print("PlainText:", "" . join(orig_text))
    
    
ptxt=input("Enter the rickgenere Text : ")
key=input("Enter the decryption key : ")
key=key.upper().strip()
ptxt=ptxt.strip()
key=key*len(ptxt)
rickgenere(ptxt, key)      
print("The program will close in 180 seconds so you can copy and paste")
time.sleep(180)

