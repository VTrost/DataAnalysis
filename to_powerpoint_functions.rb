require 'powerpoint'

def to_powerpoint_scatter_plot_by_variable(fpath,flightNum,runID,spath_full,title,variable,overwrite_all,keep_all)
    time = Time.new
    @pp = Powerpoint::Presentation.new
    coords = {x: 1270000, y: 0, cx: 6921500, cy: 6921500}

    if File.file?(spath_full) and overwrite_all == false and keep_all == false
        puts ""
        puts "#{title} file already exists"
        puts "Overwrite file? [y] or [n]"
        ARGV.clear
        input = gets.chomp()
        if input != 'y'
            return
        end 
        puts ""
        puts "Rewriting #{title} file..."
    elsif File.file?(spath_full) and overwrite_all == true
        puts ""
        puts "Rewriting #{title} file..."
    elsif File.file?(spath_full) and overwrite_all == false and keep_all == true
        puts "Skipping #{title} file..."
        return
    else
        puts ""
        puts title
        puts "Writing #{title} file..."
    end

    fig = fpath + "#{flightNum}_#{runID}_scatterPlot_#{variable}_10min.png"
    if !File.file?(fig)
        puts "#{variable} file does not exist. Skipping file construction..."   
    else
        # Title slide
        title = title
        subtitle = time.strftime("%d %B %Y")
        @pp.add_intro title, subtitle

        # Text slide
        @pp.add_textual_slide "Plot Description", ['Each figure is the data from a single model timestep. The approximate time is listed in the figure title.','The y axis is altitude','The x axis is the variable','','Each data point represents a different (x,y) coordinate']

        # 10 min
        @pp.add_pictorial_slide "", fpath + "#{flightNum}_#{runID}_scatterPlot_#{variable}_10min.png", coords

        # 1 hr
        @pp.add_pictorial_slide "", fpath + "#{flightNum}_#{runID}_scatterPlot_#{variable}_1hr.png", coords

        # 2 hr
        @pp.add_pictorial_slide "", fpath + "#{flightNum}_#{runID}_scatterPlot_#{variable}_2hr.png", coords

        # 3 hr
        @pp.add_pictorial_slide "", fpath + "#{flightNum}_#{runID}_scatterPlot_#{variable}_3hr.png", coords

        # 4 hr
        @pp.add_pictorial_slide "", fpath + "#{flightNum}_#{runID}_scatterPlot_#{variable}_4hr.png", coords

        # 5 hr
        @pp.add_pictorial_slide "", fpath + "#{flightNum}_#{runID}_scatterPlot_#{variable}_5hr.png", coords

        # 6 hr
        @pp.add_pictorial_slide "", fpath + "#{flightNum}_#{runID}_scatterPlot_#{variable}_6hr.png", coords

        # Times 
        @pp.add_pictorial_slide "", fpath + "#{flightNum}_#{runID}_times.png"

        # Run notes 
        @pp.add_pictorial_slide "Run Notes", fpath + "#{flightNum}_#{runID}_runNotes.png"

        # Save file
        @pp.save(spath_full)
    end
end

