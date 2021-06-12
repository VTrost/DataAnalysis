### Code to compile all the average profile and scatter plots into pptx files.
### Output: XXXX_avgProfiles.pptx, XXXX_scatterPlots_temperature.pptx, XXXX_scatterPlots_liquidNum.pptx, XXXX_scatterPlots_iceNum.pptx, XXXX_scatterPlots_graupelNum.pptx, XXXX_scatterPlots_snowNum.pptx, XXXX_scatterPlots_rainNum.pptx, XXXX_scatterPlots_WWind.pptx, XXXX_scatterPlots_10min.pptx, XXXX_scatterPlots_1hr.pptx, XXXX_scatterPlots_2hr.pptx, XXXX_scatterPlots_3hr.pptx, XXXX_scatterPlots_4hr.pptx, XXXX_scatterPlots_5hr.pptx, XXXX_scatterPlots_6hr.pptx
### Command line arguments: Flight number and runID

require_relative 'to_powerpoint_functions'

flightNum = ARGV[0]
runID = ARGV[1]
ARGV.clear

if runID.nil?  || flightNum.nil?
    puts "Error: must include flightNum and runID in command (ex: ruby powerpoint_constructor_master.rb f219, V22)"
    exit
end

puts "Overwrite all existing files?"
puts "[y] or [n]?"
input = gets.chomp()
if input == "y"
    overwrite_all = true
else
    puts "Keep all existing plots?"
    puts "[y] or [n]?"
    input = gets.chomp()
    if input == 'y'
        keep_all = true
    else
        keep_all = false
    end
    overwrite_all = false
end


###### MODEL INPUT PLOTS ######
puts "\n---------------"
puts "Create pptx of model input plots?"
puts "[y] or [n]?"
input = gets.chomp()
if input == "y"
    path_full = "/home/vtrost/Documents/PhD/MONC_MAC_2020/Init_profiles/#{flightNum.capitalize()}/#{runID}/"
    spath_full = path_full+"#{flightNum}_#{runID}_initial_profiles.pptx"
    title = "#{flightNum} - #{runID} - initial profiles"
    to_powerpoint_init_profiles(path_full,flightNum,runID,spath_full,title,overwrite_all,keep_all)
end


