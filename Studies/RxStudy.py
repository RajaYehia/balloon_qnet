from QEuropeFunctions import *
import lowtran
import transmittance
import cn2
from free_space_losses import  DownlinkChannel, compute_channel_length, CachedChannel, lut_zernike_index_pd
import multiprocessing as mlp
import os
import functools as fnct


'''This script calculates the mean transmittance of a Balloon-to-Ground vertical downlink channel for different altitudes of the balloon. 
    It creates 4 HeightballoonTheo0X.txt files with the theoretical mean transmittance of the channel and 4 HeightballoonSimu0X.txt files with 
    the simulated mean transmittance, where X ∈ [0.3, 0.4, 0.5, 0.6] is the aperture of the receiving telescope.
'''

# Parameters

wavelength = 1550e-9
zenith_angle = 0
ground_station_alt = 0.020 #Altitude of the receiving telescope
W0 = 0.2 #Initial Beam Waist 
obs_ratio_ground = 0.3 #Obscuration ratio of the receiving telescope 
n_max_ground = 6 #Maximum radial index of correction of AO system 
Cn0 = 9.6*10**(-14) #Reference index of refraction structure constant at ground level
u_rms = 10 #Wind speed
pointing_error = 1e-6 #Pointing error variance
Qonnector_meas_succ = 0.85 #Detector efficiency at the receiver
tracking_efficiency = 0.8 #Tracking efficiency
h_balloons = range(18,38) #Altitude range of the balloon
apertures = [0.3, 0.4, 0.5, 0.6] #Aperture of the receiving telescope sae
simtime = 500000 #Simulation time

#Theoretical mean transmittance 

def heightTheo(h_balloons,rx_aperture_ground):
    
    height_balloon = compute_channel_length(ground_station_alt, h_balloons, zenith_angle)
    transmittance_down = transmittance.slant(ground_station_alt, h_balloons, wavelength*1e9, zenith_angle)
    
   
    downlink_channel = DownlinkChannel(W0, rx_aperture_ground, obs_ratio_ground, n_max_ground, Cn0, u_rms, wavelength, ground_station_alt, h_balloons, zenith_angle,
                                            pointing_error = pointing_error, tracking_efficiency = tracking_efficiency, Tatm = transmittance_down)
    eta = np.arange(1e-7, 1, 0.001)
    mean = downlink_channel._compute_mean_channel_efficiency(eta, height_balloon, detector_efficiency = Qonnector_meas_succ)
    print("Theoretical mean " + str(mean) + " at height " + str(h_balloons))
    return mean
    
    
#Simulated mean transmittance

def heightSimu(h_balloons,rx_aperture_ground):
    
    height_balloon = compute_channel_length(ground_station_alt, h_balloons, zenith_angle)
    transmittance_down = transmittance.slant(ground_station_alt, h_balloons, wavelength*1e9, zenith_angle)
    # Initialize network
    net = QEurope("Europe")

    # Create quantum City 1
    net.Add_Qonnector("QonnectorCity1")

    # Create drone 1
    net.Add_Qonnector("QonnectorDroneCity1")

    # Create channels
    downlink_channel = DownlinkChannel(W0, rx_aperture_ground, obs_ratio_ground, n_max_ground, Cn0, u_rms, wavelength, ground_station_alt, h_balloons, zenith_angle,
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

    print("Height of the balloon : " + str(h_balloons) + "km")
    print("Aperture of the receiving telescope : " + str(rx_aperture_ground) + "cm")
    print("Number of qubits sent by the Balloon: " +str(len(balloon.QlientKeys[city.name])) )
    print("Number of qubits received by Bob (Qlient): " +str(len(city.QlientKeys[balloon.name])) )
    print("Channel efficiency : "+str(chan_eff) + " bits per channel use")
    print("QBER : "+str(estimQBER(L1)))
    
    return chan_eff

    
#Function to parallelize

def Study(h_balloons):
    res = []
    for rx in apertures:
        res.append([h_balloons,rx,'simu',heightSimu(h_balloons,rx),'theo',heightTheo(h_balloons,rx)])
    return res


#Parallelized version
mlp.set_start_method('fork')
pool_threads = os.cpu_count() - 1
pool = mlp.Pool(pool_threads)
trans = pool.map(fnct.partial(Study), h_balloons)
pool.close()
pool.join() 

#Data saving    
            
Simu01 = open("HeightballoonSimu01.txt","w")
Theo01 = open("HeightballoonTheo01.txt","w")
Simu02 = open("HeightballoonSimu02.txt","w")
Theo02 = open("HeightballoonTheo02.txt","w")
Simu04 = open("HeightballoonSimu04.txt","w")
Theo04 = open("HeightballoonTheo04.txt","w")
Simu06 = open("HeightballoonSimu06.txt","w")
Theo06 = open("HeightballoonTheo06.txt","w")

for height in trans:
    for rx in height:
        if rx[1]==0.3:
            Simu01.write(str(rx[3])+ "\n") 
            Theo01.write(str(rx[5])+ "\n")
        if rx[1]==0.4:
            Simu02.write(str(rx[3])+ "\n") 
            Theo02.write(str(rx[5])+ "\n")
        if rx[1]==0.5:
            Simu04.write(str(rx[3])+ "\n") 
            Theo04.write(str(rx[5])+ "\n")
        if rx[1]==0.6:
            Simu06.write(str(rx[3])+ "\n") 
            Theo06.write(str(rx[5])+ "\n")

Simu01.close()
Simu02.close()
Simu04.close()
Simu06.close()
Theo01.close()
Theo02.close()
Theo04.close()
Theo06.close()