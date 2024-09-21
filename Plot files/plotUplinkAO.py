import matplotlib.pyplot as plt
import numpy as np

"""This scripts produces a plot of the transmissivity of the vertical Ground-To-Balloon uplink channel for different level of correction of the AO system
 using the txt outputs from UplinkStudy.py"""

file7 = open("UplinkAOSimu5.txt","r")
L = file7.read().splitlines()
key7 =[]
for i in L:
    key7.append(float(i))
file7.close()

file8 = open("UplinkAOTheo5.txt","r")
L = file8.read().splitlines()
key8 =[]
for i in L:
    key8.append(float(i))
file8.close()

file9 = open("UplinkAOSimu6.txt","r")
L = file9.read().splitlines()
key9 =[]
for i in L:
    key9.append(float(i))
file9.close()

file10 = open("UplinkAOTheo6.txt","r")
L = file10.read().splitlines()
key10 =[]
for i in L:
    key10.append(float(i))
file10.close()

file11 = open("UplinkAOSimu7.txt","r")
L = file11.read().splitlines()
key11 =[]
for i in L:
    key11.append(float(i))
file11.close()

file12 = open("UplinkAOTheo7.txt","r")
L = file12.read().splitlines()
key12 =[]
for i in L:
    key12.append(float(i))
file12.close()

file13 = open("UplinkAOSimu8.txt","r")
L = file13.read().splitlines()
key13 =[]
for i in L:
    key13.append(float(i))
file13.close()

file14 = open("UplinkAOTheo8.txt","r")
L = file14.read().splitlines()
key14 =[]
for i in L:
    key14.append(float(i))
file14.close()

file15 = open("UplinkAOSimu9.txt","r")
L = file15.read().splitlines()
key15 =[]
for i in L:
    key15.append(float(i))
file15.close()

file16 = open("UplinkAOTheo9.txt","r")
L = file16.read().splitlines()
key16 =[]
for i in L:
    key16.append(float(i))
file16.close()

file17 = open("UplinkAOSimu10.txt","r")
L = file17.read().splitlines()
key17 =[]
for i in L:
    key17.append(float(i))
file17.close()

file18 = open("UplinkAOTheo10.txt","r")
L = file18.read().splitlines()
key18 =[]
for i in L:
    key18.append(float(i))
file18.close()



dist = range(18,38)
plt.figure(figsize=(15,9)) 

plt.plot(dist,key7, linestyle = '', marker = '*', markersize=10, color='c')
plt.plot(dist,key8,label="$N_{\\mathrm{AO}} = 5$", color='c')

plt.plot(dist,key9, linestyle = '', marker = '*', markersize=10,color='r')
plt.plot(dist,key10,label="$N_{\\mathrm{AO}} = 6$",color='r')

plt.plot(dist,key11, linestyle = '', marker = '*', markersize=10, color='k')
plt.plot(dist,key12,label="$N_{\\mathrm{AO}} = 7$", color='k')

plt.plot(dist,key13, linestyle = '', marker = '*', markersize=10, color='m')
plt.plot(dist,key14,label="$N_{\\mathrm{AO}} = 8$", color='m')

plt.plot(dist,key15, linestyle = '', marker = '*', markersize=10, color='y')
plt.plot(dist,key16,label="$N_{\\mathrm{AO}} = 9$", color='y')

plt.plot(dist,key17,linestyle = '', marker = '*', markersize=10, color='g')
plt.plot(dist,key18,label="$N_{\\mathrm{AO}} = 10$", color='g')


plt.xlabel('Height (km) ',size=30)
plt.ylabel('Mean channel efficiency',size=30)
plt.legend(loc='best',prop={'size':24})
plt.tick_params(axis='both', labelsize=25)

plt.savefig("UplinkAOstudy.pdf", format = 'pdf')
plt.show()