###### MODEL OUTPUT PLOTS - variables ######
puts "\n---------------"
puts "Create pptx of model output plots (by variable)?"
puts "[y] or [n]?"
input = gets.chomp()
if input == "y"
    spath = "/home/vtrost/Documents/PhD/MONC_MAC_2020/#{flightNum.capitalize()}/Plots/Powerpoints/#{runID}/"
    fpath = "/home/vtrost/Documents/PhD/MONC_MAC_2020/F219/Plots/"
    if Dir.exists?(spath) == false
        puts "Creating #{runID} directory..."
        Dir.mkdir(spath)
    end

    # Temperature scatter plots
    spath_full = spath + "#{flightNum}_#{runID}_scatterPlots_temperature.pptx"
    title = "#{flightNum} - #{runID} - temperature scatter plots"
    variable = "temperature"
    to_powerpoint_scatter_plot_by_variable(fpath,flightNum,runID,spath_full,title,variable,overwrite_all,keep_all)

    # Liquid number scatter plots
    spath_full = spath + "#{flightNum}_#{runID}_scatterPlots_liquidNum.pptx"
    title = "#{flightNum} - #{runID} - liquidNum scatter plots"
    variable = "liquidNum"
    to_powerpoint_scatter_plot_by_variable(fpath,flightNum,runID,spath_full,title,variable,overwrite_all,keep_all)

    # Ice number scatter plots
    spath_full = spath + "#{flightNum}_#{runID}_scatterPlots_iceNum.pptx"
    title = "#{flightNum} - #{runID} - iceNum scatter plots"
    variable = "iceNum"
    to_powerpoint_scatter_plot_by_variable(fpath,flightNum,runID,spath_full,title,variable,overwrite_all,keep_all)

    # Graupel number scatter plots
    spath_full = spath + "#{flightNum}_#{runID}_scatterPlots_graupelNum.pptx"
    title = "#{flightNum} - #{runID} - graupelNum scatter plots"
    variable = "graupelNum"
    to_powerpoint_scatter_plot_by_variable(fpath,flightNum,runID,spath_full,title,variable,overwrite_all,keep_all)

    # Snow number scatter plots
    spath_full = spath + "#{flightNum}_#{runID}_scatterPlots_snowNum.pptx"
    title = "#{flightNum} - #{runID} - snowNum scatter plots"
    variable = "snowNum"
    to_powerpoint_scatter_plot_by_variable(fpath,flightNum,runID,spath_full,title,variable,overwrite_all,keep_all)

    # Rain number scatter plots
    spath_full = spath + "#{flightNum}_#{runID}_scatterPlots_rainNum.pptx"
    title = "#{flightNum} - #{runID} - rainNum scatter plots"
    variable = "rainNum"
    to_powerpoint_scatter_plot_by_variable(fpath,flightNum,runID,spath_full,title,variable,overwrite_all,keep_all)

    # WWind  scatter plots
    spath_full = spath + "#{flightNum}_#{runID}_scatterPlots_WWind.pptx"
    title = "#{flightNum} - #{runID} - WWind scatter plots"
    variable = "WWind"
    to_powerpoint_scatter_plot_by_variable(fpath,flightNum,runID,spath_full,title,variable,overwrite_all,keep_all)

    # Accum sol mass scatter plots
    spath_full = spath + "#{flightNum}_#{runID}_scatterPlots_accumSolMass.pptx"
    title = "#{flightNum} - #{runID} - AccumSolMass scatter plots"
    variable = "accumSolMass"
    to_powerpoint_scatter_plot_by_variable(fpath,flightNum,runID,spath_full,title,variable,overwrite_all,keep_all)

    # Accum sol number scatter plots
    spath_full = spath + "#{flightNum}_#{runID}_scatterPlots_accumSolNum.pptx"
    title = "#{flightNum} - #{runID} - AccumSolNum scatter plots"
    variable = "accumSolNum"
    to_powerpoint_scatter_plot_by_variable(fpath,flightNum,runID,spath_full,title,variable,overwrite_all,keep_all)

    # Aitken sol mass scatter plots
    spath_full = spath + "#{flightNum}_#{runID}_scatterPlots_aitkenSolMass.pptx"
    title = "#{flightNum} - #{runID} - AitkenSolMass scatter plots"
    variable = "aitkenSolMass"
    to_powerpoint_scatter_plot_by_variable(fpath,flightNum,runID,spath_full,title,variable,overwrite_all,keep_all)

    # Aitken sol number scatter plots
    spath_full = spath + "#{flightNum}_#{runID}_scatterPlots_aitkenSolNum.pptx"
    title = "#{flightNum} - #{runID} - AitkenSolNum scatter plots"
    variable = "aitkenSolNum"
    to_powerpoint_scatter_plot_by_variable(fpath,flightNum,runID,spath_full,title,variable,overwrite_all,keep_all)

    # Coarse sol mass scatter plots
    spath_full = spath + "#{flightNum}_#{runID}_scatterPlots_coarseSolMass.pptx"
    title = "#{flightNum} - #{runID} - CoarseSolMass scatter plots"
    variable = "coarseSolMass"
    to_powerpoint_scatter_plot_by_variable(fpath,flightNum,runID,spath_full,title,variable,overwrite_all,keep_all)

    # Coarse sol number scatter plots
    spath_full = spath + "#{flightNum}_#{runID}_scatterPlots_coarseSolNum.pptx"
    title = "#{flightNum} - #{runID} - CoarseSolNum scatter plots"
    variable = "coarseSolNum"
    to_powerpoint_scatter_plot_by_variable(fpath,flightNum,runID,spath_full,title,variable,overwrite_all,keep_all)

    # Coarse dust mass scatter plots
    spath_full = spath + "#{flightNum}_#{runID}_scatterPlots_coarseDustMass.pptx"
    title = "#{flightNum} - #{runID} - CoarseDustMass scatter plots"
    variable = "coarseDustMass"
    to_powerpoint_scatter_plot_by_variable(fpath,flightNum,runID,spath_full,title,variable,overwrite_all,keep_all)

    # Coarse dust number scatter plots
    spath_full = spath + "#{flightNum}_#{runID}_scatterPlots_coarseDustNum.pptx"
    title = "#{flightNum} - #{runID} - CoarseDustNum scatter plots"
    variable = "coarseDustNum"
    to_powerpoint_scatter_plot_by_variable(fpath,flightNum,runID,spath_full,title,variable,overwrite_all,keep_all)

    # Active insol ice scatter plots
    spath_full = spath + "#{flightNum}_#{runID}_scatterPlots_activeInsolIce.pptx"
    title = "#{flightNum} - #{runID} - ActiveInsolIce scatter plots"
    variable = "activeInsolIce"
    to_powerpoint_scatter_plot_by_variable(fpath,flightNum,runID,spath_full,title,variable,overwrite_all,keep_all)

    # Active insol liquid scatter plots
    spath_full = spath + "#{flightNum}_#{runID}_scatterPlots_activeInsolLiquid.pptx"
    title = "#{flightNum} - #{runID} - ActiveInsolLiquid scatter plots"
    variable = "activeInsolLiquid"
    to_powerpoint_scatter_plot_by_variable(fpath,flightNum,runID,spath_full,title,variable,overwrite_all,keep_all)

    # Cloud liquid mass scatter plots
    spath_full = spath + "#{flightNum}_#{runID}_scatterPlots_cloudLiquidMass.pptx"
    title = "#{flightNum} - #{runID} - CloudLiquidMass scatter plots"
    variable = "cloudLiquidMass"
    to_powerpoint_scatter_plot_by_variable(fpath,flightNum,runID,spath_full,title,variable,overwrite_all,keep_all)

    # Cloud liquid number scatter plots
    spath_full = spath + "#{flightNum}_#{runID}_scatterPlots_cloudLiquidNum.pptx"
    title = "#{flightNum} - #{runID} - CloudLiquidNum scatter plots"
    variable = "cloudLiquidNum"
    to_powerpoint_scatter_plot_by_variable(fpath,flightNum,runID,spath_full,title,variable,overwrite_all,keep_all)

    # lwHeatingRate scatter plots
    spath_full = spath + "#{flightNum}_#{runID}_scatterPlots_lwHeatingRate.pptx"
    title = "#{flightNum} - #{runID} - lwheatingRate scatter plots"
    variable = "lwHeatingRate"
    to_powerpoint_scatter_plot_by_variable(fpath,flightNum,runID,spath_full,title,variable,overwrite_all,keep_all)

    # lwFluxDown scatter plots
    spath_full = spath + "#{flightNum}_#{runID}_scatterPlots_lwFluxDown.pptx"
    title = "#{flightNum} - #{runID} - lwFluxDown scatter plots"
    variable = "lwFluxDown"
    to_powerpoint_scatter_plot_by_variable(fpath,flightNum,runID,spath_full,title,variable,overwrite_all,keep_all)

    # lwFluxUp scatter plots
    spath_full = spath + "#{flightNum}_#{runID}_scatterPlots_lwFluxUp.pptx"
    title = "#{flightNum} - #{runID} - lwFluxUp scatter plots"
    variable = "lwFluxUp"
    to_powerpoint_scatter_plot_by_variable(fpath,flightNum,runID,spath_full,title,variable,overwrite_all,keep_all)

    # swHeatingRate scatter plots
    spath_full = spath + "#{flightNum}_#{runID}_scatterPlots_swHeatingRate.pptx"
    title = "#{flightNum} - #{runID} - swHeatingRate scatter plots"
    variable = "swHeatingRate"
    to_powerpoint_scatter_plot_by_variable(fpath,flightNum,runID,spath_full,title,variable,overwrite_all,keep_all)

    # swFluxDown scatter plots
    spath_full = spath + "#{flightNum}_#{runID}_scatterPlots_swFluxDown.pptx"
    title = "#{flightNum} - #{runID} - swFluxDown scatter plots"
    variable = "swFluxDown"
    to_powerpoint_scatter_plot_by_variable(fpath,flightNum,runID,spath_full,title,variable,overwrite_all,keep_all)

    # swFluxUp scatter plots
    spath_full = spath + "#{flightNum}_#{runID}_scatterPlots_swFluxUp.pptx"
    title = "#{flightNum} - #{runID} - swFluxUp scatter plots"
    variable = "swFluxUp"
    to_powerpoint_scatter_plot_by_variable(fpath,flightNum,runID,spath_full,title,variable,overwrite_all,keep_all)
