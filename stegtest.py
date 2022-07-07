import numpy as np
import matplotlib.pyplot as py
import matplotlib.image as ig
i=ig.imread("D:\endgame.jpg")
s=py.imshow(i)
py.show()
ir=np.array(i)
ir1=np.array(i)
d={}
c={}
for i in range (255):
    d[chr(i)]=i
    c[i]=chr(i)
p=0
q=0
r=0
t=input("enter the text you want to encrypt")
for x in range(len(t)):
    k=(d[t[x]])
    #i[p,q,r]=k
    ir[x][x][1]+=k
    #p+=1
    #q+=1
im=ig.imsave("RealEncrypted.jpeg",ir)
e1=ig.imread("RealEncrypted.jpeg")
e1s=py.imshow(e1)
py.show()
print("\n\nEncryption completed")
i=int(input("\n\nenter 1 for decryption "))
if(i==1):
    dt=""
    ir2=ir
    for x in range(len(t)):
        dt+=c[ir2[x][x][1]-ir1[x][x][1]]
        ir2[x][x][1]-=(ir2[x][x][1]-ir1[x][x][1])
    print('\n\nThe encrypted text is\n',dt)
    print("The recovered image is displayed below")
    #imat2=imat2.reshape(imat.shape)
    im2=ig.imsave("RealRecovered.jpeg",ir2)
    e2=ig.imread("RealRecovered.jpeg")
    e2s=py.imshow(e2)
    py.show()
else:
    print("Process completed")


