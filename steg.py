import numpy as np
import pandas as pd
import matplotlib.pyplot as py
import matplotlib.image as ig
i=ig.imread("D:\endgame.jpg")
s=py.imshow(i)
py.show()
imat=np.array(i)
s=imat.shape
imat1=imat.flatten()
imate=imat.flatten()
print(imat.shape)
d={}
c={}
for i in range (255):
    d[chr(i)]=i
    c[i]=chr(i)


t=input("enter the text you want to encrypt")
for i in range(len(t)):
    x=int(d[t[i]]%255)
    imat1[i]+=x
imat1=imat1.reshape(imat.shape)

print(imat1.shape)
im=ig.imsave("Encrypted.jpeg",imat1)
e1=ig.imread("Encrypted.jpeg")
e1s=py.imshow(e1)
py.show()

print("\n\nEncryption completed")
i=int(input("\n\nenter 1 for decryption "))
if(i==1):
    imat2=imat1.flatten()
    dt=""
    for i in range(len(t)):
        dt+=c[imat2[i]-imate[i]]
        imat2[i]-=(imat2[i]-imate[i])
    print('\n\nThe encrypted thext is\n',dt)
    print("The recovered image is displayed below")
    imat2=imat2.reshape(imat.shape)
    im2=ig.imsave("Recovered.jpeg",imat2)
    e2=ig.imread("Recovered.jpeg")
    e2s=py.imshow(e2)
    py.show()
else:
    print("Process completed")