##################################################################################################
def to_powerpoint_scatter_plot_by_time(fpath,flightNum,runID,spath_full,title,timeID,overwrite_all,keep_all)
    time = Time.new
    @pp = Powerpoint::Presentation.new
    coords = {x: 1270000, y: 0, cx: 6921500, cy: 6921500}

    if File.file?(spath_full) and overwrite_all == false and keep_all == false
        puts ""
        puts "#{title} file already exists"
        puts "Overwrite file? [y] or [n]"
        ARGV.clear
        input = gets.chomp()
        if input != 'y'
            return
        end 
        puts ""
        puts "Rewriting #{title} file..."
    elsif File.file?(spath_full) and overwrite_all == true
        puts ""
        puts "Rewriting #{title} file..."
    elsif File.file?(spath_full) and overwrite_all == false and keep_all == true
        puts "Skipping #{title} file..."
        return
    else
        puts ""
        puts title
        puts "Writing #{title} file..."
    end

    # Title slide
    title = title
    subtitle = time.strftime("%d %B %Y")
    @pp.add_intro title, subtitle

    # Text slide
    @pp.add_textual_slide "Plot Description", ['Each figure is the data from a single model timestep. The approximate time is listed in the figure title.','The y axis is altitude','The x axis is the variable','','Each data point represents a different (x,y) coordinate']

    # Temperature
    fig = fpath + "#{flightNum}_#{runID}_scatterPlot_temperature_#{timeID}.png"
    if File.file?(fig)
        @pp.add_pictorial_slide "", fig, coords
    else
        puts "temperature file does not exist. Skipping slide..."   
    end

    # Liquid number
    fig = fpath + "#{flightNum}_#{runID}_scatterPlot_liquidNum_#{timeID}.png"
    if File.file?(fig)
        @pp.add_pictorial_slide "", fig, coords
    else
        puts "liquidNum file does not exist. Skipping slide..."   
    end

    # Ice Number
    fig = fpath + "#{flightNum}_#{runID}_scatterPlot_iceNum_#{timeID}.png"
    if File.file?(fig)
        @pp.add_pictorial_slide "", fig, coords
    else
        puts "iceNum file does not exist. Skipping slide..."   
    end

    # Graupel number
    fig = fpath + "#{flightNum}_#{runID}_scatterPlot_graupelNum_#{timeID}.png"
    if File.file?(fig)
        @pp.add_pictorial_slide "", fig, coords
    else
        puts "graupelNum file does not exist. Skipping slide..."   
    end

    # Snow number
    fig = fpath + "#{flightNum}_#{runID}_scatterPlot_snowNum_#{timeID}.png"
    if File.file?(fig)
        @pp.add_pictorial_slide "", fig, coords
    else
        puts "snowNum file does not exist. Skipping slide..."   
    end

    # Rain number
    fig = fpath + "#{flightNum}_#{runID}_scatterPlot_rainNum_#{timeID}.png"
    if File.file?(fig)
        @pp.add_pictorial_slide "", fig, coords
    else
        puts "rainNum file does not exist. Skipping slide..."   
    end

    # W wind
    fig = fpath + "#{flightNum}_#{runID}_scatterPlot_WWind_#{timeID}.png"
    if File.file?(fig)
        @pp.add_pictorial_slide "", fig, coords
    else
        puts "WWind file does not exist. Skipping slide..."   
    end

    # Accum sol mass
    fig = fpath + "#{flightNum}_#{runID}_scatterPlot_accumSolMass_#{timeID}.png"
    if File.file?(fig)
        @pp.add_pictorial_slide "", fig, coords
    else
        puts "accumSolMass file does not exist. Skipping slide..."   
    end

    # Accum sol number
    fig = fpath + "#{flightNum}_#{runID}_scatterPlot_accumSolNum_#{timeID}.png"
    if File.file?(fig)
        @pp.add_pictorial_slide "", fig, coords
    else
        puts "accumSolNum file does not exist. Skipping slide..."   
    end

    # Aitken sol mass
    fig = fpath + "#{flightNum}_#{runID}_scatterPlot_aitkenSolMass_#{timeID}.png"
    if File.file?(fig)
        @pp.add_pictorial_slide "", fig, coords
    else
        puts "aitkenSolMass file does not exist. Skipping slide..."   
    end

    # Aitken sol number
    fig = fpath + "#{flightNum}_#{runID}_scatterPlot_aitkenSolNum_#{timeID}.png"
    if File.file?(fig)
        @pp.add_pictorial_slide "", fig, coords
    else
        puts "aitkenSolNum file does not exist. Skipping slide..."   
    end

    # Coarse sol mass
    fig = fpath + "#{flightNum}_#{runID}_scatterPlot_coarseSolMass_#{timeID}.png"
    if File.file?(fig)
        @pp.add_pictorial_slide "", fig, coords
    else
        puts "coarseSolMass file does not exist. Skipping slide..."   
    end

    # Coarse sol number
    fig = fpath + "#{flightNum}_#{runID}_scatterPlot_coarseSolNum_#{timeID}.png"
    if File.file?(fig)
        @pp.add_pictorial_slide "", fig, coords
    else
        puts "coarseSolNum file does not exist. Skipping slide..."   
    end

    # Coarse dust mass
    fig = fpath + "#{flightNum}_#{runID}_scatterPlot_coarseDustMass_#{timeID}.png"
    if File.file?(fig)
        @pp.add_pictorial_slide "", fig, coords
    else
        puts "coarseDustMass file does not exist. Skipping slide..."   
    end

    # Coarse dust number
    fig = fpath + "#{flightNum}_#{runID}_scatterPlot_coarseDustNum_#{timeID}.png"
    if File.file?(fig)
        @pp.add_pictorial_slide "", fig, coords
    else
        puts "coarseDustNum file does not exist. Skipping slide..."   
    end

    # Active insol ice
    fig = fpath + "#{flightNum}_#{runID}_scatterPlot_activeInsolIce_#{timeID}.png"
    if File.file?(fig)
        @pp.add_pictorial_slide "", fig, coords
    else
        puts "activeInsolIce file does not exist. Skipping slide..."   
    end

    # Active insol liquid
    fig = fpath + "#{flightNum}_#{runID}_scatterPlot_activeInsolLiquid_#{timeID}.png"
    if File.file?(fig)
        @pp.add_pictorial_slide "", fig, coords
    else
        puts "activeInsolLiquid file does not exist. Skipping slide..."   
    end

    # Cloud liquid mass
    fig = fpath + "#{flightNum}_#{runID}_scatterPlot_cloudLiquidMass_#{timeID}.png"
    if File.file?(fig)
        @pp.add_pictorial_slide "", fig, coords
    else
        puts "cloudLiquidMass file does not exist. Skipping slide..."   
    end

    # Cloud liquid number
    fig = fpath + "#{flightNum}_#{runID}_scatterPlot_cloudLiquidNum_#{timeID}.png"
    if File.file?(fig)
        @pp.add_pictorial_slide "", fig, coords
    else
        puts "cloudLiquidNum file does not exist. Skipping slide..."   
    end

    # LW heating rate
    fig = fpath + "#{flightNum}_#{runID}_scatterPlot_lwHeatingRate_#{timeID}.png"
    if File.file?(fig)
        @pp.add_pictorial_slide "", fig, coords
    else
        puts "lwHeatingRate file does not exist. Skipping slide..."   
    end

    # LW flux down
    fig = fpath + "#{flightNum}_#{runID}_scatterPlot_lwFluxDown_#{timeID}.png"
    if File.file?(fig)
        @pp.add_pictorial_slide "", fig, coords
    else
        puts "lwFluxDown file does not exist. Skipping slide..."   
    end

    # LW flux up
    fig = fpath + "#{flightNum}_#{runID}_scatterPlot_lwFluxUp_#{timeID}.png"
    if File.file?(fig)
        @pp.add_pictorial_slide "", fig, coords
    else
        puts "lwFluxUp file does not exist. Skipping slide..."   
    end

    # SW heating rate
    fig = fpath + "#{flightNum}_#{runID}_scatterPlot_swHeatingRate_#{timeID}.png"
    if File.file?(fig)
        @pp.add_pictorial_slide "", fig, coords
    else
        puts "swHeatingRate file does not exist. Skipping slide..."   
    end

    # SW flux down
    fig = fpath + "#{flightNum}_#{runID}_scatterPlot_swFluxDown_#{timeID}.png"
    if File.file?(fig)
        @pp.add_pictorial_slide "", fig, coords
    else
        puts "swFluxDown file does not exist. Skipping slide..."   
    end

    # SW flux up
    fig = fpath + "#{flightNum}_#{runID}_scatterPlot_swFluxUp_#{timeID}.png"
    if File.file?(fig)
        @pp.add_pictorial_slide "", fig, coords
    else
        puts "swFluxUp file does not exist. Skipping slide..."   
    end

    # Times
    @pp.add_pictorial_slide "", fpath + "#{flightNum}_#{runID}_times.png"

    # Run notes
    @pp.add_pictorial_slide "Run Notes", fpath + "#{flightNum}_#{runID}_runNotes.png"

    # Save file
    @pp.save(spath_full)
