import matplotlib.pyplot as plt
import numpy as np

"""This scripts produces a plot of the mean channel efficiency of the vertical Balloon-To-Ground downlink channel for different maximal correction of 
    the AO system using the txt outputs from AOStudy.py"""

file0 = open("AOballoonMaxi.txt","r")
L = file0.read().splitlines()
key0 =[]
for i in L:
    key0.append(float(i))
file0.close()

file1 = open("AOballoonSimu2.txt","r")
L = file1.read().splitlines()
key1 =[]
for i in L:
    key1.append(float(i))
file1.close()

file2 = open("AOballoonTheo2.txt","r")
L = file2.read().splitlines()
key2 =[]
for i in L:
    key2.append(float(i))
file2.close()

file3 = open("AOballoonSimu3.txt","r")
L = file3.read().splitlines()
key3 =[]
for i in L:
    key3.append(float(i))
file3.close()

file4 = open("AOballoonTheo3.txt","r")
L = file4.read().splitlines()
key4 =[]
for i in L:
    key4.append(float(i))
file4.close()

file5 = open("AOballoonSimu4.txt","r")
L = file5.read().splitlines()
key5 =[]
for i in L:
    key5.append(float(i))
file5.close()

file6 = open("AOballoonTheo4.txt","r")
L = file6.read().splitlines()
key6 =[]
for i in L:
    key6.append(float(i))
file6.close()

file7 = open("AOballoonSimu5.txt","r")
L = file7.read().splitlines()
key7 =[]
for i in L:
    key7.append(float(i))
file7.close()

file8 = open("AOballoonTheo5.txt","r")
L = file8.read().splitlines()
key8 =[]
for i in L:
    key8.append(float(i))
file8.close()

file9 = open("AOballoonSimu6.txt","r")
L = file9.read().splitlines()
key9 =[]
for i in L:
    key9.append(float(i))
file9.close()

file10 = open("AOballoonTheo6.txt","r")
L = file10.read().splitlines()
key10 =[]
for i in L:
    key10.append(float(i))
file10.close()

file11 = open("AOballoonSimu7.txt","r")
L = file11.read().splitlines()
key11 =[]
for i in L:
    key11.append(float(i))
file11.close()

file12 = open("AOballoonTheo7.txt","r")
L = file12.read().splitlines()
key12 =[]
for i in L:
    key12.append(float(i))
file12.close()

file13 = open("AOballoonSimu8.txt","r")
L = file13.read().splitlines()
key13 =[]
for i in L:
    key13.append(float(i))
file13.close()

file14 = open("AOballoonTheo8.txt","r")
L = file14.read().splitlines()
key14 =[]
for i in L:
    key14.append(float(i))
file14.close()

file15 = open("AOballoonSimu9.txt","r")
L = file15.read().splitlines()
key15 =[]
for i in L:
    key15.append(float(i))
file15.close()

file16 = open("AOballoonTheo9.txt","r")
L = file16.read().splitlines()
key16 =[]
for i in L:
    key16.append(float(i))
file16.close()

file17 = open("AOballoonSimu10.txt","r")
L = file17.read().splitlines()
key17 =[]
for i in L:
    key17.append(float(i))
file17.close()

file18 = open("AOballoonTheo10.txt","r")
L = file18.read().splitlines()
key18 =[]
for i in L:
    key18.append(float(i))
file18.close()


dist = range(18,38)
plt.figure(figsize=(15,9)) 
plt.plot(dist,key1, linestyle = '', marker = '*', markersize=10, color='m')
plt.plot(dist,key2,label="$N_{\\mathrm{AO}} = 2$", color='m')

plt.plot(dist,key3, linestyle = '', marker = '*', markersize=10, color='y')
plt.plot(dist,key4,label="$N_{\\mathrm{AO}} = 3$", color='y')

plt.plot(dist,key5, linestyle = '', marker = '*', markersize=10, color='g')
plt.plot(dist,key6,label="$N_{\\mathrm{AO}} = 4$", color='g')

plt.plot(dist,key7, linestyle = '', marker = '*', markersize=10, color='c')
plt.plot(dist,key8,label="$N_{\\mathrm{AO}} = 5$", color='c')

plt.plot(dist,key9, linestyle = '', marker = '*', markersize=10,color='r')
plt.plot(dist,key10,label="$N_{\\mathrm{AO}} = 6$",color='r')

plt.plot(dist,key11, linestyle = '', marker = '*', markersize=10, color='skyblue')
plt.plot(dist,key12,label="$N_{\\mathrm{AO}} = 7$", color='skyblue')

plt.plot(dist,key13, linestyle = '', marker = '*', markersize=10, color='deeppink')
plt.plot(dist,key14,label="$N_{\\mathrm{AO}} = 8$", color='deeppink')

plt.plot(dist,key15, linestyle = '', marker = '*', markersize=10, color='darkorange')
plt.plot(dist,key16,label="$N_{\\mathrm{AO}} = 9$", color='darkorange')

plt.plot(dist,key17,linestyle = '', marker = '*', markersize=10, color='mediumpurple')
plt.plot(dist,key18,label="$N_{\\mathrm{AO}} = 10$", color='mediumpurple')

plt.xlabel('Height (km) ',size=30)
plt.ylabel('Mean channel efficiency',size=30)
plt.legend(loc='best',prop={'size':24}, ncol=2)
plt.tick_params(axis='both', labelsize=25)
plt.ylim(0.1)
plt.savefig("AOstudy.pdf", format = 'pdf')
plt.show()