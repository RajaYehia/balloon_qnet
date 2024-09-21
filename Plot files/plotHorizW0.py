import matplotlib.pyplot as plt
import numpy as np

"""This scripts produces a plot of the transmissivity of the horizontal Balloon-To-Balloon channel for different initial beam waists
 using the txt outputs from HorizW0Study.py"""


file1 = open("HorizSimuW001.txt","r")
L = file1.read().splitlines()
key1 =[]
for i in L:
    key1.append(float(i))
file1.close()

file2 = open("HorizTheoW001.txt","r")
L = file2.read().splitlines()
key2 =[]
for i in L:
    key2.append(float(i))
file2.close()

file3 = open("HorizSimuW002.txt","r")
L = file3.read().splitlines()
key3 =[]
for i in L:
    key3.append(float(i))
file3.close()

file4 = open("HorizTheoW002.txt","r")
L = file4.read().splitlines()
key4 =[]
for i in L:
    key4.append(float(i))
file4.close()

file5 = open("HorizSimuW004.txt","r")
L = file5.read().splitlines()
key5 =[]
for i in L:
    key5.append(float(i))
file5.close()

file6 = open("HorizTheoW004.txt","r")
L = file6.read().splitlines()
key6 =[]
for i in L:
    key6.append(float(i))
file6.close()

file7 = open("HorizSimuW006.txt","r")
L = file7.read().splitlines()
key7 =[]
for i in L:
    key7.append(float(i))
file7.close()

file8 = open("HorizTheoW006.txt","r")
L = file8.read().splitlines()
key8 =[]
for i in L:
    key8.append(float(i))
file8.close()

dist = [1,10,15,20,25,50,60,75,100,125,150,175,200,225,250,275,300,350,400]
plt.figure(figsize=(15,9)) 
plt.plot(dist,key1,linestyle = '', marker = '*', markersize=10, color='m')
plt.plot(dist,key2,label="$W_{0}=0.05$", color='m')

plt.plot(dist,key3,linestyle = '', marker = '*', markersize=10, color='g')
plt.plot(dist,key4,label="$W_{0}=0.1$", color='g')

plt.plot(dist,key5,linestyle = '', marker = '*', markersize=10,color='r')
plt.plot(dist,key6,label="$W_{0}=0.1$5",color='r')

plt.plot(dist,key7,linestyle = '', marker = '*', markersize=10,color='b')
plt.plot(dist,key8,label="$W_{0}=0.2$",color='b')

plt.xlabel('Distance between balloons (km) ',size=30)
plt.ylabel('Mean channel efficiency',size=30)
plt.legend(loc='upper right',prop={'size':24})
plt.tick_params(axis='both', labelsize=25)
plt.ylim(0,0.17)
plt.savefig("HorizStudyW0.pdf", format = 'pdf')
plt.show()