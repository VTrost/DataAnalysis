import numpy as np
import os
from datetime import datetime
import matplotlib.pyplot as plt

## Read input profile data from MONC configuration (mcf) file and plot the data.
## Inputs:
##  fpath ~ string ~ filepath to MONC configuration (mcf) file
##  flightNum          ~ string  ~ id number for the flight being simulated (e.g. F219).
##  runID              ~ string  ~ id number for the model run to be plotted (e.g. VC1).
##  spath              ~ string ~ file path to save plots to.
##  flag               ~ boolean ~ when true x-axis tick values will be written in scientifc notation; when false x-axis tuck values will use default formatting.
##  version            ~ int     ~ version number used to determine which set of index values to use
##  run_all            ~ boolean ~ flag indicating whether to run plotting code for all variables.
##  rewrite_all_flag   ~ boolean ~ flag indicating whether to rewrite all existing files
##  keep_all_flag      ~ boolean ~ flag indicating whether to keep all existing files
def processInputProfileData(fpath,flightNum,runID,spath,flag,version,run_all_flag,rewrite_all_flag,keep_all_flag):
    # Check for the subdirectory for the run and create if it doesn't exist
    if not os.path.exists(spath+runID):
        os.makedirs(spath+runID)
    spath = spath+runID+"/"

    # Load the mcf file and extract the variables
    myLines = []
    with open(fpath,'rt') as file:
        for line in file:
            myLines.append(line)

    altitude = np.array(myLines[162][16:].split(",")).astype(np.float)

    theta = np.array(myLines[163][16:].split(",")).astype(np.float)

    u = np.array(myLines[167][12:].split(",")).astype(np.float)

    v = np.array(myLines[171][12:].split(",")).astype(np.float)

    if version == 1: # 80 levels | all q varaibles listed together
        altitude_q = altitude
        q = np.array(myLines[176][12:].split(",")).astype(np.float)
        
        vapour = q[0:80]
        coarse_dust_mass = q[80:160]
        coarse_dust_number = q[160:240]
        cloud_liquid_mass = q[240:320]
        cloud_liquid_number = q[320:400]
        active_insol_liquid = q[400:480]
        active_insol_ice = q[480:560]
        accum_sol_mass = q[560:640]
        accum_sol_number = q[640:720]
        aitken_sol_mass = q[720:800]
        aitken_sol_number = q[800:880]
        coarse_sol_mass = q[880:960]
        coarse_sol_number = q[960:1040]

    elif version == 2: # 80 levels | vapour listed separately
        altitude_q = np.array(myLines[179][12:].split(",")).astype(np.float)
        q1 = np.array(myLines[176][12:].split(",")).astype(np.float)
        q2 = np.array(myLines[180][12:].split(",")).astype(np.float)

        vapour = q1[0:80]

        coarse_dust_mass = q2[0:80]
        coarse_dust_number = q2[80:160]
        cloud_liquid_mass = q2[160:240]
        cloud_liquid_number = q2[240:320]
        active_insol_liquid = q2[320:400]
        active_insol_ice = q2[400:480]
        accum_sol_mass = q2[480:560]
        accum_sol_number = q2[560:640]
        aitken_sol_mass = q2[640:720]
        aitken_sol_number = q2[720:800]
        coarse_sol_mass = q2[800:880]
        coarse_sol_number = q2[880:960]

    elif version == 3: # 80 vapour levels | 21 aero levels | vapour listed separately
        altitude_q = np.array(myLines[175][12:].split(",")).astype(np.float)
        altitude_q2 = np.array(myLines[179][12:].split(",")).astype(np.float)
        q1 = np.array(myLines[176][12:].split(",")).astype(np.float)
        q2 = np.array(myLines[180][12:].split(",")).astype(np.float)

        vapour = q1[0:80]

        coarse_dust_mass = q2[0:21]
        coarse_dust_number = q2[21:42]
        cloud_liquid_mass = q2[42:63]
        cloud_liquid_number = q2[63:84]
        active_insol_liquid = q2[84:105]
        active_insol_ice = q2[105:126]
        accum_sol_mass = q2[126:147]
        accum_sol_number = q2[147:168]
        aitken_sol_mass = q2[168:189]
        aitken_sol_number = q2[189:210]
        coarse_sol_mass = q2[210:231]
        coarse_sol_number = q2[231:252]

    elif version == 4: # 80 vapour levels | 2 aero levels | vapour listed separately
        altitude_q = np.array(myLines[175][12:].split(",")).astype(np.float)
        altitude_q2 = np.array(myLines[179][12:].split(",")).astype(np.float)
        q1 = np.array(myLines[176][12:].split(",")).astype(np.float)
        q2 = np.array(myLines[180][12:].split(",")).astype(np.float)

        vapour = q1[0:80]

        coarse_dust_mass = q2[0:2]
        coarse_dust_number = q2[2:4]
        cloud_liquid_mass = q2[4:6]
        cloud_liquid_number = q2[6:8]
        active_insol_liquid = q2[8:10]
        active_insol_ice = q2[10:12]
        accum_sol_mass = q2[12:14]
        accum_sol_number = q2[14:16]
        aitken_sol_mass = q2[16:18]
        aitken_sol_number = q2[18:20]
        coarse_sol_mass = q2[20:22]
        coarse_sol_number = q2[22:24]

    elif version == 5: # 44 vapour levels | 80 aero levels | vapour listed separately
        altitude_q = altitude
        altitude_q2 = np.array(myLines[179][12:].split(",")).astype(np.float)
        q1 = np.array(myLines[176][12:].split(",")).astype(np.float)
        q2 = np.array(myLines[180][12:].split(",")).astype(np.float)

        vapour = q1[0:44]

        coarse_dust_mass = q2[0:80]
        coarse_dust_number = q2[80:160]
        cloud_liquid_mass = q2[160:240]
        cloud_liquid_number = q2[240:320]
        active_insol_liquid = q2[320:400]
        active_insol_ice = q2[400:480]
        accum_sol_mass = q2[480:560]
        accum_sol_number = q2[560:640]
        aitken_sol_mass = q2[640:720]
        aitken_sol_number = q2[720:800]
        coarse_sol_mass = q2[800:880]
        coarse_sol_number = q2[880:960]

    elif version == 6: # 44 vapour levels | 21 aero levels | vapour listed separately
        altitude_q = altitude
        altitude_q2 = np.array(myLines[179][12:].split(",")).astype(np.float)
        q1 = np.array(myLines[176][12:].split(",")).astype(np.float)
        q2 = np.array(myLines[180][12:].split(",")).astype(np.float)

        vapour = q1[0:44]

        coarse_dust_mass = q2[0:21]
        coarse_dust_number = q2[21:42]
        cloud_liquid_mass = q2[42:63]
        cloud_liquid_number = q2[63:84]
        active_insol_liquid = q2[84:105]
        active_insol_ice = q2[105:126]
        accum_sol_mass = q2[126:147]
        accum_sol_number = q2[147:168]
        aitken_sol_mass = q2[168:189]
        aitken_sol_number = q2[189:210]
        coarse_sol_mass = q2[210:231]
        coarse_sol_number = q2[231:252]

    elif version == 7: # 44 vapourlevels | all q variables listed together
        altitude_q = altitude
        q = np.array(myLines[176][12:].split(",")).astype(np.float)
        
        vapour = q[0:44]
        coarse_dust_mass = q[44:88]
        coarse_dust_number = q[88:132]
        cloud_liquid_mass = q[132:176]
        cloud_liquid_number = q[176:220]
        active_insol_liquid = q[220:264]
        active_insol_ice = q[264:308]
        accum_sol_mass = q[308:352]
        accum_sol_number = q[352:396]
        aitken_sol_mass = q[396:440]
        aitken_sol_number = q[440:484]
        coarse_sol_mass = q[484:528]
        coarse_sol_number = q[528:572]

    elif version == 8: # same as version 7 but without cloud liquid
        altitude_q = altitude
        q = np.array(myLines[176][12:].split(",")).astype(np.float)
        
        vapour = q[0:44]
        coarse_dust_mass = q[44:88]
        coarse_dust_number = q[88:132]
        active_insol_liquid = q[132:176]
        active_insol_ice = q[176:220]
        accum_sol_mass = q[220:264]
        accum_sol_number = q[264:308]
        aitken_sol_mass = q[308:352]
        aitken_sol_number = q[352:396]
        coarse_sol_mass = q[396:440]
        coarse_sol_number = q[440:484]

    elif version == 9: # 10 q levels | all q variables listed together
        altitude_q = altitude
        q = np.array(myLines[176][12:].split(",")).astype(np.float)
        
        vapour = q[0:401]
        coarse_dust_mass = q[10:20]
        coarse_dust_number = q[20:30]
        cloud_liquid_mass = q[30:40]
        cloud_liquid_number = q[40:50]
        active_insol_liquid = q[50:60]
        active_insol_ice = q[60:70]
        accum_sol_mass = q[70:80]
        accum_sol_number = q[80:90]
        aitken_sol_mass = q[90:100]
        aitken_sol_number = q[100:110]
        coarse_sol_mass = q[110:120]
        coarse_sol_number = q[120:130]

    else:
        print("Error: invalid version number")


    # Create plots
    # Potential temperature
    variableName = "theta"
    x_label = "Potential temperature [K]"
    x = theta
    is_constant = False
    print("\n---"+variableName+"---")
    print(x)
    # Determine if the plots should be produced and either produce the plots or move on to the next variable.
    makePlots = checkForFile(flightNum,runID,variableName,run_all_flag,rewrite_all_flag,keep_all_flag)
    if makePlots:
        plotInputProfiles(x,altitude,variableName,x_label,flightNum,runID,flag,is_constant,spath)
        print(variableName+" done... ("+str(datetime.now().strftime("%H:%M:%S"))+")")

    # U
    variableName = "u"
    x_label = "U wind [m/s"
    x = u
    is_constant = False
    print("\n---"+variableName+"---")
    print(x)
    makePlots = checkForFile(flightNum,runID,variableName,run_all_flag,rewrite_all_flag,keep_all_flag)
    if makePlots:
        plotInputProfiles(x,altitude,variableName,x_label,flightNum,runID,flag,is_constant,spath)
        print(variableName+" done... ("+str(datetime.now().strftime("%H:%M:%S"))+")")

    # V
    variableName = "v"
    x_label = "V wind [m/s]"
    x = v
    is_constant = False
    print("\n---"+variableName+"---")
    print(x)
    makePlots = checkForFile(flightNum,runID,variableName,run_all_flag,rewrite_all_flag,keep_all_flag)
    if makePlots:
        plotInputProfiles(x,altitude,variableName,x_label,flightNum,runID,flag,is_constant,spath)
        print(variableName+" done... ("+str(datetime.now().strftime("%H:%M:%S"))+")")

    # Vapour
    variableName = "vapour"
    x_label = "Vapour mixing ratio [kg/kg]"
    x = vapour
    is_constant = False
    print("\n---"+variableName+"---")
    print(x)
    makePlots = checkForFile(flightNum,runID,variableName,run_all_flag,rewrite_all_flag,keep_all_flag)
    if makePlots:
        plotInputProfiles(x,altitude,variableName,x_label,flightNum,runID,flag,is_constant,spath)
        print(variableName+" done... ("+str(datetime.now().strftime("%H:%M:%S"))+")")

    if version == 3 or version == 4 or version == 5 or version == 6:
        altitude_q = altitude_q2
        
    # Coarse dust mass
    variableName = "coarse_dust_mass"
    x_label = "Coarse dust mass mixing ratio [kg/kg]"
    x = coarse_dust_mass
    is_constant = True
    print("\n---"+variableName+"---")
    print(x)
    makePlots = checkForFile(flightNum,runID,variableName,run_all_flag,rewrite_all_flag,keep_all_flag)
    if makePlots:
        plotInputProfiles(x,altitude_q,variableName,x_label,flightNum,runID,flag,is_constant,spath)
        print(variableName+" done... ("+str(datetime.now().strftime("%H:%M:%S"))+")")

    # Coarse dust num
    variableName = "coarse_dust_number"
    x_label = "Coarse dust number concentration [#/kg]"
    x = coarse_dust_number
    is_constant = True
    print("\n---"+variableName+"---")
    print(x)
    makePlots = checkForFile(flightNum,runID,variableName,run_all_flag,rewrite_all_flag,keep_all_flag)
    if makePlots:
        plotInputProfiles(x,altitude_q,variableName,x_label,flightNum,runID,flag,is_constant,spath)
        print(variableName+" done... ("+str(datetime.now().strftime("%H:%M:%S"))+")")

    if version != 8:
        # Cloud liquid mass
        variableName = "cloud_liquid_mass"
        x_label = "Cloud liquid mass mixing ratio [kg/kg]"
        x = cloud_liquid_mass
        is_constant = True
        print("\n---"+variableName+"---")
        print(x)
        makePlots = checkForFile(flightNum,runID,variableName,run_all_flag,rewrite_all_flag,keep_all_flag)
        if makePlots:
            plotInputProfiles(x,altitude_q,variableName,x_label,flightNum,runID,flag,is_constant,spath)
            print(variableName+" done... ("+str(datetime.now().strftime("%H:%M:%S"))+")")

        # Cloud liquidt num
        variableName = "cloud_liquid_number"
        x_label = "Cloud liquid number concentration [#/kg]"
        x = cloud_liquid_number
        is_constant = True
        print("\n---"+variableName+"---")
        print(x)
        makePlots = checkForFile(flightNum,runID,variableName,run_all_flag,rewrite_all_flag,keep_all_flag)
        if makePlots:
            plotInputProfiles(x,altitude_q,variableName,x_label,flightNum,runID,flag,is_constant,spath)
            print(variableName+" done... ("+str(datetime.now().strftime("%H:%M:%S"))+")")

    # Accum sol mass
    variableName = "accum_sol_mass"
    x_label = "Accum sol mass mixing ratio [kg/kg]"
    x = accum_sol_mass
    is_constant = True
    print("\n---"+variableName+"---")
    print(x)
    makePlots = checkForFile(flightNum,runID,variableName,run_all_flag,rewrite_all_flag,keep_all_flag)
    if makePlots:
        plotInputProfiles(x,altitude_q,variableName,x_label,flightNum,runID,flag,is_constant,spath)
        print(variableName+" done... ("+str(datetime.now().strftime("%H:%M:%S"))+")")

    # Accum sol num
    variableName = "accum_sol_number"
    x_label = "Accum sol number concentration [#/kg]"
    x = accum_sol_number
    is_constant = True
    print("\n---"+variableName+"---")
    print(x)
    makePlots = checkForFile(flightNum,runID,variableName,run_all_flag,rewrite_all_flag,keep_all_flag)
    if makePlots:
        plotInputProfiles(x,altitude_q,variableName,x_label,flightNum,runID,flag,is_constant,spath)
        print(variableName+" done... ("+str(datetime.now().strftime("%H:%M:%S"))+")")

    # Aitken sol mass
    variableName = "aitken_sol_mass"
    x_label = "Aitken sol mass mixing ratio [kg/kg]"
    x = aitken_sol_mass
    is_constant = True
    print("\n---"+variableName+"---")
    print(x)
    makePlots = checkForFile(flightNum,runID,variableName,run_all_flag,rewrite_all_flag,keep_all_flag)
    if makePlots:
        plotInputProfiles(x,altitude_q,variableName,x_label,flightNum,runID,flag,is_constant,spath)
        print(variableName+" done... ("+str(datetime.now().strftime("%H:%M:%S"))+")")

    # Aitken sol num
    variableName = "aitken_sol_number"
    x_label = "Aitken sol number concentration [#/kg]"
    x = aitken_sol_number
    is_constant = True
    print("\n---"+variableName+"---")
    print(x)
    makePlots = checkForFile(flightNum,runID,variableName,run_all_flag,rewrite_all_flag,keep_all_flag)
    if makePlots:
        plotInputProfiles(x,altitude_q,variableName,x_label,flightNum,runID,flag,is_constant,spath)
        print(variableName+" done... ("+str(datetime.now().strftime("%H:%M:%S"))+")")

    # Coarse sol mass
    variableName = "coarse_sol_mass"
    x_label = "Coarse sol mass mixing ratio [kg/kg]"
    x = coarse_sol_mass
    is_constant = True
    print("\n---"+variableName+"---")
    print(x)
    makePlots = checkForFile(flightNum,runID,variableName,run_all_flag,rewrite_all_flag,keep_all_flag)
    if makePlots:
        plotInputProfiles(x,altitude_q,variableName,x_label,flightNum,runID,flag,is_constant,spath)
        print(variableName+" done... ("+str(datetime.now().strftime("%H:%M:%S"))+")")

    # Coarse sol num
    variableName = "coarse_sol_number"
    x_label = "Coarse sol number concentration [#/kg]"
    x = coarse_sol_number
    is_constant = True
    print("\n---"+variableName+"---")
    print(x)
    makePlots = checkForFile(flightNum,runID,variableName,run_all_flag,rewrite_all_flag,keep_all_flag)
    if makePlots:
        plotInputProfiles(x,altitude_q,variableName,x_label,flightNum,runID,flag,is_constant,spath)
        print(variableName+" done... ("+str(datetime.now().strftime("%H:%M:%S"))+")")

    # Active insol liquid
    variableName = "active_insol_liquid"
    x_label = "Active insol liquid mass mixing ratio [kg/kg]"
    x = active_insol_liquid
    is_constant = True
    print("\n---"+variableName+"---")
    print(x)
    makePlots = checkForFile(flightNum,runID,variableName,run_all_flag,rewrite_all_flag,keep_all_flag)
    if makePlots:
        plotInputProfiles(x,altitude_q,variableName,x_label,flightNum,runID,flag,is_constant,spath)
        print(variableName+" done... ("+str(datetime.now().strftime("%H:%M:%S"))+")")

    # Active insol ice
    variableName = "active_insol_ice"
    x_label = "Active insol ice mass mixing ratio [kg/kg]"
    x = active_insol_ice
    is_constant = True
    print("\n---"+variableName+"---")
    print(x)
    makePlots = checkForFile(flightNum,runID,variableName,run_all_flag,rewrite_all_flag,keep_all_flag)
    if makePlots:
        plotInputProfiles(x,altitude_q,variableName,x_label,flightNum,runID,flag,is_constant,spath)
        print(variableName+" done... ("+str(datetime.now().strftime("%H:%M:%S"))+")")

