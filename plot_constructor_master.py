from Functions.scatter_plots import *
from Functions.checkTimes import *
from Functions.plot_init_profiles import processInputProfileData
import time
from datetime import datetime
from pydub import AudioSegment
from pydub.playback import play

###### Set variables for run to be plotted ######
spath_init = "/home/vtrost/Documents/PhD/MONC_MAC_2020/Init_profiles/F219/"
flightNum = "F219"
timeIndex = [0,4,10,15,21,26,31]
version = 7 # Used to plot extra variables for specific version numbers
socrates = True # If True than extra plots for Socreates specific variables will be produced
fname = "f219_VC1_21600.0.nc"
fpath_init = "/home/vtrost/Documents/PhD/MONC_MAC_2020/F219/Mcf/f219_VC1.mcf"


## ---- don't change below this line ---- ##
# Ask user if they want to create plots for all variables. Set run_all_flag based on their answer.
print("{flight} - {run}\n".format(flight=flightNum,run=runID))
print("Create all plots?")
run_all_flag = input("[y] or [n]\n")
if run_all_flag=="y":
    run_all_flag = True
else:
    run_all_flag = False

# Ask user if they want to overwrite all exisitng files and set rewrite_all_flag based on their answer.
print("Overwrite all existing files?")
rewrite_all_flag = input("[y] or [n]\n")
if rewrite_all_flag == "y":
    rewrite_all_flag = True
    keep_all_flag = False
else:
    rewrite_all_flag = False
    # Ask user if they want to keep all existing files and set keep_all_flag based on their answer.
    print("Keep all existing files?")
    keep_all_flag = input("[y] or [n]\n")
    if keep_all_flag == "y":
        keep_all_flag = True
    else:
        keep_all_flag = False

###### MODEL INPUT PLOTS ######
print("\n--------------------------------")
print("Plot initial profiles?")
flag = input("[y] or [n]\n")
if flag=="y":
    processInputProfileData(fpath_init,flightNum,runID,spath_init,False,version,run_all_flag,rewrite_all_flag,keep_all_flag)

