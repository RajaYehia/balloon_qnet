import matplotlib.pyplot as plt
import numpy as np

"""This scripts produces a plot of the transmissivity of the vertical Balloon-To-Ground downlink channel for different initial beam waists
 using the txt outputs from W0Study.py"""


file1 = open("W0Simu01rx02.txt","r")
L = file1.read().splitlines()
key1 =[]
for i in L:
    key1.append(float(i))
file1.close()

file2 = open("W0Theo01rx02.txt","r")
L = file2.read().splitlines()
key2 =[]
for i in L:
    key2.append(float(i))
file2.close()

file3 = open("W0Simu02rx02.txt","r")
L = file3.read().splitlines()
key3 =[]
for i in L:
    key3.append(float(i))
file3.close()

file4 = open("W0Theo02rx02.txt","r")
L = file4.read().splitlines()
key4 =[]
for i in L:
    key4.append(float(i))
file4.close()

file5 = open("W0Simu03rx02.txt","r")
L = file5.read().splitlines()
key5 =[]
for i in L:
    key5.append(float(i))
file5.close()

file6 = open("W0Theo03rx02.txt","r")
L = file6.read().splitlines()
key6 =[]
for i in L:
    key6.append(float(i))
file6.close()

file7 = open("W0Simu04rx02.txt","r")
L = file7.read().splitlines()
key7 =[]
for i in L:
    key7.append(float(i))
file7.close()

file8 = open("W0Theo04rx02.txt","r")
L = file8.read().splitlines()
key8 =[]
for i in L:
    key8.append(float(i))
file8.close()
dist = range(18,38)
y_error = 0.01
plt.figure(figsize=(15,9)) 
plt.plot(dist,key2,label="$W_0=0.05$", color='m')
plt.plot(dist,key4,label="$W_0=0.1$", color='g')
plt.plot(dist,key6,label="$W_0=0.15$",color='r')
plt.plot(dist,key8,label="$W_0=0.2$",color='b')

plt.xlabel('Height (km) ',size=30)
plt.ylabel('Mean channel efficiency',size=30)
plt.legend(loc='best',prop={'size':24})
plt.tick_params(axis='both', labelsize=25)
plt.savefig("W0Transrx0.pdf", format = 'pdf')
plt.show()