## Produce line plot.
## Inputs:
##  x            ~ array ~ array of x-axis data points.
##  y            ~ array ~ array of y-axis data points.
##  variableName ~ string ~ name of variable to be plotted.
##  x_label      ~ string ~ text for x-axis label.
##  flightNum    ~ string  ~ id number for the flight being simulated (e.g. F219).
##  runID        ~ string  ~ id number for the model run to be plotted (e.g. VC1).
##  flag         ~ boolean ~ when true x-axis tick values will be written in scientifc notation; when false x-axis tuck values will use default formatting.
## is_constant   ~ boolean ~ flag to label lines of constant x values with the value of x.
## spath         ~ string ~ file path to save plots to.
def plotInputProfiles(x,y,variableName,x_label,flightNum,runID,flag,is_constant,spath):
    plt.figure(figsize=(10,10))
    if is_constant==True:
        plt.text(x[0],3800,min(x),fontsize=20,bbox=dict(facecolor='white'))
    plt.plot(x,y,'g*-')
    plt.xlabel(x_label,fontsize=20)
    plt.ylabel("Altitude [m]",fontsize=20)
    plt.title(flightNum +" - "+runID+" - "+variableName+" input profile",fontsize=22)
    plt.xticks(fontsize=18)
    if flag:
        plt.ticklabel_format(axis="x", style="sci", scilimits=(0,0))
    plt.yticks(fontsize=18)
    plt.grid()
    plt.savefig(spath+flightNum[0].lower()+flightNum[1:]+"_"+runID+"_"+variableName+"_inputProfile.png")
    plt.close()