end


###### MODEL OUTPUT PLOTS - times ######
puts "\n---------------"
puts "Create pptx of model output plots (by time)?"
puts "[y] or [n]?"
input = gets.chomp()
if input == "y"
    spath = "/home/vtrost/Documents/PhD/MONC_MAC_2020/#{flightNum.capitalize()}/Plots/Powerpoints/#{runID}/"
    fpath = "/home/vtrost/Documents/PhD/MONC_MAC_2020/F219/Plots/"

    # 10 min
    spath_full = spath + "#{flightNum}_#{runID}_scatterPlots_10min.pptx"
    title = "#{flightNum} - #{runID} - 10 minutes model time"
    timeID = "10min"
    to_powerpoint_scatter_plot_by_time(fpath,flightNum,runID,spath_full,title,timeID,overwrite_all,keep_all)

    # 1 hr
    spath_full = spath + "#{flightNum}_#{runID}_scatterPlots_1hr.pptx"
    title = "#{flightNum} - #{runID} - 1 hour model time"
    timeID = "1hr"
    to_powerpoint_scatter_plot_by_time(fpath,flightNum,runID,spath_full,title,timeID,overwrite_all,keep_all)

    # 2 hr
    spath_full = spath + "#{flightNum}_#{runID}_scatterPlots_2hr.pptx"
    title = "#{flightNum} - #{runID} - 2 hours model time"
    timeID = "2hr"
    to_powerpoint_scatter_plot_by_time(fpath,flightNum,runID,spath_full,title,timeID,overwrite_all,keep_all)

    # 3 hr
    spath_full = spath + "#{flightNum}_#{runID}_scatterPlots_3hr.pptx"
    title = "#{flightNum} - #{runID} - 3 hours model time"
    timeID = "3hr"
    to_powerpoint_scatter_plot_by_time(fpath,flightNum,runID,spath_full,title,timeID,overwrite_all,keep_all)

    # 4 hr
    spath_full = spath + "#{flightNum}_#{runID}_scatterPlots_4hr.pptx"
    title = "#{flightNum} - #{runID} - 4 hours model time"
    timeID = "4hr"
    to_powerpoint_scatter_plot_by_time(fpath,flightNum,runID,spath_full,title,timeID,overwrite_all,keep_all)

    # 5 hr
    spath_full = spath + "#{flightNum}_#{runID}_scatterPlots_5hr.pptx"
    title = "#{flightNum} - #{runID} - 5 hours model time"
    timeID = "5hr"
    to_powerpoint_scatter_plot_by_time(fpath,flightNum,runID,spath_full,title,timeID,overwrite_all,keep_all)

    # 6 hr
    spath_full = spath + "#{flightNum}_#{runID}_scatterPlots_6hr.pptx"
    title = "#{flightNum} - #{runID} - 6 hours model time"
    timeID = "6hr"
    to_powerpoint_scatter_plot_by_time(fpath,flightNum,runID,spath_full,title,timeID,overwrite_all,keep_all)
