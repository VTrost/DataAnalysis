from netCDF4 import Dataset

## Print the time data from specified data file to the terminal.
## Inputs:
##  flightNum     ~ string  ~ id number for the flight being simulated (e.g. F219)
##  fname         ~ string  ~ name of nc file containing the data to be plotted
def checkTimes(flightNum,fname):
    # Set file paths and load data
    fpath = "/home/vtrost/Documents/PhD/MONC_MAC_2020/"+flightNum+"/NC/"
    data = Dataset(fpath + fname)

    # Print times
    print("\n")
    print(data['time_series_200_600.0'][:]/3600.0)
    print("\n")

## Print a table of the specifed time data to the terminal.
## Inputs:
##  flightNum     ~ string  ~ id number for the flight being simulated (e.g. F219)
##  fname         ~ string  ~ name of nc file containing the data to be plotted
##  runID         ~ string  ~ id number for the model run to be plotted (e.g. VC1)
##  index         ~ array   ~ array holding the index values for the time data
def printTimes(flightNum,fname,runID,index):
    # Set file paths and load data
    fpath = "/home/vtrost/Documents/PhD/MONC_MAC_2020/"+flightNum+"/NC/"
    data = Dataset(fpath + fname)

    # Print selected times and indexes
    print("\n"+"        " + runID)
    print("        index : time (in hours):")
    print("        " + str(index[0]) + "  : " + str(data['time_series_200_600.0'][index[0]]/3600.0))
    print("        " + str(index[1]) + "  : " + str(data['time_series_200_600.0'][index[1]]/3600.0))
    print("        " + str(index[2]) + " : " + str(data['time_series_200_600.0'][index[2]]/3600.0))
    print("        " + str(index[3]) + " : " + str(data['time_series_200_600.0'][index[3]]/3600.0))
    print("        " + str(index[4]) + " : " + str(data['time_series_200_600.0'][index[4]]/3600.0))
    print("        " + str(index[5]) + " : " + str(data['time_series_200_600.0'][index[5]]/3600.0))
    print("        " + str(index[6]) + " : " + str(data['time_series_200_600.0'][index[6]]/3600.0)+"\n")