## Checks to see if a file exists for the plot in question, prints status message to user and/or requests input from user based on the value of three flags.
## Inputs:
##  flightNum          ~ string  ~ id number for the flight being simulated (e.g. F219)
##  runID              ~ string  ~ id number for the model run to be plotted (e.g. VC1)
##  variableName       ~ string  ~ name for identifying variable being plotted (may be different to the name used in the data file) (e.g. temperature)
##  run_all            ~ boolean ~ flag indicating whether to run plotting code for all variables.
##  rewrite_all_flag   ~ boolean ~ flag indicating whether to rewrite all existing files
##  keep_all_flag      ~ boolean ~ flag indicating whether to keep all existing files
## Output:
##  returns True if the plot in question should be produced and False if the plot should not be produced
def checkForFile(flightNum,runID,variableName,run_all_flag,rewrite_all_flag,keep_all_flag):
    spath = "/home/vtrost/Documents/PhD/MONC_MAC_2020/"+flightNum+"/Plots/"
    
    # If file exists and rewrite_all_flag and keep_all_flag are both False then ask the user if they want to overwrite the existing file.
    # If they don't want to overwrite, then tell the user that the file is being skipped and return False, otherwise return True
    if rewrite_all_flag==False and keep_all_flag==False and os.path.isfile(spath+flightNum[0].lower()+flightNum[1:]+"_"+runID+"_scatterPlot_"+variableName+"_10min.png"):
        print("\nOverwrite {runID} {variable} plots?".format(runID=runID,variable=variableName))
        flag = input("[y] or [n]\n")
        if flag!="y":
            print("Skip {runID} {variable}...\n".format(runID=runID,variable=variableName))
            return False
        else:
            return True
    # If file exists and keep_all_flag is True, then tell user the file is being skipped and return False
    elif rewrite_all_flag == False and keep_all_flag == True and os.path.isfile(spath+flightNum[0].lower()+flightNum[1:]+"_"+runID+"_scatterPlot_"+variableName+"_10min.png"):
        print("Skip {runID} {variable}...\n".format(runID=runID,variable=variableName))
        return False
    # If run_all_flag is False then as the user if they want to produce the plot.
    # If they don't want to produce the plot then tell the user that the plot is being skipped and return False, otherwise return True
    elif run_all_flag==False:
        print("\nMake {runID} {variable} plots?".format(runID=runID,variable=variableName))
        flag = input("[y] or [n]\n")
        if flag!="y":
            print("Skip {runID} {variable}...\n".format(runID=runID,variable=variableName))
            return False
        else:
            return True
    # If none of the previous conditions have been met then assume that the plot should be produced and return True
    else:   
        return True
