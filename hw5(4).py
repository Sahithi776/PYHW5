#Write two decorator functions encrypt and decrypt
#When applied as a decorator,the encrypt function will encrypt the returning string
#(assume it is always a string) and decrypt function will decrypt 
#the encrypted string back to its original value.
def Encryption(s,k):
    encstr=""
    for i in s:
        if(ord(i))>=65 and (ord(i)<=90):
            temp=(ord(i)+k)
            if temp>90:
                temp=temp%90+64
            encstr=encstr+chr(temp)
        elif(ord(i))>=97 and (ord(i)<=122):
            temp=(ord(i)+k)
            if temp>122:
                temp=temp%122+96
            encstr=encstr+chr(temp)
        else:
            encstr=encstr+chr(ord(i)+k)
    return encstr
def Decryption(k):
    p=Encryption(s,k)
    decstr=""
    for i in p:
        if((ord(i))>=65) and (ord(i))<=90:
            decstr=decstr+chr((ord(i) - k-65) % 26 + 65)
        elif((ord(i))>=97) and (ord(i))<=122:
            decstr=decstr+chr((ord(i) - k - 97) % 26 + 97)
        else:
            decstr=decstr+chr(ord(i)-k)
    return decstr
print("Enter the string to Encrypt and decrypt : ")
s=input()
print("Enter any digits to view encrypted and decrypted String: ")
k=int(input())
k=k%26
print("Encrypted String : ",Encryption(s,k))
print("Decrypted String : ",Decryption(k))