end

##################################################################################################################################

def to_powerpoint_avg_plots(spath_full,fig1,fig2,fig3,fig4,fig5,fig6,fig7,fig8,fig9,fig10,fig11,fig12,fig13,fig14,title)
    time = Time.new
    @pp = Powerpoint::Presentation.new
    coords = {x: 1270000, y: 0, cx: 6921500, cy: 6921500}

    if File.file?(spath_full)
        puts "#{title} file already exists"
        puts "Overwrite file? [y] or [n]"
        ARGV.clear
        input = gets.chomp()
        if input != 'y'
            return
        end 
        puts "Rewriting file..."
    else
        puts title
        puts "Writing new file..."
    end

    # Title slide
    title = title
    subtitle = time.strftime("%d %B %Y")
    @pp.add_intro title, subtitle

    # Temperature slide
    @pp.add_pictorial_slide "", fig1, coords

    # Liquid number slide
    @pp.add_pictorial_slide "", fig2, coords

    # Ice number slide
    @pp.add_pictorial_slide "", fig3, coords

    # Graupel number slide
    @pp.add_pictorial_slide "", fig4, coords

    # Snow number slide
    @pp.add_pictorial_slide "", fig5, coords

    # Rain number slide
    @pp.add_pictorial_slide "", fig6, coords

    # RMS W wind slide
    @pp.add_pictorial_slide "", fig7, coords

    # Liquid mass slide
    @pp.add_pictorial_slide "", fig10, coords

    # Ice mass slide
    @pp.add_pictorial_slide "", fig11, coords

    # Gaupel mass slide
    @pp.add_pictorial_slide "", fig12, coords

    # Snow mass slide
    @pp.add_pictorial_slide "", fig13, coords

    # Rain mass slide
    @pp.add_pictorial_slide "", fig14, coords

    # Run notes slide
    @pp.add_pictorial_slide "Run Notes", fig9

    # Times slide
    @pp.add_pictorial_slide "", fig8

    # Save file
    @pp.save(spath_full)
