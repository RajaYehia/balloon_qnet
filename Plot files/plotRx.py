import matplotlib.pyplot as plt
import numpy as np

"""This scripts produces a plot of the transmissivity of the vertical Balloon-To-Ground downlink channel for different apertures of the receiving telescope
 using the txt outputs from RxStudy.py"""

file0 = open("HeightballoonSimu00.txt","r")
L = file0.read().splitlines()
key0 =[]
for i in L:
    key0.append(float(i))
file0.close()

file01 = open("HeightballoonTheo00.txt","r")
L = file01.read().splitlines()
key01 =[]
for i in L:
    key01.append(float(i))
file01.close()

file1 = open("HeightballoonSimu01.txt","r")
L = file1.read().splitlines()
key1 =[]
for i in L:
    key1.append(float(i))
file1.close()

file2 = open("HeightballoonTheo01.txt","r")
L = file2.read().splitlines()
key2 =[]
for i in L:
    key2.append(float(i))
file2.close()

file3 = open("HeightballoonSimu02.txt","r")
L = file3.read().splitlines()
key3 =[]
for i in L:
    key3.append(float(i))
file3.close()

file4 = open("HeightballoonTheo02.txt","r")
L = file4.read().splitlines()
key4 =[]
for i in L:
    key4.append(float(i))
file4.close()

file5 = open("HeightballoonSimu04.txt","r")
L = file5.read().splitlines()
key5 =[]
for i in L:
    key5.append(float(i))
file5.close()

file6 = open("HeightballoonTheo04.txt","r")
L = file6.read().splitlines()
key6 =[]
for i in L:
    key6.append(float(i))
file6.close()

file7 = open("HeightballoonSimu06.txt","r")
L = file7.read().splitlines()
key7 =[]
for i in L:
    key7.append(float(i))
file7.close()

file8 = open("HeightballoonTheo06.txt","r")
L = file8.read().splitlines()
key8 =[]
for i in L:
    key8.append(float(i))
file8.close()
dist = range(18,38)
y_error = 0.002

plt.figure(figsize=(15,9)) 
plt.plot(dist,key0, linestyle = '', marker = '*', markersize=10, color='y')
plt.plot(dist,key01,label="$D_{\\mathrm{Rx}}=20$ cm", color='y')

plt.plot(dist,key1, linestyle = '', marker = '*', markersize=10, color='m')
plt.plot(dist,key2,label="$D_{\\mathrm{Rx}}=30$ cm", color='m')

plt.plot(dist,key3, linestyle = '', marker = '*', markersize=10, color='g')
plt.plot(dist,key4,label="$D_{\\mathrm{Rx}}=40$ cm", color='g')

plt.plot(dist,key5, linestyle = '', marker = '*', markersize=10,color='r')
plt.plot(dist,key6,label="$D_{\\mathrm{Rx}}=50$ cm",color='r')

plt.plot(dist,key7, linestyle = '', marker = '*', markersize=10,color='b')
plt.plot(dist,key8,label="$D_{\\mathrm{Rx}}=60$ cm",color='b')

plt.xlabel('Height (km) ',size=30)
plt.ylabel('Mean channel efficiency',size=30)
plt.legend(loc='best',prop={'size':24})
plt.tick_params(axis='both', labelsize=25)

plt.savefig("HeightStudy.pdf", format = 'pdf')
plt.show()