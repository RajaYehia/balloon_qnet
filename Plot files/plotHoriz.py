import matplotlib.pyplot as plt
import numpy as np

"""This scripts produces a plot of the transmissivity of the horizontal Balloon-To-Balloon channel for different height of the balloons
 using the txt outputs from HorizStudy.py"""


file1 = open("HorizSimu01.txt","r")
L = file1.read().splitlines()
key1 =[]
for i in L:
    key1.append(float(i))
file1.close()

file2 = open("HorizTheo01.txt","r")
L = file2.read().splitlines()
key2 =[]
for i in L:
    key2.append(float(i))
file2.close()

file3 = open("HorizSimu02.txt","r")
L = file3.read().splitlines()
key3 =[]
for i in L:
    key3.append(float(i))
file3.close()

file4 = open("HorizTheo02.txt","r")
L = file4.read().splitlines()
key4 =[]
for i in L:
    key4.append(float(i))
file4.close()

file5 = open("HorizSimu04.txt","r")
L = file5.read().splitlines()
key5 =[]
for i in L:
    key5.append(float(i))
file5.close()

file6 = open("HorizTheo04.txt","r")
L = file6.read().splitlines()
key6 =[]
for i in L:
    key6.append(float(i))
file6.close()

file7 = open("HorizSimu06.txt","r")
L = file7.read().splitlines()
key7 =[]
for i in L:
    key7.append(float(i))
file7.close()

file8 = open("HorizTheo06.txt","r")
L = file8.read().splitlines()
key8 =[]
for i in L:
    key8.append(float(i))
file8.close()

dist = [1,10,15,20,25,50,60,75,100,125,150,175,200,225,250,275,300,350,400]
plt.figure(figsize=(15,9)) 
plt.plot(dist,key1,label="Simulated, h=18", linestyle = '', marker = '*', markersize=10, color='m')
plt.plot(dist,key2,label="Theorical, h=18", color='m')

plt.plot(dist,key3,label="Simulated, h=23", linestyle = '', marker = '*', markersize=10, color='g')
plt.plot(dist,key4,label="Theorical, h=23", color='g')

plt.plot(dist,key5,label="Simulated, h=28", linestyle = '', marker = '*', markersize=10,color='r')
plt.plot(dist,key6,label="Theorical, h=28",color='r')

plt.plot(dist,key7,label="Simulated, h=33", linestyle = '', marker = '*', markersize=10,color='b')
plt.plot(dist,key8,label="Theorical, h=33",color='b')

plt.xlabel('distance between balloons (km) ',size=30)
plt.ylabel('Channel mean efficiency',size=30)
plt.legend(loc='upper right',prop={'size':24})
plt.tick_params(axis='both', labelsize=25)
plt.ylim(0,0.17)
plt.savefig("HorizStudy2.pdf", format = 'pdf')
plt.show()