###### MODEL OUTPUT PLOTS ######
print("\n--------------------------------")
print("\nPlot model outputs?")
flag = input("[y] or [n]\n")
if flag=="y":
    print("Starting plot construction... ("+str(datetime.now().strftime("%H:%M:%S"))+")")

    start_time = time.time()
    
    # If timeIndex is empty, then print the time data so that the user can select the desired time index values.
    if timeIndex == []:
        checkTimes(flightNum,fname)
        exit()

    # Temperature
    variable = "TdegK"
    variableName = "temperature"
    x_label = "Temperature [K]"
    flag = False
    convertFactor = 1
    # Determine if the plots should be produced and either produce the plots or move on to the next variable.
    makePlots = checkForFile(flightNum,runID,variableName,run_all_flag,rewrite_all_flag,keep_all_flag)
    if makePlots:
        scatter_plots(flightNum,fname,runID,timeIndex,variable,variableName,x_label,flag,convertFactor)
        print("Temperature done... ("+str(datetime.now().strftime("%H:%M:%S"))+")")

    # Liquid Number
    variable = "q_cloud_liquid_number"
    variableName = "liquidNum"
    x_label = "Liquid Number [/L]"
    flag = True
    convertFactor = 0.0012
    makePlots = checkForFile(flightNum,runID,variableName,run_all_flag,rewrite_all_flag,keep_all_flag)
    if makePlots:
        scatter_plots(flightNum,fname,runID,timeIndex,variable,variableName,x_label,flag,convertFactor)
        print("Liquid done... ("+str(datetime.now().strftime("%H:%M:%S"))+")")

    # Ice Number
    variable = "q_ice_number"
    variableName = "iceNum"
    x_label = "Ice Number [/L]"
    flag = True
    convertFactor = 0.0012
    makePlots = checkForFile(flightNum,runID,variableName,run_all_flag,rewrite_all_flag,keep_all_flag)
    if makePlots:
        scatter_plots(flightNum,fname,runID,timeIndex,variable,variableName,x_label,flag,convertFactor)
        print("Ice done... ("+str(datetime.now().strftime("%H:%M:%S"))+")")

    # Graupel Number
    variable = "q_graupel_number"
    variableName = "graupelNum"
    x_label = "graupel Number [/L]"
    flag = True
    convertFactor = 0.0012
    makePlots = checkForFile(flightNum,runID,variableName,run_all_flag,rewrite_all_flag,keep_all_flag)
    if makePlots:
        scatter_plots(flightNum,fname,runID,timeIndex,variable,variableName,x_label,flag,convertFactor)
        print("Graupel done... ("+str(datetime.now().strftime("%H:%M:%S"))+")")

    # Snow Number
    variable = "q_snow_number"
    variableName = "snowNum"
    x_label = "Snow Number [/L]"
    flag = True
    convertFactor = 0.0012
    makePlots = checkForFile(flightNum,runID,variableName,run_all_flag,rewrite_all_flag,keep_all_flag)
    if makePlots:
        scatter_plots(flightNum,fname,runID,timeIndex,variable,variableName,x_label,flag,convertFactor)
        print("Snow done... ("+str(datetime.now().strftime("%H:%M:%S"))+")")

    # Rain Number
    variable = "q_rain_number"
    variableName = "rainNum"
    x_label = "Rain Number [/L]"
    flag = True
    convertFactor = 0.0012
    makePlots = checkForFile(flightNum,runID,variableName,run_all_flag,rewrite_all_flag,keep_all_flag)
    if makePlots:
        scatter_plots(flightNum,fname,runID,timeIndex,variable,variableName,x_label,flag,convertFactor)
        print("Rain done... ("+str(datetime.now().strftime("%H:%M:%S"))+")")

    # W Wind
    variable = "w"
    variableName = "WWind"
    x_label = "W Wind [m/s]"
    flag = False
    convertFactor = 1
    makePlots = checkForFile(flightNum,runID,variableName,run_all_flag,rewrite_all_flag,keep_all_flag)
    if makePlots:
        scatter_plots(flightNum,fname,runID,timeIndex,variable,variableName,x_label,flag,convertFactor)
        print("Wind done... ("+str(datetime.now().strftime("%H:%M:%S"))+")")

    # Accum sol mass
    variable = "q_accum_sol_mass"
    variableName = "accumSolMass"
    x_label = "accumSolMass [kg/kg]"
    flag = False
    convertFactor = 1
    makePlots = checkForFile(flightNum,runID,variableName,run_all_flag,rewrite_all_flag,keep_all_flag)
    if makePlots:
        scatter_plots(flightNum,fname,runID,timeIndex,variable,variableName,x_label,flag,convertFactor)
        print(variableName + " done... ("+str(datetime.now().strftime("%H:%M:%S"))+")")

    # Accum sol number
    variable = "q_accum_sol_number"
    variableName = "accumSolNum"
    x_label = "accumSolNumber [#/kg]"
    flag = False
    convertFactor = 1
    makePlots = checkForFile(flightNum,runID,variableName,run_all_flag,rewrite_all_flag,keep_all_flag)
    if makePlots:
        scatter_plots(flightNum,fname,runID,timeIndex,variable,variableName,x_label,flag,convertFactor)
        print(variableName + " done... ("+str(datetime.now().strftime("%H:%M:%S"))+")")

    # Aitken sol mass
    variable = "q_aitken_sol_mass"
    variableName = "aitkenSolMass"
    x_label = "aitkenSolMass [kg/kg]"
    flag = True
    convertFactor = 1
    makePlots = checkForFile(flightNum,runID,variableName,run_all_flag,rewrite_all_flag,keep_all_flag)
    if makePlots:
        scatter_plots(flightNum,fname,runID,timeIndex,variable,variableName,x_label,flag,convertFactor)
        print(variableName + " done... ("+str(datetime.now().strftime("%H:%M:%S"))+")")

    # Aitken sol number
    variable = "q_aitken_sol_number"
    variableName = "aitkenSolNum"
    x_label = "aitkenSolNumber [#/kg]"
    flag = True
    convertFactor = 1
    makePlots = checkForFile(flightNum,runID,variableName,run_all_flag,rewrite_all_flag,keep_all_flag)
    if makePlots:
        scatter_plots(flightNum,fname,runID,timeIndex,variable,variableName,x_label,flag,convertFactor)
        print(variableName + " done... ("+str(datetime.now().strftime("%H:%M:%S"))+")")

    # Coarse sol mass
    variable = "q_coarse_sol_mass"
    variableName = "coarseSolMass"
    x_label = "coarseSolMass [kg/kg]"
    flag = True
    convertFactor = 1
    makePlots = checkForFile(flightNum,runID,variableName,run_all_flag,rewrite_all_flag,keep_all_flag)
    if makePlots:
        scatter_plots(flightNum,fname,runID,timeIndex,variable,variableName,x_label,flag,convertFactor)
        print(variableName + " done... ("+str(datetime.now().strftime("%H:%M:%S"))+")")

    # Coarse sol number
    variable = "q_coarse_sol_number"
    variableName = "coarseSolNum"
    x_label = "coarseSolNumber [#/kg]"
    flag = True
    convertFactor = 1
    makePlots = checkForFile(flightNum,runID,variableName,run_all_flag,rewrite_all_flag,keep_all_flag)
    if makePlots:
        scatter_plots(flightNum,fname,runID,timeIndex,variable,variableName,x_label,flag,convertFactor)
        print(variableName + " done... ("+str(datetime.now().strftime("%H:%M:%S"))+")")

    # Coarse dust mass
    variable = "q_coarse_dust_mass"
    variableName = "coarseDustMass"
    x_label = "coarseDustMass [kg/kg]"
    flag = False
    convertFactor = 1
    makePlots = checkForFile(flightNum,runID,variableName,run_all_flag,rewrite_all_flag,keep_all_flag)
    if makePlots:
        scatter_plots(flightNum,fname,runID,timeIndex,variable,variableName,x_label,flag,convertFactor)
        print(variableName + " done... ("+str(datetime.now().strftime("%H:%M:%S"))+")")

    # Coarse dust number
    variable = "q_coarse_dust_number"
    variableName = "coarseDustNum"
    x_label = "coarseDustNumber [#/kg]"
    flag = False
    convertFactor = 1
    makePlots = checkForFile(flightNum,runID,variableName,run_all_flag,rewrite_all_flag,keep_all_flag)
    if makePlots:
        scatter_plots(flightNum,fname,runID,timeIndex,variable,variableName,x_label,flag,convertFactor)
        print(variableName + " done... ("+str(datetime.now().strftime("%H:%M:%S"))+")")

    # Active insol ice
    variable = "q_active_insol_ice"
    variableName = "activeInsolIce"
    x_label = "activeInsolIce [kg/kg]"
    flag = False
    convertFactor = 1
    makePlots = checkForFile(flightNum,runID,variableName,run_all_flag,rewrite_all_flag,keep_all_flag)
    if makePlots:
        scatter_plots(flightNum,fname,runID,timeIndex,variable,variableName,x_label,flag,convertFactor)
        print(variableName + " done... ("+str(datetime.now().strftime("%H:%M:%S"))+")")

    # Active insol liquid
    variable = "q_active_insol_liquid"
    variableName = "activeInsolLiquid"
    x_label = "activeInsolLiquid [kg/kg]"
    flag = False
    convertFactor = 1
    makePlots = checkForFile(flightNum,runID,variableName,run_all_flag,rewrite_all_flag,keep_all_flag)
    if makePlots:
        scatter_plots(flightNum,fname,runID,timeIndex,variable,variableName,x_label,flag,convertFactor)
        print(variableName + " done... ("+str(datetime.now().strftime("%H:%M:%S"))+")")

    if version != 8:
        # Cloud liquid mass
        variable = "q_cloud_liquid_mass"
        variableName = "cloudLiquidMass"
        x_label = "cloudLiquidMass [kg/kg]"
        flag = True
        convertFactor = 1
        makePlots = checkForFile(flightNum,runID,variableName,run_all_flag,rewrite_all_flag,keep_all_flag)
        if makePlots:
            scatter_plots(flightNum,fname,runID,timeIndex,variable,variableName,x_label,flag,convertFactor)
            print(variableName + " done... ("+str(datetime.now().strftime("%H:%M:%S"))+")")

        # Cloud liquid number
        variable = "q_cloud_liquid_number"
        variableName = "cloudLiquidNum"
        x_label = "cloudLiquidNumber [#/kg]"
        flag = True
        convertFactor = 1
        makePlots = checkForFile(flightNum,runID,variableName,run_all_flag,rewrite_all_flag,keep_all_flag)
        if makePlots:
            scatter_plots(flightNum,fname,runID,timeIndex,variable,variableName,x_label,flag,convertFactor)
            print(variableName + " done... ("+str(datetime.now().strftime("%H:%M:%S"))+")")

    if socrates == True:
        # Longwave Heating Rate
        variable = "longwave_heating_rate"
        variableName = "lwHeatingRate"
        x_label = "Longwave heating rate [?]"
        flag = False
        convertFactor = 1
        makePlots = checkForFile(flightNum,runID,variableName,run_all_flag,rewrite_all_flag,keep_all_flag)
        if makePlots:
            scatter_plots(flightNum,fname,runID,timeIndex,variable,variableName,x_label,flag,convertFactor)
            print("Longwave heating rate done... ("+str(datetime.now().strftime("%H:%M:%S"))+")")

        # Shortwave Heating Rate
        variable = "shortwave_heating_rate"
        variableName = "swHeatingRate"
        x_label = "Shortwave heating rate [?]"
        flag = True
        convertFactor = 1
        makePlots = checkForFile(flightNum,runID,variableName,run_all_flag,rewrite_all_flag,keep_all_flag)
        if makePlots:
            scatter_plots(flightNum,fname,runID,timeIndex,variable,variableName,x_label,flag,convertFactor)
            print("Shortwave heating rate done... ("+str(datetime.now().strftime("%H:%M:%S"))+")")

        # Longwave Flux Down
        variable = "flux_down_longwave"
        variableName = "lwFluxDown"
        x_label = "Longwave flux - down [?]"
        flag = False
        convertFactor = 1
        makePlots = checkForFile(flightNum,runID,variableName,run_all_flag,rewrite_all_flag,keep_all_flag)
        if makePlots:
            scatter_plots(flightNum,fname,runID,timeIndex,variable,variableName,x_label,flag,convertFactor)
            print("Longwave flux down done... ("+str(datetime.now().strftime("%H:%M:%S"))+")")

        # Longwave Flux Up
        variable = "flux_up_longwave"
        variableName = "lwFluxUp"
        x_label = "Longwave flux - up [?]"
        flag = False
        convertFactor = 1
        makePlots = checkForFile(flightNum,runID,variableName,run_all_flag,rewrite_all_flag,keep_all_flag)
        if makePlots:
            scatter_plots(flightNum,fname,runID,timeIndex,variable,variableName,x_label,flag,convertFactor)
            print("Longwave flux up done... ("+str(datetime.now().strftime("%H:%M:%S"))+")")

        # Shortwave Flux Down
        variable = "flux_down_shortwave"
        variableName = "swFluxDown"
        x_label = "Shortwave flux - down [?]"
        flag = False
        convertFactor = 1
        makePlots = checkForFile(flightNum,runID,variableName,run_all_flag,rewrite_all_flag,keep_all_flag)
        if makePlots:
            scatter_plots(flightNum,fname,runID,timeIndex,variable,variableName,x_label,flag,convertFactor)
            print("Shortwave flux down done... ("+str(datetime.now().strftime("%H:%M:%S"))+")")

        # Shortwave Flux Up
        variable = "flux_up_shortwave"
        variableName = "swFluxUp"
        x_label = "Shortwave flux - up [?]"
        flag = False
        convertFactor = 1
        makePlots = checkForFile(flightNum,runID,variableName,run_all_flag,rewrite_all_flag,keep_all_flag)
        if makePlots:
            scatter_plots(flightNum,fname,runID,timeIndex,variable,variableName,x_label,flag,convertFactor)
            print("Shortwave flux up done... ("+str(datetime.now().strftime("%H:%M:%S"))+")")

    print("Process finished --- %s seconds ---" % (time.time() - start_time))

# Print table of times to terminal.
printTimes(flightNum,fname,runID,timeIndex)

# Play tone to let user know that the program has finished
play(AudioSegment.from_mp3('/home/vtrost/Music/Sounds/chimes-glassy-456.mp3'))