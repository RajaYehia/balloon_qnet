import matplotlib.pyplot as plt
import numpy as np

"""This scripts produces a plot of the transmissivity of the Balloon-To-Ground downlink channel for different zenith angles
 using the txt outputs from ZenithStudy.py"""

file1 = open("ZenithBalloonSimu01.txt","r")
L = file1.read().splitlines()
key1 =[]
for i in L:
    key1.append(float(i))
file1.close()

file2 = open("ZenithBalloonTheo01.txt","r")
L = file2.read().splitlines()
key2 =[]
for i in L:
    key2.append(float(i))
file2.close()

file3 = open("ZenithBalloonSimu02.txt","r")
L = file3.read().splitlines()
key3 =[]
for i in L:
    key3.append(float(i))
file3.close()

file4 = open("ZenithBalloonTheo02.txt","r")
L = file4.read().splitlines()
key4 =[]
for i in L:
    key4.append(float(i))
file4.close()

file5 = open("ZenithBalloonSimu04.txt","r")
L = file5.read().splitlines()
key5 =[]
for i in L:
    key5.append(float(i))
file5.close()

file6 = open("ZenithBalloonTheo04.txt","r")
L = file6.read().splitlines()
key6 =[]
for i in L:
    key6.append(float(i))
file6.close()

file7 = open("ZenithBalloonSimu06.txt","r")
L = file7.read().splitlines()
key7 =[]
for i in L:
    key7.append(float(i))
file7.close()

file8 = open("ZenithBalloonTheo06.txt","r")
L = file8.read().splitlines()
key8 =[]
for i in L:
    key8.append(float(i))
file8.close()

file9 = open("ZenithBalloonSimu08.txt","r")
L = file9.read().splitlines()
key9 =[]
for i in L:
    key9.append(float(i))
file9.close()

file10 = open("ZenithBalloonTheo08.txt","r")
L = file10.read().splitlines()
key10 =[]
for i in L:
    key10.append(float(i))
file10.close()

dist = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,77,80]
y_error = 0.002

plt.figure(figsize=(15,9)) 
plt.plot(dist,key1,linestyle = '', marker = '*', markersize=10, color='m')
plt.plot(dist,key2,label="$h=18$ cm", color='m')

plt.plot(dist,key3,linestyle = '', marker = '*', markersize=10, color='g')
plt.plot(dist,key4,label="$h=23$ cm", color='g')

plt.plot(dist,key5,linestyle = '', marker = '*', markersize=10,color='r')
plt.plot(dist,key6,label="$h=28$ cm",color='r')

plt.plot(dist,key7,linestyle = '', marker = '*', markersize=10,color='b')
plt.plot(dist,key8,label="$h=33$ cm",color='b')

plt.plot(dist,key9,linestyle = '', marker = '*', markersize=10,color='y')
plt.plot(dist,key10,label="$h=38$ cm",color='y')

plt.xlabel('Zenith angle (degree) ',size=30)
plt.ylabel('Mean channel efficiency',size=30)
plt.legend(loc='upper right',prop={'size':24})
plt.tick_params(axis='both', labelsize=25)

plt.savefig("ZenithHeight.pdf", format = 'pdf')
plt.show()