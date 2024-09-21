from QEuropeFunctions import *
import lowtran
import transmittance
import cn2
from free_space_losses import  DownlinkChannel, compute_channel_length, CachedChannel, lut_zernike_index_pd
import multiprocessing as mlp
import os
import functools as fnct


'''This script calculates the mean transmittance of a Balloon-to-Ground downlink channel for a varying zenith angle and different altitudes of the balloon. 
    It creates 5 ZenithBalloonSimuX.txt files with the theoretical mean transmittance of the channel and 5 ZenithBalloonSimuX.txt files with 
    the simulated mean transmittance of each of the considered altitudes.
'''

# Parameters

wavelength = 1550e-9

ground_station_alt = 0.020 #Altitude of the receiving telescope
W0 = 0.1 #Initial Beam Waist
obs_ratio_ground = 0.3 #Obscuration ratio of the receiving telescope 
n_max_ground = 6 #Maximum radial index of correction of AO system 
Cn0 = 9.6*10**(-14) #Reference index of refraction structure constant at ground level
u_rms = 10 #Wind speed
pointing_error = 1e-6 #Pointing error variance
Qonnector_meas_succ = 0.85 #Detector efficiency at the receiver
tracking_efficiency = 0.8 #Tracking efficiency
rx_aperture = 0.4 #Aperture of the receiving telescope

h_balloons = [18,23,28,33,38] #Altitude of the balloon
zenith_angle = [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,77,80]
simtime = 500000

#Theoretical mean transmittance 

def heightTheo(h_balloons, zenith_angle):
    
    height_balloon = compute_channel_length(ground_station_alt, h_balloons, zenith_angle)
    transmittance_down = transmittance.slant(ground_station_alt, h_balloons, wavelength*1e9, zenith_angle)

   
    downlink_channel = DownlinkChannel(W0, rx_aperture, obs_ratio_ground, n_max_ground, Cn0, u_rms, wavelength, ground_station_alt, h_balloons, zenith_angle,
                                            pointing_error = pointing_error, tracking_efficiency = tracking_efficiency, Tatm = transmittance_down)
    eta = np.arange(1e-7, 1, 0.001)
    mean = downlink_channel._compute_mean_channel_efficiency(eta, height_balloon, detector_efficiency = Qonnector_meas_succ)
    print("Theoretical mean " + str(mean) + " at zenith angle " + str(zenith_angle))
    return mean
    
    
#Simulated mean transmittance

def heightSimu(h_balloons,zenith_angle):
    
    height_balloon = compute_channel_length(ground_station_alt, h_balloons, zenith_angle)
    transmittance_down = transmittance.slant(ground_station_alt, h_balloons, wavelength*1e9, zenith_angle)
    # Initialize network
    net = QEurope("Europe")

    # Create quantum City 1
    net.Add_Qonnector("QonnectorCity1")

    # Create drone 1
    net.Add_Qonnector("QonnectorDroneCity1")


    # Create channels
    downlink_channel = DownlinkChannel(W0, rx_aperture, obs_ratio_ground, n_max_ground, Cn0, u_rms, wavelength, ground_station_alt, h_balloons, zenith_angle,
                                            pointing_error = pointing_error, tracking_efficiency = tracking_efficiency, Tatm = transmittance_down)
        
    a = downlink_channel._compute_loss_probability(height_balloon,math.ceil(simtime/Qonnector_init_time ))

    downlink = CachedChannel(a)
    
    # Connect nodes
    net.connect_qonnectors("QonnectorCity1", "QonnectorDroneCity1", distance = height_balloon, loss_model = downlink)

    # Get node instances
    city = net.network.get_node("QonnectorCity1")
    balloon = net.network.get_node("QonnectorDroneCity1")

    # BB84 from city 1 to drone 1
    send = SendBB84(city, Qonnector_init_succ, Qonnector_init_flip, balloon)
    send.start()
    receive = ReceiveProtocol(balloon, Qonnector_meas_succ, Qonnector_meas_flip, True, city)
    receive.start()


    # Run simulation
    stat = ns.sim_run(duration = simtime)

    # Display and results 
    L1 = Sifting(balloon.QlientKeys[city.name], city.QlientKeys[balloon.name])
    chan_eff = len(city.QlientKeys[balloon.name])/len(balloon.QlientKeys[city.name])

    print("Zenith angle : " + str(zenith_angle) + "degree")
    print("Height of the balloon : " + str(h_balloons) + "cm")
    print("Number of qubits sent by the Balloon: " +str(len(balloon.QlientKeys[city.name])) )
    print("Number of qubits received by Bob (Qlient): " +str(len(city.QlientKeys[balloon.name])) )
    print("Channel efficiency : "+str(chan_eff) + " bits per channel use")
    
    return chan_eff

    
#Function to parallelize

def Study(zenith_angle):
    res = []
    for h in h_balloons:
        res.append([h,rx_aperture,'simu',heightSimu(h,zenith_angle),'theo',heightTheo(h, zenith_angle)])
    return res


#Parallelized version
mlp.set_start_method('fork')
pool_threads = os.cpu_count() - 1
pool = mlp.Pool(pool_threads)
trans = pool.map(fnct.partial(Study), zenith_angle)
pool.close()
pool.join() 


#Data saving    
            
Simu01 = open("ZenithBalloonSimu01.txt","w")
Theo01 = open("ZenithBalloonTheo01.txt","w")
Simu02 = open("ZenithBalloonSimu02.txt","w")
Theo02 = open("ZenithBalloonTheo02.txt","w")
Simu04 = open("ZenithBalloonSimu04.txt","w")
Theo04 = open("ZenithBalloonTheo04.txt","w")
Simu06 = open("ZenithBalloonSimu06.txt","w")
Theo06 = open("ZenithBalloonTheo06.txt","w")
Simu08 = open("ZenithBalloonSimu08.txt","w")
Theo08 = open("ZenithBalloonTheo08.txt","w")

for height in trans:
    for rx in height:
        if rx[0]==18:
            Simu01.write(str(rx[3])+ "\n") 
            Theo01.write(str(rx[5])+ "\n")
        if rx[0]==23:
            Simu02.write(str(rx[3])+ "\n") 
            Theo02.write(str(rx[5])+ "\n")
        if rx[0]==28:
            Simu04.write(str(rx[3])+ "\n") 
            Theo04.write(str(rx[5])+ "\n")
        if rx[0]==33:
            Simu06.write(str(rx[3])+ "\n") 
            Theo06.write(str(rx[5])+ "\n")
        if rx[0]==38:
            Simu08.write(str(rx[3])+ "\n") 
            Theo08.write(str(rx[5])+ "\n")

Simu01.close()
Simu02.close()
Simu04.close()
Simu06.close()
Simu08.close()
Theo01.close()
Theo02.close()
Theo04.close()
Theo06.close()
Theo08.close()


