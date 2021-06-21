from netCDF4 import Dataset
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os.path

## Create scatter plots of specified MONC variable at specified times.
## Inputs:
##  flightNum     ~ string  ~ id number for the flight being simulated (e.g. F219)
##  fname         ~ string  ~ name of nc file containing the data to be plotted
##  runID         ~ string  ~ id number for the model run to be plotted (e.g. VC1)
##  timeIndex     ~ array   ~ array holding the index values for the timesteps to be plotted
##  variable      ~ string  ~ name, as listed in the data file, of the variable to be plotted (e.g. TdegK)
##  variableName  ~ string  ~ name for identifying variable being plotted (may be different to the name used in the data file) (e.g. temperature)
##  x_label       ~ string  ~ text for the x-axis label (e.g. "Temperature [K]")
##  flag          ~ boolean ~ when true x-axis tick values will be written in scientific notation; when false x-axis tick values will use default formatting
##  convertFactor ~ double  ~ value to multiply the data by before plotting (used for unit conversions)
## Outputs:
## Png files of data plots saved to spath which is currently hardcoded.

def scatter_plots(flightNum,fname,runID,timeIndex,variable,variableName,x_label,flag,convertFactor):
    print("Making {flightNum} {runID} {variable} plots...".format(flightNum=flightNum,runID=runID,variable=variable))
    # Set file paths and load data
    fpath = "/home/vtrost/Documents/PhD/MONC_MAC_2020/"+flightNum+"/NC/"
    spath = "/home/vtrost/Documents/PhD/MONC_MAC_2020/"+flightNum+"/Plots/"

    data = Dataset(fpath + fname)

    # Set up empty DataFrame (size determined by model grid set up)
    df_index = range(32*32) # number of x grid boxes * number of y grid boxes
    columns = range(37) # number of z levels
    df = pd.DataFrame(index=df_index,columns=columns)

    # Set up array of figure titles
    nameCount = 0
    times = ["10min","1hr","2hr","3hr","4hr","5hr","6hr"]

    # Loop through time steps
    for t in timeIndex:
        # Create figure title
        title = flightNum+" - "+runID+" - "+variable+" - "+times[nameCount]

        # Initialize figure
        plt.figure(figsize=(10,10))

        # The "temperature [C]" variable has a different conversion factor so check to see if that is the variable being plotted
        if variableName == "temperature [C]":
            # Loop through data, select the desired datapoints, and save datapoints to DataFrame (applying conversion factors as needed)
            for z in range(37):
                count = 0
                zplot = [data['z'][z]] *1024
                for x in range(32):
                    for y in range(32):
                        df[z][count] = data[variable][t][x][y][z]-273.15
                        count+=1

                # Plot the (x,y) data points for the current z level
                plt.plot(df[z][:],zplot,'b+')
        else:
            # Loop through data, select the desired datapoints, and save datapoints to DataFrame (applying conversion factors as needed)
            for z in range(37):
                count = 0
                zplot = [data['z'][z]] *1024
                for x in range(32):
                    for y in range(32):
                        df[z][count] = data[variable][t][x][y][z]*convertFactor
                        count+=1

                # Plot the (x,y) data points for the current z level
                plt.plot(df[z][:],zplot,'b+')

        # After all the data is ploted format the rest of the figure and save it
        plt.xlabel(x_label,fontsize=20)
        plt.ylabel("Altitude [m]",fontsize=20)
        plt.title(title,fontsize=22)
        plt.xticks(fontsize=18)
        if flag:
            plt.ticklabel_format(axis="x", style="sci", scilimits=(0,0))
        plt.yticks(fontsize=18)
        plt.grid()
        plt.savefig(spath+flightNum[0].lower()+flightNum[1:]+"_"+runID+"_scatterPlot_"+variableName+"_"+times[nameCount]+".png")
        plt.close()
        nameCount += 1

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
    # If they don't want to produce the plot then tell the user that the plot is being skipped and return False, otherwise return True.
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