end


###### MODEL AVERAGE PLOTS ######
puts "\n---------------"
puts "Create pptx of model average plots?"
puts "[y] or [n]?"
input = gets.chomp()
if input == "y"
    spath_full = spath + "#{flightNum}_#{runID}_avgProfiles.pptx"
    fig1 = fpath + "#{flightNum}_#{runID}_temperature.png"
    fig2 = fpath + "#{flightNum}_#{runID}_liquidNumber.png"
    fig3 = fpath + "#{flightNum}_#{runID}_iceNumber.png"
    fig4 = fpath + "#{flightNum}_#{runID}_graupelNumber.png"
    fig5 = fpath + "#{flightNum}_#{runID}_snowNumber.png"
    fig6 = fpath + "#{flightNum}_#{runID}_rainNumber.png"
    fig7 = fpath + "#{flightNum}_#{runID}_RMSw.png"
    fig8 = fpath + "#{flightNum}_#{runID}_times.png"
    fig9 = fpath + "#{flightNum}_#{runID}_runNotes.png"
    fig10 = fpath + "#{flightNum}_#{runID}_liquidMass.png"
    fig11 = fpath + "#{flightNum}_#{runID}_iceMass.png"
    fig12 = fpath + "#{flightNum}_#{runID}_graupelMass.png"
    fig13 = fpath + "#{flightNum}_#{runID}_snowMass.png"
    fig14 = fpath + "#{flightNum}_#{runID}_rainMass.png"
    to_powerpoint_avg_plots(spath_full,fig1,fig2,fig3,fig4,fig5,fig6,fig7,fig8,fig9,fig10,fig11,fig12,fig13,fig14,title)
end