end

###################################################################################################

def to_powerpoint_init_profiles(path_full,flightNum,runID,spath_full,title,overwrite_all,keep_all)
    time = Time.new
    @pp = Powerpoint::Presentation.new
    coords = {x: 1270000, y: 0, cx: 6921500, cy: 6921500}

    if File.file?(spath_full) and overwrite_all == false and keep_all == false
        puts "\n#{title} file already exists"
        puts "Overwrite file? [y] or [n]"
        ARGV.clear
        input = gets.chomp()
        if input != 'y'
            return
        end 
        puts "Rewriting #{title} file..."
    elsif File.file?(spath_full) and overwrite_all == true
        puts "Rewriting #{title} file..."
    elsif File.file?(spath_full) and overwrite_all == false and keep_all == true
        puts "Skipping #{title} file..."
        return
    else
        puts title
        puts "Writing #{title} file..."
    end

    # Title slide
    title = title
    subtitle = time.strftime("%d %B %Y")
    @pp.add_intro title, subtitle

    # Potential temperature slide
    @pp.add_pictorial_slide "", path_full+"#{flightNum}_#{runID}_theta_inputProfile.png", coords

    # U  slide
    @pp.add_pictorial_slide "", path_full+"#{flightNum}_#{runID}_u_inputProfile.png", coords

    # V  slide
    @pp.add_pictorial_slide "", path_full+"#{flightNum}_#{runID}_v_inputProfile.png", coords

    # vapour  slide
    @pp.add_pictorial_slide "", path_full+"#{flightNum}_#{runID}_vapour_inputProfile.png", coords

    # liquid number slide
    @pp.add_pictorial_slide "", path_full+"#{flightNum}_#{runID}_cloud_liquid_number_inputProfile.png", coords

    # liquid mass slide
    @pp.add_pictorial_slide "", path_full+"#{flightNum}_#{runID}_cloud_liquid_mass_inputProfile.png", coords

    # coarse dust number slide
    @pp.add_pictorial_slide "", path_full+"#{flightNum}_#{runID}_coarse_dust_number_inputProfile.png", coords

    # coarse dust mass slide
    @pp.add_pictorial_slide "", path_full+"#{flightNum}_#{runID}_coarse_dust_mass_inputProfile.png", coords

    # ciarse sol number slide
    @pp.add_pictorial_slide "", path_full+"#{flightNum}_#{runID}_coarse_sol_number_inputProfile.png", coords

    # coarse sol mass slide
    @pp.add_pictorial_slide "", path_full+"#{flightNum}_#{runID}_coarse_sol_mass_inputProfile.png", coords

    # accum sol number slide
    @pp.add_pictorial_slide "", path_full+"#{flightNum}_#{runID}_accum_sol_number_inputProfile.png", coords

    # accum sol mass slide
    @pp.add_pictorial_slide "", path_full+"#{flightNum}_#{runID}_accum_sol_mass_inputProfile.png", coords

    # aitken sol number slide
    @pp.add_pictorial_slide "", path_full+"#{flightNum}_#{runID}_aitken_sol_number_inputProfile.png", coords

    # aitken sol mass slide
    @pp.add_pictorial_slide "", path_full+"#{flightNum}_#{runID}_aitken_sol_mass_inputProfile.png", coords

    # active_insol_liquid slide
    @pp.add_pictorial_slide "", path_full+"#{flightNum}_#{runID}_active_insol_liquid_inputProfile.png", coords

    # active insol ice slide
    @pp.add_pictorial_slide "", path_full+"#{flightNum}_#{runID}_active_insol_ice_inputProfile.png", coords

    # run notes slide
    @pp.add_pictorial_slide "", "/home/vtrost/Documents/PhD/MONC_MAC_2020/#{flightNum.capitalize()}/Plots/#{flightNum}_#{runID}_runNotes.png"

    # Save file
    @pp.save(spath_full)
end